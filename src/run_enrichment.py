from collections import defaultdict,OrderedDict
import numpy as np
import sys
from scipy.stats import fisher_exact
import os
from gsea import readgenesets, gsea
file_name = sys.argv[1]
background_file_name = sys.argv[2]
geneset_name = sys.argv[3]
save_name = sys.argv[4]

""" Read test genes"""
fh = open(file_name,'r')
lines = fh.readlines()
fh.close()
test_genes = []
for line in lines:
	test_genes.append(line.strip('\n'))


""" Read background genes"""
fh = open(background_file_name,'r')
lines = fh.readlines()
fh.close()
all_genes = []
for line in lines:
	all_genes.append(line.strip('\n'))

		
all_genes = set(all_hormones)
test_genes = set(test_genes)



test_out = gsea(hormone_test_gene_list, all_genes, geneset_name)

""" Save result to save_name"""
fh = open(save_name,'w')
print >>f,"TestFile:", file_name, "\nBackgroundFile:", background_file_name, "\nGeneset:", geneset_name, "SaveFile:", save_name
print >>f,"test_inset\ttest_notinset\tbackground_inset\tbackground_notinset\toddsratio\tpvalue"
for i in test_out:
	print >>f, i,'\t','\t'.join(str(j) for j in test_out[i])
fh.close()
