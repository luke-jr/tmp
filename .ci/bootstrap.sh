#!/usr/bin/env bash
# Clone bitcoinknots/bitcoin and configure it with every remote +
# refspec the target spec needs. Idempotent: a pre-existing clone at
# $BITCOIN is reused; existing remotes are updated in place.
#
# Previously inlined in .github/workflows/reproduce.yml as five
# separate steps (clone, configure remotes, fetch all, fetch base tag,
# create master ref). Promoted to a script so the workflow and a
# direct local invocation drive the same code.

set -euo pipefail
. "$(dirname "$0")/lib.sh"

BASE_TAG="$(resolve_base_tag)"
[ -n "$BASE_TAG" ] || die "could not resolve base tag from spec $SPEC"

EXTRACT="${EXTRACT_REMOTES:-$TMP/extract-remotes.pl}"
[ -x "$EXTRACT" ] || die "extract-remotes.pl not found at $EXTRACT"

mkdir -p "$OUT"

# 1. Clone (or reuse) bitcoinknots/bitcoin. The Knots release tag is
# only present on this remote, not on bitcoin/bitcoin upstream.
if [ -d "$BITCOIN/.git" ]; then
  say "reusing existing bitcoin clone at $BITCOIN"
  # Prune prior-run state so a second invocation against a different
  # tag starts clean. Without this, remotes from the previous spec
  # stick around in .git/config and synthesize-refs's prior
  # rewrites of refs/heads/* shadow the current spec — any branch
  # synthesize-refs can't parse for the current release is left at
  # the wrong release's tip.
  say "  pruning non-origin remotes and synthesized refs from prior runs"
  for r in $(git -C "$BITCOIN" remote | grep -vxF origin); do
    git -C "$BITCOIN" remote remove "$r"
  done
  git -C "$BITCOIN" for-each-ref --format='delete %(refname)' refs/heads/ \
    | grep -vxF 'delete refs/heads/master' \
    | git -C "$BITCOIN" update-ref --stdin
else
  say "cloning bitcoinknots/bitcoin -> $BITCOIN"
  git clone https://github.com/bitcoinknots/bitcoin.git "$BITCOIN"
fi

# 2. Translate the spec into a remote-config table:
#    REMOTE_NAME<TAB>URL<TAB>REFSPEC, one row per refspec.
REMOTES_TSV="$OUT/${TAG_SHORT}.remotes.tsv"
perl "$EXTRACT" < "$SPEC" > "$REMOTES_TSV"
n_remotes=$(awk -F'\t' '{print $1}' "$REMOTES_TSV" | sort -u | wc -l)
n_refspecs=$(wc -l < "$REMOTES_TSV")
say "spec needs $n_remotes remotes, $n_refspecs refspecs"

# First pass: add (or update) each unique remote and clear stale
# fetch lines. set-url is idempotent; remote add is not.
awk -F'\t' '!seen[$1]++ {print $1"\t"$2}' "$REMOTES_TSV" | \
  while IFS=$'\t' read -r name url; do
    if git -C "$BITCOIN" remote | grep -qxF "$name"; then
      git -C "$BITCOIN" remote set-url "$name" "$url"
    else
      git -C "$BITCOIN" remote add "$name" "$url"
    fi
    git -C "$BITCOIN" config --unset-all "remote.$name.fetch" 2>/dev/null || true
  done

# Second pass: append every refspec to its remote.
while IFS=$'\t' read -r name _ refspec; do
  git -C "$BITCOIN" config --add "remote.$name.fetch" "$refspec"
done < "$REMOTES_TSV"

# extract-remotes.pl emits `upstream` for master only; ensure the
# release's base tag is fetched too.
git -C "$BITCOIN" config --add remote.upstream.fetch \
  "+refs/tags/$BASE_TAG:refs/tags/$BASE_TAG"

# 3. Fetch every configured remote except origin (which we just
# cloned and is already current).
#
# Tolerate per-remote failures. Developer forks routinely delete
# branches (or whole forks go private/away) after a release ships;
# `git fetch --multiple` returns non-zero if ANY remote fails, even
# when the other dozen succeed. A branch actually merged into the
# release still has its release-time tip recoverable by
# synthesize-refs from the release tag's merge graph, so a missing
# dev-fork branch is not fatal here. Report the failures instead of
# letting set -e kill the run silently.
say "fetching $n_remotes remotes (parallelized)"
remotes=$(git -C "$BITCOIN" remote | grep -vxF origin | tr '\n' ' ')
if ! git -C "$BITCOIN" fetch --multiple --no-tags --prune -j8 $remotes; then
  say "  NOTE: one or more remotes failed (deleted branch / removed fork)."
  say "  synthesize-refs recovers release-time SHAs from the release tag's"
  say "  merge graph; only fatal if a needed SHA is genuinely unrecoverable."
fi

# 4. Tags don't come with --no-tags fetches; pull the base tag
# explicitly. The Knots release tag is already in origin's tag
# namespace from the initial clone.
say "fetching base tag $BASE_TAG"
git -C "$BITCOIN" fetch upstream "refs/tags/$BASE_TAG:refs/tags/$BASE_TAG"

if ! git -C "$BITCOIN" rev-parse --verify --quiet "refs/tags/$RELEASE_TAG" >/dev/null; then
  die "release tag $RELEASE_TAG missing from $BITCOIN; expected from origin = bitcoinknots/bitcoin"
fi
say "release tag $RELEASE_TAG -> $(git -C "$BITCOIN" rev-parse "$RELEASE_TAG")"

# 5. The driver's poison-check expects a local `master` ref. Point it
# at upstream/master so the check has something to compare against.
git -C "$BITCOIN" update-ref refs/heads/master \
  "$(git -C "$BITCOIN" rev-parse upstream/master)"
say "local master ref -> $(git -C "$BITCOIN" rev-parse master)"
