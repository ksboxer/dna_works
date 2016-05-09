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

import random
import rna_aligner

class DnaAligner:
    

    def align_initialize(self,dna2, dna1):
        full_matrix = []
        for i in range(len(dna1)+1):
            full_matrix.append([0]*(len(dna2)+1))
            for j in range(len(dna2)+1):
                if i == 0:
                    full_matrix[i][j] = ((j-1) * -1 ) - 10
                elif j == 0:
                    full_matrix[i][j] = ((i-1) * -1) - 10
                else:
                    full_matrix[i][j]=0
        full_matrix[0][0] = 0
        return full_matrix


    def align_initialize_local(self,dna2, dna1):
        full_matrix = []
        for i in range(len(dna1)+1):
            full_matrix.append([0]*(len(dna2)+1))
            for j in range(len(dna2)+1):
                if i == 0:
                    full_matrix[i][j] = 0
                elif j == 0:
                    full_matrix[i][j] = 0
                else:
                    full_matrix[i][j]=0
        return full_matrix
        
#global alignment
    def dna_align(self, dna1, dna2, blosum):
        full_matrix_D = self.align_initialize(dna1, dna2)
        full_matrix_I = self.align_initialize(dna1, dna2)
        full_matrix_M = self.align_initialize(dna1, dna2)
        
        
        dna1 = " "+ dna1
        dna2 = " "+ dna2
        
        gap_open=-10;
        gap_extend=-1;
               
        for i in range(1, len(full_matrix_D)):
            for j in range(1, len(full_matrix_D[0])):
                
               
                match_score = blosum[dna1[j]+','+dna2[i]] 
        
                #if dna1[j] == dna2[i]:
                #    match_score = 0
                    
                full_matrix_D[i][j] = max([full_matrix_D[i][j-1]+ gap_extend , # 
                           # full_matrix_I[i][j-1] + gap_open,
                            full_matrix_M[i][j-1]+gap_open])
                            
                full_matrix_I[i][j] = max([full_matrix_D[i-1][j]+ gap_open, full_matrix_I[i-1][j] + gap_extend])
                            #full_matrix_M[i-1][j]+gap_open])
                            
                full_matrix_M[i][j] = max([full_matrix_D[i-1][j-1]+ match_score, # diagonal
                            full_matrix_I[i-1][j-1] + match_score,
                            full_matrix_M[i-1][j-1]+match_score])
        return (full_matrix_D, full_matrix_I,full_matrix_M)

        
         

    def find_min_direction(self,min_list):
        if len(min_list) == 1:
            return min_list[0]
        rand_i = random.randint(0,(len(min_list))-1)
        return min_list[rand_i]
        
    
    def find_mins(self,m, l):
        fin_list = []
        for i in l:
            if i[0] == m:
                fin_list.append(i)
        return fin_list



    def find_min_value(self,l):
        val_max  = -1* float('inf')
        for element in l:
            if element[0] > val_max:
                val_max = element[0]
        return val_max



    def merge (self,s1,s2):
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
        
        
        
        
    def backtrack(self,full_matrix_D,full_matrix_I,full_matrix_M ,dna1, dna2):
        dna1 = " "+ dna1
        dna2 = " " + dna2
        dna_1_fin = ''
        dna_2_fin = ''
        i = len(full_matrix_D)-1
        j = len(full_matrix_D[0]) -1
        while(i > 0 or j > 0):
            possible_mins= []
            if i >0 :
                possible_mins.append([max(full_matrix_D[i-1][j],full_matrix_I[i-1][j],full_matrix_M[i-1][j])
                                                  ,"up"])
            if j > 0:
                possible_mins.append([max(full_matrix_D[i][j-1],full_matrix_I[i][j-1],full_matrix_M[i][j-1])
                                                , "left"])
            if i > 0 and j > 0:
                possible_mins.append([max (full_matrix_D[i-1][j-1],full_matrix_I[i-1][j-1],full_matrix_M[i-1][j-1])
                                              ,"diagonal"])
            
            direction = (self.find_min_direction(self.find_mins(self.find_min_value(possible_mins), possible_mins)))[1]
            #print  (direction )       
            if direction == 'diagonal':
                #print ('diagonal_test')
                dna_1_fin = dna1[j] + dna_1_fin
                dna_2_fin = dna2[i] + dna_2_fin
                i = i -1
                j = j -1
            elif direction == 'up':
               # print ('up_test')
                dna_1_fin = '-' + dna_1_fin
                dna_2_fin = dna2[i] + dna_2_fin
                i = i -1
            else:
               # print ('left_test')
                dna_1_fin = dna1[j] + dna_1_fin
                dna_2_fin = '-' + dna_2_fin 
                j = j-1
        return dna_1_fin, dna_2_fin
    
    def find_score(self, arr_d, arr_i, arr_m):
        return max([arr_d[len(arr_d)-1][len(arr_d[0])-1],arr_i[len(arr_d)-1][len(arr_d[0])-1], arr_m[len(arr_d)-1][len(arr_d[0])-1]]) 
        
    def find_score_dna(self,dna, dna1):
        count_mis_match = 0
        for idx,i in enumerate(dna):
            if i <> '-' and dna1[idx] <> '-' and i <> dna1[idx]:
                count_mis_match = count_mis_match +1
        return float(count_mis_match)/ len(dna)
                
    def run(self,dna1, dna2):
        rna_a = Alignment()
        blosum = rna_a.run(dna1, dna2)
        total_len = len(dna1) + len(dna2)
        (full_matrix_D, full_matrix_I,full_matrix_M) = self.dna_align(dna1, dna2, blosum)
        #print (full_matrix_D, full_matrix_I,full_matrix_M)
        dna_fin1, dna_fin2 = self.backtrack(full_matrix_D,full_matrix_I,full_matrix_M, dna1,dna2)
        fin_dna = self.merge(dna_fin1,dna_fin2)
        return fin_dna, self.find_score_dna(dna_fin1, dna_fin2), dna_fin1, dna_fin2


    
    
    
    
 
    
