# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:50:10 2016

@author: Kate
"""

import urllib2
import time
import json

collected_genes_list = []
collected_genes_path = "C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\collected_amino_acids_seq\\collected_genes.txt"


base_url = 'http://rest.ensembl.org/sequence/id/'
end_url = '?content-type=application/json;type=protein'
def read_in_collected_genes():
    f = open(collected_genes_path, 'r')
    collected_genes_list = f.readlines()
    for idx,c in enumerate(collected_genes_list):
        collected_genes_list[idx] = c.replace('\n','')
    return collected_genes_list

def write_collected_genes(lst):
    f = open(collected_genes_path, 'a')
    for item in lst:
        f.write("%s\n" % item)

def get_url(url):
    response = urllib2.urlopen(url)  
    return response.read()

#example url
#http://rest.ensembl.org/sequence/id/ENSONIG00000012345?content-type=application/json;type=protein

path = 'C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\cluster-information.txt'

f = open(path, 'r')
x = f.read()
lines = x.split('\n')

gene_animal_lookup = {}
gene_animal_dictionary = {}
gene_lookup_table = {}
cluster_animal = {}

for idx,cluster in enumerate(lines):
    genes = cluster.split('\t')
    cluster_animal[idx] = {}
    for animal_info in genes:
        print animal_info
        arr_info = animal_info.split("|")
        gene_animal_lookup[arr_info[1]] = arr_info[0]
        if arr_info[0] not in gene_animal_dictionary:
            gene_animal_dictionary[arr_info[0]] = []
        gene_animal_dictionary[arr_info[0]].append(arr_info[1])
        if arr_info[1] not in gene_lookup_table:
            gene_lookup_table[arr_info[1]] = []
        gene_lookup_table[arr_info[1]].append(idx)
        if arr_info[0] not in cluster_animal[idx]:
            print animal_info[0]
            cluster_animal[idx][arr_info[0]] = []
        cluster_animal[idx][arr_info[0]].append(arr_info[1])
        

for key in gene_animal_dictionary.keys():
    print len(gene_animal_dictionary[key])
    
    
for gene in gene_lookup_table.keys():
    if len(gene_lookup_table[gene]) != 1:
        print gene

count = 0
cluster_same_species_count = 0
for cluster in cluster_animal.keys():
    if len(cluster_animal[cluster]) > 1 :
        print cluster
        count = count +1
        multi = False
        for s_key in cluster_animal[cluster].keys():
            if len(cluster_animal[cluster][s_key]) > 1:
                multi = True
        if multi:
            cluster_same_species_count = cluster_same_species_count + 1

'''list_collected = read_in_collected_genes()

full_p = 'C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\collected_amino_acids_seq\\'

for idx, id_ in enumerate(gene_animal_lookup.keys()):
    org_id = id_
    if org_id not in list_collected:
        id_ = id_.replace('\n', '')
        id_ = id_.strip()
        try:
        #if True:
            json_data = get_url(base_url + id_ + end_url)
            #print json_data
            print str(idx) +   '\\' + str(len(gene_animal_lookup.keys()))
            d = json.loads(json_data)
            print d
            print gene_animal_lookup[org_id]
            time.sleep(.15)
            with open(full_p + gene_animal_lookup[org_id]+ '\\' + id_ + '.json', 'w') as fp:
                print "trying to dump"                
                json.dump(d, fp)
                print "dumped"
            write_collected_genes([org_id])
        except:
            print 'exception: '+ id_ '''
len_dict = {1:0, 2:0, 3:0, 4:0, 5:0,6:0}
for key in cluster_animal.keys():
    len_dict[len(cluster_animal[key])] = len_dict[len(cluster_animal[key])] +1
    
lengths = []
freq = []
for i in len_dict:
    lengths.append(i)
    freq.append(len_dict[i])

    