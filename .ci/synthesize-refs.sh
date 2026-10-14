#!/usr/bin/env bash
# After the fetch step in the CI workflow brings all required commits into
# the object database, this script forces every branch ref to match its
# release-time SHA, taken from the second parent of each merge commit on
# the first-parent chain of the target release.
#
# Why:
#   luke-jr/bitcoin feature branches are MUTABLE. The Knots maintainers keep
#   advancing them after a release is tagged. Fetching the current tip gives
#   newer commits than what they actually merged at release time; the driver
#   then merges the newer tip, produces a diverging tree, and downstream
#   merges hit conflicts the recorded autoresolvers don't match.
#
#   For historical reproduction, the authoritative source for branch tips
#   is the release tag itself: each "Merge <prnum> via <branch>" commit on
#   the first-parent chain has the branch's release-time tip as its second
#   parent. We walk every such commit and update-ref accordingly.
#
# Ported from knots-knowledge/scripts/15-synthesize-refs.sh.

set -euo pipefail
. "$(dirname "$0")/lib.sh"

[ -d "$BITCOIN/.git" ] || die "$BITCOIN is not a git clone"

BASE_TAG="$(resolve_base_tag)"
git -C "$BITCOIN" rev-parse --verify --quiet "$RELEASE_TAG" >/dev/null \
  || die "$RELEASE_TAG not present; fetch it first"
git -C "$BITCOIN" rev-parse --verify --quiet "$BASE_TAG" >/dev/null \
  || die "$BASE_TAG not present; fetch it first"

mkdir -p "$OUT"

# Auto-generated spec overrides: sed substitutions for cherrypick sources
# the Knots maintainers keep only in a local working repo. For each spec line
# `(cherrypick=X) Y` where X is not in our object database, Y is the
# previous release's equivalent commit; find the current release's
# equivalent commit Z and substitute X with Z. Two strategies, in order:
#
#   1. parent2-of-merge: works when the driver wraps the cherrypick in a
#      merge commit with parent2 == Y (drivers v29.2+).
#   2. file-set match: works when the cherrypick landed as a plain
#      non-merge commit (older drivers). Matches by the file-set the
#      commit touches relative to its first parent.
AUTO_SED="$OUT/${TAG_SHORT}.auto-overrides.sed"
: > "$AUTO_SED"

file_set_of() {
  git -C "$BITCOIN" diff --name-only "$1^1" "$1" 2>/dev/null \
    | sort \
    | tr '\n' '|'
}

declare -A PARENT2_TO_COMMIT
while IFS='|' read -r csha cpar; do
  p2=$(printf '%s\n' "$cpar" | awk '{print $2}')
  [ -n "$p2" ] || continue
  PARENT2_TO_COMMIT[$p2]="$csha"
done < <(git -C "$BITCOIN" log --first-parent --merges --pretty='%H|%P' "$BASE_TAG..$RELEASE_TAG")

declare -A FILESET_TO_COMMIT
while read -r csha; do
  fs=$(file_set_of "$csha")
  [ -n "$fs" ] || continue
  FILESET_TO_COMMIT[$fs]="$csha"
done < <(git -C "$BITCOIN" log --first-parent --pretty='%H' "$BASE_TAG..$RELEASE_TAG")

cherrypick_fixed=0
while IFS=$'\t' read -r cherry lastapply; do
  if git -C "$BITCOIN" cat-file -e "$cherry" 2>/dev/null; then
    continue
  fi
  if ! git -C "$BITCOIN" cat-file -e "$lastapply" 2>/dev/null; then
    say "  WARN: cherrypick=$cherry has unreachable lastapply $lastapply; cannot auto-substitute"
    continue
  fi
  substitute=""
  for p2key in "${!PARENT2_TO_COMMIT[@]}"; do
    if [ "${p2key#$lastapply}" != "$p2key" ]; then
      substitute="${PARENT2_TO_COMMIT[$p2key]}"
      break
    fi
  done
  if [ -z "$substitute" ]; then
    fs=$(file_set_of "$lastapply")
    if [ -z "$fs" ]; then
      say "  WARN: empty file-set for lastapply $lastapply (cherrypick=$cherry); cannot auto-substitute"
      continue
    fi
    substitute="${FILESET_TO_COMMIT[$fs]:-}"
    if [ -z "$substitute" ]; then
      say "  WARN: no release commit matches file-set of lastapply $lastapply for cherrypick=$cherry"
      continue
    fi
  fi
  printf 's/cherrypick=%s/cherrypick=%s/\n' "$cherry" "$substitute" >> "$AUTO_SED"
  cherrypick_fixed=$((cherrypick_fixed+1))
