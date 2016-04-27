# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:02:04 2016

@author: Kate
"""

import json
from dna_alignment_tool import DnaAligner
from distance_methods import DistanceMethods

path_dna = 'C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\dna_synthetic.json'

dna_data= {}
with open(path_dna) as data_file:    
    dna_data = json.load(data_file)

st1 = dna_data['data'][0]['b']
st2 = dna_data['data'][0]['c']
dna_tool = DnaAligner()
dna_a_mat = dna_tool.dna_align(st1,st2)
dna1, dna2 = dna_tool.backtrack(dna_a_mat, st1,st2)

merged_dna = dna_tool.merge(dna1, dna2)


dist_tool = DistanceMethods()
distance = dist_tool.levenshtein(merged_dna, dna_data['data'][0]['a'])

