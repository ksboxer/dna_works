# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:46:24 2016

@author: AMANSIE
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:37:57 2016

@author: Kate
"""

def align_initialize(dna2, dna1):
    full_matrix = []
    for i in range(len(dna1)+1):
        full_matrix.append([0]*(len(dna2)+1))
        for j in range(len(dna2)+1):
            if i == 0:
                full_matrix[i][j] = j
            elif j == 0:
                full_matrix[i][j] = i
            else:
                full_matrix[i][j]=0
    return full_matrix

def dna_align(dna1, dna2):
    full_matrix = align_initialize(dna1, dna2)
    dna1 = " "+ dna1
    dna2 = " "+ dna2
    for i in range(1, len(full_matrix)):
        for j in range(1, len(full_matrix[0])):
            match_score = 1
            if dna1[j] == dna2[i]:
                match_score = 0
            full_matrix[i][j] = min([full_matrix[i-1][j-1]+ match_score, # diagonal
                        full_matrix[i-1][j] + 1,
                        full_matrix[i][j-1]+1])
    return full_matrix
    
import random

def find_min_direction(min_list):
    if len(min_list) == 1:
        return min_list[0]
    for m in min_list:
        if m[1] == 'diagonal':
            return 'diagonal'
    rand_num = random.random()
    if rand_num < .5:
        return 'up'
    else:
        return 'left'
        
    
def find_mins(m, l):
    fin_list = []
    for i in l:
        if i[0] == m:
            fin_list.append(i)
    return fin_list

def find_min_value(l):
    val_max  = float('inf')
    for element in l:
        if element[0] < val_max:
            val_max = element[0]
    return val_max
    
def backtrack(full_matrix,dna1, dna2):
    dna1 = " "+ dna1
    dna2 = " " + dna2
    dna_1_fin = ''
    dna_2_fin = ''
    i = len(full_matrix)-1
    j = len(full_matrix[0]) -1
    while(i > 0 or j > 0):
        possible_mins= []
        if i >0 :
            possible_mins.append([full_matrix[i-1][j], "up"])
        if j > 0:
            possible_mins.append([full_matrix[i][j-1], "left"])
        if i > 0 and j > 0:
            possible_mins.append([full_matrix[i-1][j-1], "diagonal"])
        
        direction = (find_min_direction(find_mins(find_min_value(possible_mins), possible_mins)))[1]
        print  (direction )       
        if direction == 'diagonal':
            print ('diagonal_test')
            dna_1_fin = dna1[j] + dna_1_fin
            dna_2_fin = dna2[i] + dna_2_fin
            i = i -1
            j = j -1
        elif direction == 'up':
            print ('up_test')
            dna_1_fin = '-' + dna_1_fin
            dna_2_fin = dna2[i] + dna_2_fin
            i = i -1
        else:
            print ('left_test')
            dna_1_fin = dna1[j] + dna_1_fin
            dna_2_fin = '-' + dna_2_fin 
            j = j-1
    return dna_1_fin, dna_2_fin
            
    
#estimated_a=print(estimated_a)
#seq=difflib.SequenceMatcher(estimated_a,actual_a)
#print (seq.ratio())

#
import pprint
#pprint.pprint(pprint_mat)
                    
                
            

#s1 is horizontal string
#s2 is vertical string
def merge (s1,s2):
    s3=''
    for i in range(len(s1)):
        if (s1[i]=='-' and s2[i]!='-'):
            s3=s3+s2[i]
        elif (s2[i]=='-' and s1[i]!='-'):
            s3=s3+s1[i]
        else:
            # randomly pick between s1 and s2
            rand_num = random.random()
            if rand_num < .5:
                s3=s3+s1[i]
            else:
                s3=s3+s2[i]
    return (s3)
    
results = []

for row in value_dict:
    full_mat = dna_align(row['b'], row['c'])
    
    
    



        