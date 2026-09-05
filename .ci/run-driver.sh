#!/usr/bin/env bash
# Run assemble-knots.pl against the spec for $RELEASE_TAG inside an isolated
# worktree.
#
# Sets the three environment invariants that byte-exact SHA reproduction
# depends on:
#   TZ=UTC                       so bare spec timestamps resolve to +0000
#   user.email=<maintainer's>    so committer metadata bytes match
#   merge.conflictStyle=diff3    so the driver's smartconflicthealer can
#                                parse conflict markers (it REQUIRES the
#                                ||||||| common-ancestor section that only
#                                diff3 style emits)
# The driver hardcodes the committer name ("merge-script") but nothing else.
#
# Ported from knots-knowledge/scripts/30-run-driver.sh.

set -euo pipefail
. "$(dirname "$0")/lib.sh"

[ -d "$BITCOIN/.git" ] || die "no bitcoin clone at $BITCOIN"
[ -f "$SPEC" ]          || die "no spec at $SPEC"
[ -x "$ASSEMBLE/assemble-knots.pl" ] || die "no driver at $ASSEMBLE/assemble-knots.pl"

BASE_TAG="$(resolve_base_tag)"
[ -n "$BASE_TAG" ] || die "could not resolve base tag from spec $SPEC"

mkdir -p "$OUT"

# Fresh worktree. Nuke previous if present, then prune any stale registration.
if [ -e "$REPRO" ]; then
  say "removing previous worktree at $REPRO"
  git -C "$BITCOIN" worktree remove --force "$REPRO" 2>/dev/null || rm -rf "$REPRO"
fi
git -C "$BITCOIN" worktree prune 2>/dev/null || true
say "creating fresh worktree at $REPRO (detached at $BASE_TAG)"
git -C "$BITCOIN" worktree add --detach "$REPRO" "$BASE_TAG"

# The driver looks up conflict resolutions at CWD/assemble-knots-resolutions.
ln -sfn "$TMP/assemble-knots-resolutions" "$REPRO/assemble-knots-resolutions"
say "linked assemble-knots-resolutions -> $TMP/assemble-knots-resolutions"

git -C "$REPRO" config user.email "$COMMITTER_EMAIL"
git -C "$REPRO" config user.name  "merge-script"

# merge.conflictStyle=diff3 is REQUIRED by the driver's smartconflicthealer.
# With the default 2-way style (no |||||||), the healer's state machine
# fails at the ======= marker and falls through to the interactive user
# prompt on every conflict — even trivial filelist/#include unions the
# healer is designed to handle automatically.
git -C "$REPRO" config merge.conflictStyle diff3

say "worktree git config: user.email=$(git -C "$REPRO" config user.email), user.name=$(git -C "$REPRO" config user.name), merge.conflictStyle=$(git -C "$REPRO" config merge.conflictStyle)"

# Pre-process the spec. Two layers:
#
# (1) Blanket: comment out all (CHECK-LAST) lines.
#     CHECK-LAST lines verify that a tracked upstream ref still matches a
#     recorded SHA and die if not. They never modify the working tree or
#     make commits. The driver's --skip-update-check flag suppresses the
#     analogous check on regular merge lines but NOT CHECK-LAST. For
#     reproducing an already-published release, every CHECK-LAST ref is by
#     definition historical; commenting them out is semantically safe.
#
# (2) Per-release: apply .ci/overrides/$RELEASE_TAG.sed if present.
say "pre-processing spec: $(basename "$SPEC") -> $(basename "$SPEC_IN")"
sed 's/^\(\s*(CHECK-LAST)\)/#\1/' "$SPEC" > "$SPEC_IN"
checklast_count=$(diff "$SPEC" "$SPEC_IN" | grep -c '^<' || true)
say "  CHECK-LAST lines commented: $checklast_count"

# Auto-generated spec rewrites from synthesize-refs.sh: cherrypick-source
# substitutions and `last=` pins for unpinned direct-remote merges.
AUTO_SED="$OUT/${TAG_SHORT}.auto-overrides.sed"
if [ -s "$AUTO_SED" ]; then
  sed -i -f "$AUTO_SED" "$SPEC_IN"
  say "  applied synthesized spec overrides: $(wc -l < "$AUTO_SED") substitutions"
fi

# Per-release manual override.
if [ -f "$OVERRIDE_SED" ]; then
  pre_hash=$(md5sum "$SPEC_IN" | awk '{print $1}')
  sed -i -f "$OVERRIDE_SED" "$SPEC_IN"
  post_hash=$(md5sum "$SPEC_IN" | awk '{print $1}')
  if [ "$pre_hash" != "$post_hash" ]; then
    say "  applied per-release override: $(basename "$OVERRIDE_SED")"
  else
    say "  per-release override present but matched nothing: $(basename "$OVERRIDE_SED")"
  fi
else
  say "  no per-release override at $OVERRIDE_SED"
fi

# Stream the driver log to a capped file.
# Safety (driver has an interactive conflict prompt that spins forever on
# closed stdin): yes 2 -> "Aborted" on first unhandled conflict; head -c
# caps log size; timeout enforces wall-clock limit.
LOG_CAP="200M"
RUN_TIMEOUT="30m"
rm -f "$OUTSPEC" "$DRIVER_LOG"

# Optional pinned git for the driver's own merges. The driver keys recorded
# conflict resolutions by `git patch-id` of the conflict text, and the diff3
# `|||||||` ancestor marker changed in git 2.24.0. Set KNOTS_DRIVER_GIT_DIR
# to a directory whose `git` is a pre-2.24 build for old-spec reproduction;
# unset = host git.
DRIVER_GIT_DIR="${KNOTS_DRIVER_GIT_DIR:-}"
if [ -n "$DRIVER_GIT_DIR" ]; then
  [ -x "$DRIVER_GIT_DIR/git" ] || die "KNOTS_DRIVER_GIT_DIR has no executable git: $DRIVER_GIT_DIR"
  say "driver git pinned: $("$DRIVER_GIT_DIR/git" --version) ($DRIVER_GIT_DIR)"
fi

say "running driver for $RELEASE_TAG (base $BASE_TAG)"
say "safety: timeout=$RUN_TIMEOUT log cap=$LOG_CAP stdin=yes(2) log=$DRIVER_LOG"
set +e
(
  cd "$REPRO"
  [ -n "$DRIVER_GIT_DIR" ] && export PATH="$DRIVER_GIT_DIR:$PATH"
  yes 2 | TZ="$REPRO_TZ" timeout "$RUN_TIMEOUT" \
    perl "$ASSEMBLE/assemble-knots.pl" \
      --skip-update-check \
      -o "$OUTSPEC" \
      "$SPEC_IN" 2>&1
) | head -c "$LOG_CAP" > "$DRIVER_LOG"
ec="${PIPESTATUS[0]}"
set -e

say "driver exit code: $ec"
say "worktree HEAD: $(git -C "$REPRO" rev-parse HEAD)"
say "target commit: $(git -C "$BITCOIN" rev-parse "${RELEASE_TAG}^{commit}")"

# Don't propagate $ec. It's non-zero on every successful run for two
# unrelated reasons:
#   - SIGPIPE 141: the `yes 2` feeder gets killed when the driver finishes
#     reading stdin.
#   - Exit 255 on older specs whose tail has a `TODO:` line the pinned
#     older driver doesn't recognise; by that point the target commit is
#     already on HEAD.
# verify.sh is the authority on whether the run succeeded.
exit 0