#s1 = "MKNLASREVNIYVNGKLV"
#s2= "QMASREVNIYVNGKL"
#s2="AABBFF"

#dna_tool = DnaAligner()
#best_score, opt_loc =  dna_tool.dna_align_local(s1,s2)
#print(best_score)
'''
fin_mat_D,fin_mat_I,fin_mat_M = dna_tool.dna_align_local(s1,s2)
dna1, dna2 = dna_tool.backtrack(fin_mat_D,fin_mat_I,fin_mat_M, s1,s2)
merged_dna = dna_tool.merge(dna1, dna2)
print(merged_dna)
'''


'''
fin_mat_D,fin_mat_I,fin_mat_M = dna_align(dna1, dna2)
tuple=backtrack(fin_mat_D,fin_mat_I,fin_mat_M , dna1 , dna2)
print(tuple[0])
print(tuple[1])
print(merge(tuple[0], tuple[1]))


'''
#estimated_a=print(estimated_a)
#seq=difflib.SequenceMatcher(estimated_a,actual_a)
#print (seq.ratio())


                    
                
            


    


    

 
        
        #estimated_a=print(estimated_a)
#seq=difflib.SequenceMatcher(estimated_a,actual_a)
#print (seq.ratio())

#
#import pprint
#pprint.pprint(pprint_mat)
                    
                
            

#s1 is horizontal string
#s2 is vertical string
    
'''results = []

for row in value_dict:
    full_mat = dna_align(row['b'], row['c'])'''
    
    
'''  def dna_align_local(self, dna1, dna2 blosum):
        full_matrix_D = self.align_initialize_local(dna1, dna2)
        full_matrix_I = self.align_initialize_local(dna1, dna2)
        full_matrix_M = self.align_initialize_local(dna1, dna2)
        
        dna1 = " "+ dna1
        dna2 = " "+ dna2
        
        gap_open=-11
        gap_extend=-1
        
        best_score=0
        opt_loc=(0,0)
               
        for i in range(1, len(full_matrix_D)):
            for j in range(1, len(full_matrix_D[0])):
                
               
                match_score = blosum[dna1[j]+','+dna1[i]] #for mismatch
        
                #if dna1[j] == dna2[i]:
                 #   match_score = 0
                    
                full_matrix_D[i][j] = max([full_matrix_D[i][j-1]+ gap_extend , # 
                            full_matrix_I[i][j-1] + gap_open,
                            full_matrix_M[i][j-1]+gap_open, 0])
                            
                                
                if (full_matrix_D[i][j] > best_score):
                    best_score=full_matrix_D[i][j]
                    opt_loc=(i,j)
                            
                full_matrix_I[i][j] = max([full_matrix_D[i-1][j]+ gap_open, # 
                            full_matrix_I[i-1][j] + gap_extend,
                            full_matrix_M[i-1][j]+gap_open,0])
                                
                
                if (full_matrix_I[i][j] > best_score):
                    best_score=full_matrix_I[i][j]
                    opt_loc=(i,j)
                            
                full_matrix_M[i][j] = max([full_matrix_D[i-1][j-1]+ match_score, # diagonal
                            full_matrix_I[i-1][j-1] + match_score,
                            full_matrix_M[i-1][j-1]+match_score, 0])
                                
                if (full_matrix_D[i][j] > best_score) :
                    best_score=full_matrix_M[i][j]
                    opt_loc=(i,j)
                            
        #return (full_matrix_D, full_matrix_I,full_matrix_M)          
        return (best_score, opt_loc) '''

    
    



        
