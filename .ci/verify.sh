#!/usr/bin/env bash
# Verify that the driver's output matches $RELEASE_TAG at four
# progressively weaker levels:
#   1. Byte-exact SHA match — strongest; what a tag-signature verifier needs.
#   2. HEAD tree hash match — source identical, only metadata diverged.
#   3. First-parent tree match (pairwise walk) — diagnostic; finds the first
#      point of divergence.
#   4. Working tree diff — weakest; just "files match".
#
# Ported from knots-knowledge/scripts/40-verify.sh.

set -euo pipefail
. "$(dirname "$0")/lib.sh"

[ -d "$REPRO/.git" ] || [ -f "$REPRO/.git" ] || die "no worktree at $REPRO (run run-driver.sh first)"

# Append a markdown block to $GITHUB_STEP_SUMMARY when running in GH
# Actions; no-op otherwise.
emit_summary() {
  [ -n "${GITHUB_STEP_SUMMARY:-}" ] || return 0
  printf '%s\n' "$@" >> "$GITHUB_STEP_SUMMARY"
}

BASE_TAG="$(resolve_base_tag)"
repro_head=$(git -C "$REPRO" rev-parse HEAD)
target_head=$(git -C "$BITCOIN" rev-parse "$RELEASE_TAG^{commit}")

say "repro HEAD  : $repro_head"
say "target      : $target_head"
echo

# Level 1: commit SHA
if [ "$repro_head" = "$target_head" ]; then
  say "LEVEL 1 PASS: byte-exact SHA match"
  echo "reproduction is bit-identical to $RELEASE_TAG"
  emit_summary \
    "## Reproduction: \`$RELEASE_TAG\`" \
    "" \
    "**PASS** — byte-exact SHA match against the published release tag." \
    "" \
    "| field        | value |" \
    "|--------------|-------|" \
    "| spec         | \`$(basename "$SPEC")\` |" \
    "| base tag     | \`$BASE_TAG\` |" \
    "| target SHA   | \`$target_head\` |" \
    "| reproduced   | \`$repro_head\` |"
  exit 0
fi

say "LEVEL 1 FAIL: SHAs differ"
echo

# Level 2: final tree hash
repro_tree=$(git -C "$REPRO" rev-parse 'HEAD^{tree}')
target_tree=$(git -C "$BITCOIN" rev-parse "$RELEASE_TAG^{tree}")
say "repro tree  : $repro_tree"
say "target tree : $target_tree"

if [ "$repro_tree" = "$target_tree" ]; then
  say "LEVEL 2 PASS: final source tree matches (only commit metadata diverged)"
else
  say "LEVEL 2 FAIL: final tree differs"
fi
echo

# Level 3: walk first-parent chains, find first divergence
say "LEVEL 3: first-parent pairwise tree match"
repro_chain=$(git -C "$REPRO" log --first-parent --reverse --pretty='%H %T' "$BASE_TAG..$repro_head")
target_chain=$(git -C "$BITCOIN" log --first-parent --reverse --pretty='%H %T' "$BASE_TAG..$target_head")

repro_count=$(printf '%s\n' "$repro_chain" | wc -l)
target_count=$(printf '%s\n' "$target_chain" | wc -l)
say "first-parent commit count — repro: $repro_count  target: $target_count"

paste <(printf '%s\n' "$repro_chain") <(printf '%s\n' "$target_chain") | \
  awk 'BEGIN {n=0}
       {n++; split($0,a,"\t");
        split(a[1],x," "); split(a[2],y," ");
        if (x[2] != y[2]) {
          printf("  first divergence at first-parent commit #%d\n", n);
          printf("  repro:  %s  tree=%s\n", x[1], x[2]);
          printf("  target: %s  tree=%s\n", y[1], y[2]);
          exit 1
        }}
       END {if (n == 0) exit 2}'
awk_ec=$?
case "$awk_ec" in
  0) say "LEVEL 3 PASS: every first-parent tree matches pairwise" ;;
  1) : ;;
  *) say "LEVEL 3 SKIP: no commits to compare" ;;
esac
echo

# Level 4: working tree diff
say "LEVEL 4: raw file diff between repro HEAD and target tag"
set +e
diff_count=$(git -C "$REPRO" diff --stat "$repro_head" "$target_head" | tail -1)
set -e
echo "  $diff_count"

say "verification complete"

if [ "$repro_tree" = "$target_tree" ]; then
  level2="**PARTIAL** — tree-exact, commit metadata diverged"
else
  level2="**FAIL** — final tree differs from $RELEASE_TAG"
fi
emit_summary \
  "## Reproduction: \`$RELEASE_TAG\`" \
  "" \
  "$level2" \
  "" \
  "| field        | value |" \
  "|--------------|-------|" \
  "| spec         | \`$(basename "$SPEC")\` |" \
  "| base tag     | \`$BASE_TAG\` |" \
  "| target SHA   | \`$target_head\` |" \
  "| reproduced   | \`$repro_head\` |" \
  "| target tree  | \`$target_tree\` |" \
  "| repro tree   | \`$repro_tree\` |"

[ "$repro_head" = "$target_head" ] && exit 0 || exit 1
