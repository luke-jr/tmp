#!/usr/bin/perl
# Read a Knots spec file on stdin and emit, one per line,
# the set of git remotes + fetch refspecs needed to satisfy it.
#
# Output format: REMOTE_NAME<TAB>URL<TAB>REFSPEC
#
# Naming conventions (derived from luke-jr/tmp commit history and the driver):
#   - Bare branch name (no slash)                -> lives in luke-jr/bitcoin
#   - <user>/<path>                              -> <user>/bitcoin fork
#   - <user>-g/<path>                            -> <user>/gui fork
#   - origin-pull/<n>/head                       -> refs/pull/<n>/head of bitcoin/bitcoin
#   - origin-pull-g/<n>/head                     -> refs/pull/<n>/head of bitcoin-core/gui
#   - origin-pull-k/<n>/head                     -> refs/pull/<n>/head of bitcoinknots/bitcoin

use strict;
use warnings;

my %need;   # remote name -> { url => ..., refs => { refspec => 1 } }

sub add_need {
    my ($name, $url, $refspec) = @_;
    $need{$name}{url} = $url;
    $need{$name}{refs}{$refspec} = 1;
}

while (my $line = <>) {
    # Strip comments per driver semantics
    $line =~ s/\s*#.*//;
    next if $line =~ /^\s*$/;

    my ($prnum, $branch);

    # Match a (CHECK-LAST) trip-wire line first (more specific shape):
    #   \t(CHECK-LAST) last=<sha> <branch>
    # The driver will rev-parse <sha> against <branch>'s current tip; we
    # need <branch> fetched so that comparison can evaluate (and so a
    # genuine upstream-drift is the actual failure cause, not a fetch gap).
    if ($line =~ /^\s*\(CHECK-LAST\)\s+last=\S+\s+(\S+)/) {
        $branch = $1;
    }
    # Otherwise match an active merge line. Driver recognises three forms
    # (assemble-knots.pl lines 1027, 1071, 1085):
    #   NM\t<prnum>\s+<branch>...              — null merge
    #   TM\t<prnum>\s+<branch>...              — tree merge
    #   [am]*\t<prnum>\s+<branch>...           — regular merge (flags: a, m, am, or empty)
    elsif ($line =~ /^(?:NM|TM|[am]*)\t\s*([a-z]?\d+|\-|n\/a)\s+(\S+)/) {
        ($prnum, $branch) = ($1, $2);
        next if $branch =~ /^\(/;   # directive like (cherrypick=...)
    }
    else {
        next;
    }

    # Strip trailing ^ characters. The spec may reference a branch with a
    # caret suffix (git's "parent-of" syntax) to pin a specific ancestor of
    # the current tip; see `do_all_fetching` in the driver for the same
    # transformation. We just want to fetch the underlying branch.
    $branch =~ s/\^+$//;

    # Literal "-" in branch column means "use origin-pull/<prnum>/head".
    # Only applies to merge lines (CHECK-LAST has no <prnum>).
    # Prefix letter in prnum picks the remote:
    #   plain digits -> origin-pull    (bitcoin/bitcoin)
    #   g<digits>    -> origin-pull-g  (bitcoin-core/gui)
    #   k<digits>    -> origin-pull-k  (bitcoinknots/bitcoin)
    if (defined $prnum && $branch eq "-") {
        if ($prnum =~ /^(\d+)$/) {
            $branch = "origin-pull/$1/head";
        } elsif ($prnum =~ /^g(\d+)$/) {
            $branch = "origin-pull-g/$1/head";
        } elsif ($prnum =~ /^k(\d+)$/) {
            $branch = "origin-pull-k/$1/head";
        } else {
            next;  # n/a or -; no ref to resolve
        }
    }

    if ($branch =~ m{^origin-pull-g/(\d+)/head$}) {
        my $n = $1;
        add_need("origin-pull-g",
                 "https://github.com/bitcoin-core/gui.git",
                 "+refs/pull/$n/head:refs/remotes/origin-pull-g/$n/head");
    } elsif ($branch =~ m{^origin-pull-k/(\d+)/head$}) {
        my $n = $1;
        add_need("origin-pull-k",
                 "https://github.com/bitcoinknots/bitcoin.git",
                 "+refs/pull/$n/head:refs/remotes/origin-pull-k/$n/head");
    } elsif ($branch =~ m{^origin-pull/(\d+)/head$}) {
        my $n = $1;
        add_need("origin-pull",
                 "https://github.com/bitcoin/bitcoin.git",
                 "+refs/pull/$n/head:refs/remotes/origin-pull/$n/head");
    } elsif ($branch =~ m{^([A-Za-z0-9_.-]+)-g/(.+)$}) {
        my ($user, $path) = ($1, $2);
        add_need("$user-g",
                 "https://github.com/$user/gui.git",
                 "+refs/heads/$path:refs/remotes/$user-g/$path");
    } elsif ($branch =~ m{^([A-Za-z0-9_.-]+)/(.+)$}) {
        my ($user, $path) = ($1, $2);
        add_need($user,
                 "https://github.com/$user/bitcoin.git",
                 "+refs/heads/$path:refs/remotes/$user/$path");
    } else {
        # Bare branch name -> luke-jr/bitcoin heads
        add_need("luke-jr",
                 "https://github.com/luke-jr/bitcoin.git",
                 "+refs/heads/$branch:refs/heads/$branch");
    }
}

# Also: we always need the Core base tag from upstream and master for the
# poison check. Add an "upstream" remote that fetches tags + master.
add_need("upstream",
         "https://github.com/bitcoin/bitcoin.git",
         "+refs/heads/master:refs/remotes/upstream/master");

# Emit
for my $name (sort keys %need) {
    my $r = $need{$name};
    for my $refspec (sort keys %{$r->{refs}}) {
        print join("\t", $name, $r->{url}, $refspec), "\n";
    }
}
