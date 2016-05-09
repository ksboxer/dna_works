# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:43:36 2016

@author: Kate
"""

import read_in_bosom

class Alignment:
    
    def find_substitution_matrix(self, rna_1, rna_2):
        min_len = min([len(rna_1), len(rna_2)])
        similarity_count = 0
        for i in range(0,min_len):
            if rna_1[i] == rna_2[i]:
                similarity_count = similarity_count +1
        return float(similarity_count)/float((max([len(rna_1), len(rna_2)])))
        
    def get_blosum_matrix(self,ratio):
        b = BlosumMat()
        mats = b.read_in()
        print mats.keys()
        if ratio <= .3:
            return mats['blosum30']
        elif ratio <= .35:
            return mats['blosum35']
        elif ratio <= .40:
            return mats['blosum40']
        elif ratio <= .45:
            return mats['blosum45']
        elif ratio <= .50:
            return mats['blosum50']
        elif ratio <= .55:
            return mats['blosum55']
        elif ratio <= .60:
            return mats['blosum60']
        elif ratio <= .62:
            return mats['blosum62']
        elif ratio <= .65:
            return mats['blosum65']
        elif ratio <= .70:
            return mats['blosum70']
        elif ratio <= .75:
            return mats['blosum75']
        elif ratio <= .8:
            return mats['blosum80']
        elif ratio <= .85:
            return mats['blosum85']
        elif ratio <= .9:
            return mats['blosum95']
        elif ratio <= .95:
            return mats['blosum95']
        else:
            return mats['blosum100']
            
    def run(self,rna_1, rna_2):
        ratio = self.find_substitution_matrix(rna_1,rna_2)
        blosum = self.get_blosum_matrix(.62)
        return blosum