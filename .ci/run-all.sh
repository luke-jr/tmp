#!/usr/bin/env bash
# End-to-end entrypoint for the Knots release reproduction pipeline.
# Drives the five .ci/ phases in order. Both the GitHub Actions
# workflow and a local reproducer run this same script.
#
# Usage:
#   ./.ci/run-all.sh                          # default release
#   ./.ci/run-all.sh v29.2.knots20251110      # specific release tag
#
# lib.sh derives the spec filename from the tag via tag_to_spec(),
# so the tag alone is enough.

set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

if [ "$#" -gt 0 ]; then
  export KNOTS_TAG="$1"
fi

"$HERE/pin-submodule.sh"
"$HERE/bootstrap.sh"
"$HERE/synthesize-refs.sh"
"$HERE/run-driver.sh"
"$HERE/verify.sh"
