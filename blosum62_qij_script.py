# -*- coding: utf-8 -*-
"""
Created on Sun May 08 23:55:55 2016

@author: Kate
"""

aa_index_dict = { 'A' : 0,'R' : 1,'N' : 2,'D' : 3,'C' : 4,'Q' : 5,'E' : 6,'G' : 7,'H' : 8,'I' : 9,'L' : 10,'K' : 11,'M' : 12,'F' : 13,'P' : 14,'S' : 15,'T' : 16,'W' : 17,'Y' : 18,'V' : 19}



#needed to create index
'''aa_str = 'A      R      N      D      C      Q      E      G      H      I      L      K      M      F      P      S      T      W      Y  V '

aa_arr = aa_str.split(' ')

ind_str = ''
count = 0
for idx,aa in enumerate(aa_arr):
    if aa.strip() <> '':
        ind_str = ind_str+ '\'' + aa + '\'' + ' : ' + str(count) + ',' 
        count = count+1'''
        
arr_aa = [[0 for col in range(20)] for row in range(20)]
        

lines = open('C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\blosum85.qij').readlines()


line_count = 0
for line in lines:
    if line[0] <> '#':
        probility_nums = line.split(' ')
        prob_count = 0
        for probs in probility_nums:
            if probs.strip() <> '':
                arr_aa[line_count][prob_count] = float(probs)
                arr_aa[prob_count][line_count] = float(probs)
                prob_count = prob_count +1
        line_count = line_count + 1
        
        
for idx, a_line in enumerate(arr_aa):
    sum_a = sum(a_line)
    for idx_1, aa in enumerate(a_line):
        arr_aa[idx][idx_1]= aa/sum_a
        
for i in range(20):
    print sum(arr_aa[:][i])