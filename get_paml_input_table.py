#!/usr/bin/python

# yexinhai, yexinhai@zju.edu.cn

from sys import argv

with open(argv[1]) as groups:
	list1 = groups.readlines()

groups_dict = {}

for line in list1:
	line = line.strip()
	a = line.split(' ')
	group_id = a[0]
	del a[0]
	groups_dict[group_id] = a

#for key in groups_dict.keys():
#	print (str(key))

with open(argv[2]) as inputid:
	list2 = inputid.readlines()

c = ['Harm','Sfru','Slit','Tni']

for line in list2:
	line = line.strip()
	b = line.split('\t')
	Id = b[0]
	gene_list = []
	for i in groups_dict[Id]:
		species_name = i.split('|')[0]
		if species_name in c:
			gene_list.append(i)
	d = '\t'.join(gene_list)
	print (str(b[0]) + '\t' + str(d))
