# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:02:04 2016

@author: Kate
"""

import json
from dna_alignment_tool import DnaAligner
from distance_methods import DistanceMethods

path_dna = 'C:\\Users\\AMANSIE\\dna_works\\dna_synthetic.json'

dna_data= {}
with open(path_dna) as data_file:    
    dna_data = json.load(data_file)

#st1 = dna_data['data'][0]['b']
#st2 = dna_data['data'][0]['c']


'''
st1="a"
st2="b"
for i in range (4000):
    st1=st1+"a"
    
    
for i in range (4000):
    st2=st2+"a"
'''
    
dna_tool = DnaAligner()

fin_mat_D,fin_mat_I,fin_mat_M = dna_tool.dna_align(st1,st2)
dna1, dna2 = dna_tool.backtrack(fin_mat_D,fin_mat_I,fin_mat_M, st1,st2)
merged_dna = dna_tool.merge(dna1, dna2)
print(merged_dna)

'''
fin_mat_D,fin_mat_I,fin_mat_M = dna_tool.dna_align(st1,st2)
dna1, dna2 = dna_tool.backtrack( st1,st2)
merged_dna = dna_tool.merge(dna1, dna2)
print(merged_dna)

'''


dist_tool = DistanceMethods()
distance = dist_tool.levenshtein(merged_dna, dna_data['data'][0]['a'])

