#!/usr/bin/env bash
# shellcheck shell=bash
# Shared variables and helpers for the in-repo reproduction CI.
#
# Ported from knots-knowledge/scripts/lib.sh with the fork's layout baked
# into the defaults: this repo (the luke-jr/tmp fork) plays the role of
# the knots-knowledge superproject's TMP/ clone, and the driver lives at
# the `assemble-knots/` submodule rather than a sibling `assemble-deriv/`.
# Every path defaults via ${X:-…} so the CI workflow can override without
# editing this file.
#
# The target release is driven by the KNOTS_TAG environment variable.

set -euo pipefail

# The pipeline only ever fetches public repos. Some developer-fork remotes
# still trigger an HTTPS username prompt (e.g. when a referenced branch was
# deleted), which would hang an unattended run forever. Fail fast instead.
export GIT_TERMINAL_PROMPT=0

ROOT="${KNOTS_CI_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

# In the knots-knowledge layout, the fork lives at $ROOT/knots-assembly and
# bitcoin/, assemble-deriv/, bitcoin-repro/, out/ are siblings. In this fork
# checkout the layout is collapsed: TMP is $ROOT itself (spec files live at
# the repo root), the driver submodule is $ROOT/assemble-knots, and bitcoin/
# + bitcoin-repro/ + out/ are created under $ROOT during the CI run.
TMP="${TMP:-$ROOT}"
BITCOIN="${BITCOIN:-$ROOT/bitcoin}"
ASSEMBLE="${ASSEMBLE:-$TMP/assemble-knots}"
REPRO="${REPRO:-$ROOT/bitcoin-repro}"
OUT="${OUT:-$ROOT/out}"
OVERRIDES="${OVERRIDES:-$ROOT/.ci/overrides}"

# The release we're reproducing. Defaults to the dated spec with the
# latest YYYYMMDD suffix present in $TMP — the assumption being that
# any `knots-<ver>.knots<YYYYMMDD>.spec` checked into the repo
# corresponds to a shipped release. Override with $KNOTS_TAG.
detect_latest_tag() {
  local latest
  latest=$(cd "$TMP" 2>/dev/null && \
    ls knots-*.knots[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].spec 2>/dev/null \
    | sort -V | tail -1)
  [ -n "$latest" ] || { echo "no dated spec files found in $TMP" >&2; return 1; }
  latest="${latest#knots-}"
  latest="${latest%.spec}"
  echo "v$latest"
}

RELEASE_TAG="${KNOTS_TAG:-$(detect_latest_tag)}"
[ -n "$RELEASE_TAG" ] || { echo "could not determine release tag" >&2; exit 1; }

# Release tag -> spec file mapping. Always pass the real Knots release tag
# (e.g. v29.3.knots20260210 or v0.13.1.knots20161027).
#
# Modern specs are named after the full dated release, so the direct lookup
# `knots-<tag>.spec` hits. Pre-26 specs are named only after the upstream
# base version (`knots-0.13.1.spec`) while the release is still tagged
# `v0.13.1.knots20161027`; for those, strip the trailing `.knotsYYYYMMDD`
# and fall back to the bare spec.
tag_to_spec() {
  local tag="${1#v}"
  local direct="$TMP/knots-${tag}.spec"
  if [ -f "$direct" ]; then
    echo "$direct"
    return
  fi
  echo "$TMP/knots-${tag%.knots[0-9]*}.spec"
}

SPEC="$(tag_to_spec "$RELEASE_TAG")"

# BASE_TAG comes from the spec's "checkout <ref>" line. Resolved lazily so
# scripts can run before the spec exists on disk.
resolve_base_tag() {
  [ -f "$SPEC" ] || die "spec not found for tag $RELEASE_TAG: $SPEC"
  awk '/^checkout / {print $2; exit}' "$SPEC"
}

# Per-release output/log names so a walk across many releases doesn't
# trample its own artifacts.
TAG_SHORT="${RELEASE_TAG#v}"
OUTSPEC="$OUT/${TAG_SHORT}.out.spec"
SPEC_IN="$OUT/${TAG_SHORT}.in.spec"
DRIVER_LOG="$OUT/${TAG_SHORT}.driver.log"
DRIFT_LOG="$OUT/drift-${RELEASE_TAG}.tsv"

# Per-release sed override, auto-loaded by the driver step if present.
OVERRIDE_SED="$OVERRIDES/${RELEASE_TAG}.sed"

# Metadata invariants for byte-exact SHA match.
COMMITTER_EMAIL="luke-jr+git@utopios.org"
REPRO_TZ="UTC"

say() { printf '\033[1;34m==>\033[0m %s\n' "$*" >&2; }
die() { printf '\033[1;31merror:\033[0m %s\n' "$*" >&2; exit 1; }
