#!/usr/bin/perl -w
use strict;

# yexinhai, yexinhai@zju.edu.cn

my %hash_null;
my %hash_alter;

open my $null, "<", $ARGV[0] or die "can't open your null result !\n";
while (<$null>) {
	chomp();
	if (/^(Group\d+)\t(.*)\t$/) {
		$hash_null{$1} = $2;
	}
}
close $null;

open my $alter, "<", $ARGV[1] or die "can't open your alter result !\n";
while (<$alter>) {
	chomp();
	if (/^(Group\d+)\t(.*)$/) {
		$hash_alter{$1} = $2;
	}
}
close $alter;

print "id\tnull_np\tnull_lnL\talter_np\talter_lnL\n";

foreach my $key (sort keys %hash_null) {
	print $key."\t".$hash_null{$key}."\t".$hash_alter{$key}."\n";
}
