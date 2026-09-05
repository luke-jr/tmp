# Bitcoin Knots assembly spec

> **Note for reviewers:** while this PR is under review, the CI runs
> described below live on
> [`chrisguida/knots-assembly`][cguida-fork]. After merge they will
> appear on this repository's Actions tab.

[cguida-fork]: https://github.com/chrisguida/knots-assembly/actions/workflows/reproduce.yml

This repository holds the **assembly specs** for every published
Bitcoin Knots release. A Knots release isn't a separate codebase;
it's a derivation of a specific Bitcoin Core release tag, layered
with a curated set of additional pull requests, branches, and
cherry-picks. The specs in this repo are the recipes that describe
how to perform that derivation deterministically.

Together with the [`assemble-knots`][assemble-knots] driver (a
submodule at `assemble-knots/`) and the recorded conflict resolutions
in `assemble-knots-resolutions/`, an assembled tree can be derived
from these specs plus public upstream sources. The CI added in this
branch verifies that derivation is **byte-exact** against the
published release tag for the most recent dated release.

[assemble-knots]: https://github.com/bitcoinknots/assemble-knots

---

## The spec model

Each spec file is a plain-text recipe. The first non-comment line is
a `checkout` of a Bitcoin Core release tag; subsequent lines are
entries that describe one operation on top of the assembly tip.

```text
timestamp 2026-02-10 02:26:19
checkout v29.3
@29.x-syslibs
# SYSLIBS:
    2241  sys_leveldb           a083281a33d    last=bd2be933f26 sys_leveldb-30
    n/a   rm_minisketch-29+syslibs    53bf7e9206c    last=0fd60441475 rm_minisketch-30+syslibs
    (cherrypick=488640fe20b)            2e044dabbf
    (CHECK-LAST) last=ea0f7c54aac suggest_check_chain-30
```

Recognised entry shapes:

| Shape | Meaning |
|-------|---------|
| `<prnum>  <branch>  [last=<sha>]` | Merge `<branch>` (with optional release-time tip pin) |
| `NM\t<prnum>  <branch>` | Null merge (record without altering tree) |
| `TM\t<prnum>  <branch>` | Tree merge (adopt a tree without recording history) |
| `(cherrypick=<sha>) <lastapply>` | Cherry-pick a specific commit |
| `(CHECK-LAST) last=<sha> <branch>` | Tripwire: fail if `<branch>` no longer points at `<sha>` |
| `@<name>` | Splice in a named sub-spec |

Branch names follow naming conventions interpreted by the driver and
by `extract-remotes.pl`:

| Pattern | Source |
|---------|--------|
| `<bare-name>` | `luke-jr/bitcoin` |
| `<user>/<path>` | `<user>/bitcoin` |
| `<user>-g/<path>` | `<user>/gui` |
| `origin-pull/<n>/head` | `bitcoin/bitcoin` PR `#<n>` |
| `origin-pull-g/<n>/head` | `bitcoin-core/gui` PR `#<n>` |
| `origin-pull-k/<n>/head` | `bitcoinknots/bitcoin` PR `#<n>` |

Spec filenames follow `knots-<version>.spec` for older releases (the
file is reused across dated re-releases sharing a base) and
`knots-<version>.knots<YYYYMMDD>.spec` for modern dated releases.

## Assembling a release

The driver reads a spec, plays it forward against the checked-out
Bitcoin Core base, and produces a worktree at the assembled tip:

```sh
git clone --recurse-submodules https://github.com/<this-repo>.git
cd <this-repo>
# Driver source lives in the assemble-knots/ submodule; consult its
# README for command-line invocation.
```

The byte-exactness of an assembled HEAD vs. a published release tag
depends on a handful of environment invariants: UTC timezone, the
committer email the Knots maintainers use for assembly merges, and
`merge.conflictStyle=diff3` (the recorded conflict resolutions are
keyed by patch-ids that include the diff3 common-ancestor marker).
See `.ci/run-driver.sh` for the full set.

## Release reproduction CI *(new in this branch)*

This branch adds a GitHub Actions workflow
(`.github/workflows/reproduce.yml`) that reproduces the most recent
published Knots release **byte-exact** from public sources only, on
every push and on a nightly cron. The workflow targets the newest
dated release (currently **`v29.3.knots20260508`**) and completes in
a couple of minutes.

