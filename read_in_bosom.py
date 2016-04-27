# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:17:52 2016

@author: Kate
"""


import glob

class BlosumMat:
        
        path = 'blosum_mat\\*.qij'
        def read_in(self):
            file_names = glob.glob(self.path)
            full_blosom_dict = {}
            for file_name in file_names:
                text = open(file_name).read()
                lines = text.split('\n')
                index = True
                index_aa = []
                aa_dict  = {}
                idx_full = 0
                for line in lines:
                    if '#' not in line:
                        if index:
                            index = False
                            aa = line.split(' ')
                            for acid in aa:
                                if acid.strip() <> '':
                                    index_aa.append(acid)
                        else:
                            probs = line.split(' ')
                            prob_clean = []
                            for prob in probs:
                                if prob.strip() <> '':
                                    #print '|'+prob+'|'
                                    prob_clean.append(float(prob.strip()))
                            for idx, prob in enumerate(prob_clean):
                                aa_dict[index_aa[idx_full]+','+index_aa[idx]] = prob
                                aa_dict[index_aa[idx]+','+index_aa[idx_full]] = prob
                            idx_full = idx_full +1
                full_blosom_dict[file_name[11:len(file_name)-4]] = aa_dict
            return full_blosom_dict
                            
                        
                