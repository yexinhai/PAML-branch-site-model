#!/bin/bash

input_table_list=./input_table.list

for i in `cat $input_table_list`
do
	mkdir $i
	cd $i
	ln -s ../positive_selection_codeml.pl .
	ln -s ../input_table/$i .
	bsub -n 1 -oo paml.log -eo paml perl positive_selection_codeml.pl ../all_pep.fasta ../all_cds.fasta $i
	cd ..
done