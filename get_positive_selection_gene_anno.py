#!/usr/bin/python

# yexinhai, yexinhai@zju.edu.cn

from sys import argv

with open(argv[1]) as input_table:
	list1 = input_table.readlines()

groups_dict = {}

for line in list1:
	line = line.strip()
	tmp = line.split('\t')
	group_id = tmp[0].split(':')[0]
	for i in tmp:
		if 'Sfru' in i:
			gene_id = i.split('|')[-1]
	groups_dict[group_id] = gene_id

import re
reg_id = re.compile("^>(\S+)")
reg_anno = re.compile("annotation:\s(.*)\sOS=")

with open(argv[2]) as genome_ogs_pep:
	list2 = genome_ogs_pep.readlines()

gene2anno_dict = {}

for line in list2:
	if line[0] == '>':
		if reg_anno.search(line):
			anno = reg_anno.search(line).group(1)
		else:
			anno = "Putative uncharacterized protein"
		geneid = reg_id.search(line).group(1)
		gene2anno_dict[geneid] = anno

with open(argv[3]) as PSG:
	list3 = PSG.readlines()

print ('groupid\tgeneid\tannotation\tp-value\tfdr')

for line in list3:
	line = line.strip()
	if line.split('\t')[0] != "id":
		groupid = line.split('\t')[0]
		p = line.split('\t')[-2]
		fdr = line.split('\t')[-1]
		print (str(groupid) + '\t' + str(groups_dict[groupid]) + '\t' + str(gene2anno_dict[groups_dict[groupid]]) + '\t' + str(p) + '\t' + str(fdr))