**What a green run proves:** the published spec for the targeted
dated release, run through the historically pinned assembly driver,
still produces a HEAD whose SHA is identical to the release tag's
SHA, starting from nothing but public upstream sources. A red run
means either a public artifact has drifted in a way that breaks
reproduction, or the reproduction harness has a regression; both
worth knowing about.

### See it passing

The [Actions tab][cguida-fork] (currently on the review fork) renders
the latest run's result table at the top of its summary page
(expected SHA, reproduced SHA, ref-synthesis stats), no log diving
needed.

### Reproduce locally

```sh
git clone --recurse-submodules \
  https://github.com/chrisguida/knots-assembly.git    # or this repo's URL after merge
cd knots-assembly
./.ci/run-all.sh
```

`--recurse-submodules` is optional; `run-all.sh` initialises the
`assemble-knots/` submodule itself if needed. The first run clones
`bitcoinknots/bitcoin` (~1.5 GB) and fetches every remote the spec
references; subsequent runs reuse the existing clone.

### Reproduce a different release

Pass any release tag as a positional argument to `run-all.sh`:

```sh
./.ci/run-all.sh v29.2.knots20251110
```

In CI, the same override is available on the workflow's "Run
workflow" dispatch dialog; leave the input blank for the
auto-detected default.

Releases known to reproduce byte-exact with this pipeline, every
final dated 29.x Knots release published to date (release candidates
aside):

- `v29.3.knots20260508`
- `v29.3.knots20260507`
- `v29.3.knots20260210`
- `v29.2.knots20251110`
- `v29.2.knots20251010`
- `v29.1.knots20250903`

Earlier releases (pre-29) reproduce too but need an era-appropriate
`git` binary (the driver keys recorded conflict resolutions by
`git patch-id`, and the diff3 conflict-marker format changed in git
2.24); that workflow lives outside this repo for now.

### System requirements

The `.ci/` pipeline (and the driver itself) needs:

- Linux or macOS with `bash`.
- `git` 2.24 or newer for the releases listed above.
- `perl` 5.x with the standard library (no extra CPAN modules
  required for the reproduction pipeline; `geninfo-to-html.pl` and
  `check-pr-updates.pl` have their own dependencies).
- Standard POSIX userspace: `awk`, `sed`, `head`, `tail`, `wc`,
  `grep`, `tr`, `paste`, `diff`, `md5sum`, `sort`, `timeout`, `yes`.
- ~3 GB free disk for the bitcoin clone and the driver worktree.
- Outbound network access to `github.com` (the spec references
  `bitcoin/bitcoin`, `bitcoinknots/bitcoin`, `luke-jr/bitcoin`,
  `bitcoin-core/gui`, plus several developer forks).

The CI workflow uses `ubuntu-latest` runners with no extra
provisioning; the runner image ships every dependency listed.

### CI script layout

| Path | Purpose |
|------|---------|
| `.github/workflows/reproduce.yml` | GH Actions orchestration (thin) |
| `.ci/run-all.sh` | Local + CI entrypoint |
| `.ci/lib.sh` | Shared paths and helpers |
| `.ci/pin-submodule.sh` | Pin `assemble-knots/` to spec-time SHA |
| `.ci/bootstrap.sh` | Clone bitcoin, configure remotes, fetch |
| `.ci/synthesize-refs.sh` | Overwrite branch refs with release-time SHAs |
| `.ci/run-driver.sh` | Run `assemble-knots.pl` against the spec |
| `.ci/verify.sh` | Four-level commit/tree comparison vs release tag |
| `.ci/overrides/` | Per-release manual `sed` overrides (currently empty) |
| `extract-remotes.pl` | Translates a spec into remote/refspec config |

New dated releases are picked up automatically as soon as their
spec is committed; no workflow edits required. Reproduction of
pre-`v29` releases is handled offline and is out of CI scope for now.

## Repository layout

| Path | Purpose |
|------|---------|
| `knots-<version>.spec`, `knots-<version>.knots<date>.spec` | Per-release assembly specs |
| `assemble-knots/` | Driver submodule ([`bitcoinknots/assemble-knots`][assemble-knots]) |
| `assemble-knots-resolutions/` | Recorded conflict resolutions (`.diff` files keyed by `git patch-id`) |
| `check-pr-updates.pl`, `check-pr-updates.sh` | Detect upstream PR drift since a recorded timestamp |
| `extract-remotes.pl` | Spec → `(remote, url, refspec)` triples (used by CI) |
| `geninfo-to-html.pl` | Render assembly-info into HTML |
| `.ci/`, `.github/workflows/` | Reproduction CI (this branch) |
