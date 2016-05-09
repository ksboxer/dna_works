# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:40:02 2016

@author: Kate
"""

import json
import pprint
#from dna_alignment_tool import DnaAligner

collected_genes_path = "C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\clustered_processed_v2.txt"


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

species_idx = {'Canis_familiaris': 0, 'Gorilla_gorilla': 1, 'Loxodonta_africana': 2 , 'Mus_musculus': 3, 'Oreochromis_niloticus': 4, 'Ovis_aries' : 5 }

path = 'C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\cluster_dict.json'

dna_a = DnaAligner()

with open(path) as data_file:    
    data = json.load(data_file)

#pprint(data)

seq_path = "C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\collected_amino_acids_seq\\"


processed_data = 'C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\processed_cluster_data_v2\\'

pp = pprint.PrettyPrinter()

count = 0

processed_list = read_in_collected_genes()

import random
keys = random.sample(range(0, len(data.keys())), 500)

for key in keys:
   p = str(key)
   dis_mat = [[float('NaN') for x in range(6)] for y in range(6)]
   #print dis_mat
   if len(data[p].keys()) > 1 and p not in processed_list and p <> '2688':
       print p 
       count = count +1
       data_dict = {}
       for idx, spec in enumerate(data[p].keys()):
           seq = {}
           #print data[p]
           data_dict[species_idx[spec]] = data[p][spec][0]
           if True:
               with open(seq_path + spec+'\\'+data[p][spec][0]+'.json') as data_file:    
                   seq_1 = json.load(data_file)
                   #print seq_1['seq']
               for idx_col in range(idx, len(data[p].keys())):
                   #print seq_path + data[p].keys()[idx_col]+'\\'+data[p][data[p].keys()[idx_col]][0]+'.json'
                   with open(seq_path + data[p].keys()[idx_col]+'\\'+data[p][data[p].keys()[idx_col]][0]+'.json') as data_file:    
                       seq_2 = json.load(data_file)
                       #print seq_2['seq']
                       fin_dna, score, fin1, fin2 = dna_a.run(seq_1['seq'], seq_2['seq'])
                       dis_mat[species_idx[data[p].keys()[idx_col]]][species_idx[spec]] = (score, fin_dna)
                       dis_mat[species_idx[spec]][species_idx[data[p].keys()[idx_col]]] =  (score, fin_dna)
       print(dis_mat)
       data_dict['dist_mat'] = dis_mat
       with open(processed_data +'_' + p + '.json', 'w') as fp:
           json.dump(data_dict, fp)
           write_collected_genes([p])
           print 'done w '+ p
      

                     
        