done < <(perl -ne '
  s/\s*#.*//;
  next unless /\(cherrypick=([a-f0-9]+)\)\s+([a-f0-9]+)/;
  print "$1\t$2\n";
' "$SPEC")

say "walking $BASE_TAG..$RELEASE_TAG merges, pinning refs to release-time SHAs"
printf '%s\t%s\t%s\t%s\n' branch release_sha current_sha_at_run status > "$DRIFT_LOG"

match=0; drift=0; created=0; skipped_nm=0; skipped_unparsed=0; caret=0; directpin=0

while IFS='|' read -r sha subject parents; do
  is_null=0
  case "$subject" in
    "NULL-Merge "*) is_null=1 ;;
  esac

  if [[ "$subject" =~ ^(NULL-|Tree-)?Merge\ ([a-zA-Z0-9#]+\ via\ )?(.+)$ ]]; then
    branch="${BASH_REMATCH[3]}"
  else
    skipped_unparsed=$((skipped_unparsed+1))
    continue
  fi

  caret_suffix=""
  if [[ "$branch" == *"^"* ]]; then
    caret_suffix="${branch#*^}^"
    branch="${branch%%^*}"
  fi

  if [ "$is_null" = "1" ]; then
    skipped_nm=$((skipped_nm+1))
    continue
  fi

  parent2=$(printf '%s\n' "$parents" | awk '{print $2}')
  [ -n "$parent2" ] || continue

  # Direct remote merge: the driver refuses to merge any slash-form remote
  # ref without a `last=` pin (unpinned slash-form merges are
  # non-deterministic). Old specs frequently omit the pin since it was
  # ambient at authoring time. parent2 IS the release-time tip, so emit a
  # spec rewrite appending `last=<parent2>` to that line when it has none.
  if [[ "$branch" == */* ]]; then
    needs_pin=$(perl -ne '
      s/\s*#.*//;
      next unless /^\s*(?:NM|TM|[am]*)\t\s*(?:[a-z]?\d+|\-|n\/a)\s+(\S+)/;
      next unless $1 eq "'"$branch"'";
      print "yes" unless /last=/;
      exit;
    ' "$SPEC")
    if [ "$needs_pin" = "yes" ]; then
      printf 's#%s#%s last=%s#\n' "$branch" "$branch" "$parent2" >> "$AUTO_SED"
      printf '%s\t%s\t%s\t%s\n' "$branch" "$parent2" "-" "direct-pin" >> "$DRIFT_LOG"
      directpin=$((directpin+1))
    fi
  fi

  case "$branch" in
    */*) ref="refs/remotes/$branch" ;;
    *)   ref="refs/heads/$branch"   ;;
  esac

  if [ -n "$caret_suffix" ]; then
    # Caret-suffix merge ("<branch>^", "<branch>^^", ...): the driver
    # runs `git merge <branch><carets>` AND bakes column 2 verbatim
    # into the commit message ("Merge <pr> via <branch><carets>"), so
    # the spec line must stay untouched — we can only move the ref.
    # The commit that `<carets>` should dereference to is routinely an
    # orphaned SHA after the branch is rebased upstream; rather than
    # fetch that orphan, fabricate a chain of stand-in commits so that
    # `<branch>` followed by N carets walks down to parent2 — what
    # `<branch><carets>` resolved to at release time, straight from
    # the merge graph. One stand-in per caret: each is parented on the
    # next, the last on parent2. The stand-ins are never merged (only
    # their `^` chain is read), so their trees/identities are
    # irrelevant. No fetch, no orphan, no REST API.
    #
    # caret_suffix is a run of '^' chars; ${#caret_suffix} = N.
    synth="$parent2"
    i=0
    while [ "$i" -lt "${#caret_suffix}" ]; do
      synth=$(GIT_AUTHOR_NAME=synthetic GIT_AUTHOR_EMAIL=synthetic@localhost \
              GIT_COMMITTER_NAME=synthetic GIT_COMMITTER_EMAIL=synthetic@localhost \
              git -C "$BITCOIN" commit-tree "$parent2^{tree}" -p "$synth" \
                -m "synthetic caret stand-in #$((i+1)) for ${branch}${caret_suffix}")
      i=$((i+1))
    done
    git -C "$BITCOIN" update-ref "$ref" "$synth"
    printf '%s\t%s\t%s\t%s\n' "${branch}${caret_suffix}" "$parent2" "-" "caret-synthetic" >> "$DRIFT_LOG"
    caret=$((caret+1))
    continue
  fi

  current=$(git -C "$BITCOIN" rev-parse --verify --quiet "$ref" 2>/dev/null || true)
  if [ -z "$current" ]; then
    git -C "$BITCOIN" update-ref "$ref" "$parent2"
    printf '%s\t%s\t%s\t%s\n' "$branch" "$parent2" "-" "created" >> "$DRIFT_LOG"
    created=$((created+1))
  elif [ "$current" = "$parent2" ]; then
    match=$((match+1))
  else
    git -C "$BITCOIN" update-ref "$ref" "$parent2"
    printf '%s\t%s\t%s\t%s\n' "$branch" "$parent2" "$current" "drift" >> "$DRIFT_LOG"
    drift=$((drift+1))
  fi
done < <(git -C "$BITCOIN" log --first-parent --merges --pretty='%H|%s|%P' "$BASE_TAG..$RELEASE_TAG")

say "synthesis complete"
say "  match:     $match branches already at release-time SHA"
say "  drift:     $drift branches overwritten (pre-drift SHA logged)"
say "  created:   $created new refs (no prior fetch target)"
say "  skipped:   $skipped_nm NULL-merges (parent2 is a runtime-generated revert)"
say "  caret:     $caret caret-suffix merges resolved via last=<sha> fetch"
say "  directpin: $directpin unpinned direct-remote merges given synthesized last="
say "  crp-fix:   $cherrypick_fixed cherrypick sources auto-substituted"
[ -s "$AUTO_SED" ] && say "  auto-overrides file: $AUTO_SED"
[ "$skipped_unparsed" -eq 0 ] || say "  unparsed: $skipped_unparsed merge subjects I couldn't match"
say "drift log: $DRIFT_LOG"

if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
  {
    echo "## Synthesized release-time refs"
    echo
    echo "Branch refs rewritten to the SHAs that were current when \`$RELEASE_TAG\` was tagged."
    echo
    echo "| metric | count |"
    echo "|--------|-------|"
    echo "| already at release-time SHA | $match |"
    echo "| drift (overwritten)         | $drift |"
    echo "| new refs created            | $created |"
    echo "| NULL-merges skipped         | $skipped_nm |"
    echo "| caret-suffix resolutions    | $caret |"
    echo "| direct-pin synthesis        | $directpin |"
    echo "| cherrypick substitutions    | $cherrypick_fixed |"
  } >> "$GITHUB_STEP_SUMMARY"
fi
