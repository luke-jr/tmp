#!/usr/bin/env bash
# Pin the assemble-knots/ submodule to the SHA that was current when
# the target spec was last touched. The default checkout follows the
# spec branch's CURRENT submodule pointer, which may have advanced
# past release time; we want the driver the Knots maintainers actually used.
#
# Walks the spec repo's history for the last commit that touched
# $SPEC, reads ITS submodule pointer, checks that SHA out in
# $ASSEMBLE.

set -euo pipefail
. "$(dirname "$0")/lib.sh"

git -C "$TMP" rev-parse --git-dir >/dev/null 2>&1 \
  || die "$TMP is not a git repository (need spec repo history for submodule pin)"

[ -f "$SPEC" ] || die "spec not found: $SPEC"

# Idempotent submodule init for a fresh local clone without
# --recurse-submodules.
sub_path="$(basename "$ASSEMBLE")"
if [ ! -e "$ASSEMBLE/.git" ]; then
  say "initialising $sub_path submodule"
  git -C "$TMP" submodule update --init -- "$sub_path"
fi

spec_rel="$(basename "$SPEC")"
spec_commit=$(git -C "$TMP" log -n 1 --format='%H' -- "$spec_rel")
[ -n "$spec_commit" ] || die "no commit in $TMP touched $spec_rel"

driver_sha=$(git -C "$TMP" ls-tree "$spec_commit" "$sub_path" | awk '{print $3}')
[ -n "$driver_sha" ] || die "no $sub_path submodule pointer at $spec_commit"

say "pinning $sub_path to $driver_sha (spec commit $spec_commit)"
git -C "$ASSEMBLE" fetch --quiet origin "$driver_sha" 2>/dev/null || true
git -C "$ASSEMBLE" -c advice.detachedHead=false checkout "$driver_sha"
say "$sub_path HEAD -> $(git -C "$ASSEMBLE" rev-parse HEAD)"
