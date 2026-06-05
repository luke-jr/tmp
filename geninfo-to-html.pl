#!/usr/bin/perl
# kate: space-indent off;

# Copyright 2016-2021 Luke Dashjr
# Note this is presently NOT free software. See LICENSE for details.
# Use at your own risk. No warranty.

use sort 'stable';
use strict;
use warnings;
use forks;
use utf8;

BEGIN { binmode STDOUT, ":utf8" }

use File::Basename;
use HTML::Entities;
use HTTP::Request;
use JSON::PP;
use LWP;

my $cachedir = dirname(__FILE__) . "/geninfo-to-html-cache/";

warn "Remember to wipe cache if PRs might have been merged!\n";

my @github_auth;
{
	open my $f, "<&3" or die;
	@github_auth = <$f>;
	close $f;
	chomp for @github_auth;
}

sub makegitcmd {
	("git", "--no-pager", @_)
}

sub syscapture {
	my @cmd = @_;
	#print "@cmd\n";
	open(my $outio, "-|", @cmd);
	my $out;
	{
		local $/;
		$out = <$outio>;
	}
	close $outio;
	my $ec = $?;
	($ec, $out)
}

sub gitcapture {
	my @cmd = makegitcmd(@_);
	my ($ec, $out) = syscapture(@cmd);
	chomp $out;
	die "@cmd failed (exit code $ec; output $out)" if $ec;
	$out
}

sub wc_l {
	return 0 unless length $_[0];
	1 + ($_[0] =~ tr/\n//)
}

sub github_fetch_prinfo {
	my ($prspec) = @_;
	$prspec =~ m[([gk]?)(.*)] or die;
	my ($is_gui, $prnum) = @{^CAPTURE};
	
	my $j;
	if (-e "$cachedir/$prspec") {
		open my $f, "<$cachedir/$prspec";
		my $content;
		{
			local $/ = undef;
			$content = <$f>;
		}
		close $f;
		$j = decode_json $content;
	} else {
		my $repo;
		if ("g" eq $is_gui) {
			$repo = "bitcoin-core/gui";
		} elsif ("k" eq $is_gui) {
			$repo = "bitcoinknots/bitcoin";
		} else {
			$repo = "bitcoin/bitcoin";
		}
		my $req = HTTP::Request->new(GET => "https://api.github.com/repos/$repo/pulls/$prnum");
		$req->authorization_basic(@github_auth);
		my $content = LWP::UserAgent->new->request($req)->content;
		$j = decode_json $content;
		die $content unless $j->{title};

		open my $f, ">$cachedir/$prspec";
		print $f $content;
		close $f;
	}
	$j
}

my @to_process;

my $base;
{
	my $line = <>;
	$line =~ m/^checkout (.*)$/ or die;
	$base = $1;
}

sub preptitle {
	my ($title) = @_;
	$title =~ s/^\[?WIP\]?\:?//i;
	$title =~ s/^\s+//;
	$title =~ s/\.?\s*$//;
	encode_entities($title, "<>&")
}

my %sortorder = (
	"\@" => 0,
	"PR" => 1,
	"BM" => 2,
	"LA" => 2,
);

sub prep_html {
	@to_process = sort {
		my ($aa, $bb) = ($a, $b);
		$aa =~ s/^(\S+) // or die;
		my $ka = $1;
		$bb =~ s/^(\S+) // or die;
		my $kb = $1;
		my $sod = $sortorder{$ka} <=> $sortorder{$kb};
		return $sod if $sod;
		if ($ka eq 'PR') {
			for ($aa, $bb) {
				$_ += 1000000 if s/^g//;
				$_ += 2000000 if s/^k//;
			}
			return $aa <=> $bb
		}
		0  # Stable sort
	} @to_process;
	my @threads;
	my $i;
	while ($_ = shift @to_process) {
		my $line = $_;
		push @threads, async {
			if (s/^PR ([gk]?.*)//) {
				my ($prspec) = @{^CAPTURE};
				my $j;
				$j = github_fetch_prinfo($prspec);
				$_ = "<a";
				$_ .= " class=\"merged\"" if $j->{merged};
				my $subject = preptitle($j->{title});
				my $url = $j->{"html_url"} // '';
				$url = '' unless $url =~ m{^https?://}i;
				$_ .= " href=\"" . encode_entities($url, '<>&"') . "\">" . $subject . "</a>";
			} elsif (m/^BM (\S+) (\S+)$/ or m/^LA ()(\S+)$/) {
				my ($branch, $lastmerge) = @{^CAPTURE};
				my $gitlog = gitcapture("log", "--no-decorate", "--no-merges", "--pretty=%H %s", "$lastmerge^..$lastmerge");
				if (wc_l($gitlog) == 1) {
					my ($commithash, $subject) = split /\s/, $gitlog, 2;
					$subject = preptitle($subject);
					$_ = "<a href=\"https://github.com/bitcoinknots/bitcoin/commit/$commithash\">$subject</a>";
				} else {
					my $mergecommit = gitcapture("rev-parse", $lastmerge);
					$_ = "<a href=\"https://github.com/bitcoinknots/bitcoin/commit/$mergecommit\">TODO: $branch</a>";
				}
			}
			$_ = "<li>$_</li>" if m[^<];
			"$_\n"
		};
		if ($line =~ /^PR /) {
			if (not $i++) {  # First PR job runs synchronously to init LWP
				while (@threads) {
					my $thread = shift @threads;
					print $thread->join;
				}
			}
		}
		while (@threads > 4) {
			my $thread = shift @threads;
			print $thread->join;
		}
	}
	for my $thread (@threads) {
		print $thread->join;
	}
}

while (my $line = <>) {
	chomp $line;
	if ($line =~ m[^\@]) {
		prep_html;
	}
	push @to_process, $line;
}
prep_html;

