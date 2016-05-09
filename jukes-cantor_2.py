# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:51:45 2016

@author: Kate
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 22:04:19 2016

@author: Kate
"""


from read_in_bosom import BlosumMat

def n_lower_chars(string):
    return sum(1 for c in string if c.islower())

file_dna = open('sample_amino_acid_sequence.txt')
dna_sequence = ((file_dna.read()).split('\n'))
print len(dna_sequence)
del dna_sequence[0]
dna_extract = ''.join(dna_sequence)
#print dna_extract

uppercasedna = ''
for nuc in dna_extract:
    if nuc.islower():
        a=1
    else:
        uppercasedna = uppercasedna + nuc

import random
len(uppercasedna)


def transition(aa_dict, NUC):
    nucleotide_string = 'ACDEFGHIKLMNPQRSTVWY'
    #nuc_temp = nucleotide_string.replace(NUC,'')
    rand_float = random.random()
    total_prob = 0.0
    for aa in nucleotide_string:
        total_prob = total_prob + aa_dict[nuc+','+aa]
        if rand_float <= total_prob:
            return aa
 '''   if (rand_float < val_same):
        return NUC
    elif (1-val_same)/3.0 < rand_float:
        return nuc_temp[0]
    elif  ((1-val_same)/3.0)*2 < rand_float:
        return nuc_temp[1]
    else:
        return nuc_temp[2]'''
    
    

from math import * 



def generateinsertion(len):
    seq = ''
    nuc = 'ACGT'
    for i in range(len):
        rand = random.random()
        if rand < .25:
            seq = seq + nuc[0]
        elif rand < .5 :
            seq = seq + nuc[1]
        elif rand < .75:
            seq = seq + nuc[2]
        else:
            seq = seq + nuc[3]
    return seq
        
    

def jukes_cantor(rt, time):
    x = (1/4.0) + (3/4.0) *exp(-4*rt*time)
    y = (1/4.0) - (1/4.0) *exp(-4*rt*time)
    return [[x,y,y,y],[y,x,y,y],[y,y,x,y],[y,y,y,x]]
    
value_dict = []

b = BlosumMat()
aa_dict =  b.read_in()

def create_seq(blosum, seq, indelrate):
     for n in seq:
                    transition_1 = transition(blosum, n)
                    transition_2 = transition(blosum, n)
                    new_seq = new_seq + transition_1
                    new_seq_2 = new_seq_2 + transition_2
                    if transition_1 == n:
                        seq_holder = seq_holder + 'C'
                    else:
                        seq_holder = seq_holder + 'S'
                    if transition_2 == n:
                        seq_holder_2 = seq_holder_2 + 'C'
                    else:
                        seq_holder_2 = seq_holder_2 + 'S'
                    ran_holder = random.random()
                    #print ran_holder, prob_dem
                    if ran_holder < prob_dem:
                        #print ran_holder
                        if random.random() < .29:
                            rand_insert = int(abs(random.normalvariate(3.63, 4.66)))
                            #print rand_insert
                            insertion = generateinsertion(rand_insert)
                            new_seq= new_seq +insertion
                            seq_holder = seq_holder + 'I' * rand_insert
                        else:
                            random_del = int(abs(random.normalvariate(6.69, 15.04)))
                            if random_del < len(new_seq) :
                                print('-------1')
                                print len(new_seq)
                                new_seq = new_seq[0:(len(new_seq)-random_del)]
                                print len(new_seq)
                                seq_holder = seq_holder + 'D' * random_del
                    ran_holder = random.random()
                    if ran_holder < prob_dem:
                        if random.random() < .29:
                            rand_insert  = int(abs(random.normalvariate(3.63, 4.66)))
                            #print rand_insert                        
                            new_seq_2= new_seq_2 +insertion
                            seq_holder_2 = seq_holder_2 + 'I' * rand_insert
                        else:
                            random_del = int(abs(random.normalvariate(6.69, 15.04)))
                            print random_del
                            if random_del < len(new_seq_2) :
                                #print('-------2')
                                #print len(new_seq_2)
                                new_seq_2 = new_seq_2[0:(len(new_seq_2)-random_del )]
                                print len(new_seq_2)
                                seq_holder_2 = seq_holder_2 + 'D' * random_del
                print str(len(new_seq)) + ' , ' + str(len(new_seq_2))
                value_dict.append({'rate': rate, 'time': time, 'indelrate': indelrate, 'a': uppercasedna, 'b': new_seq, 'c': new_seq_2, 'b_changes':seq_holder, 'c_changes': seq_holder_2, 'b_len': len(new_seq), 'c_len': len(new_seq_2), 'a_len': len(uppercasedna)})
                               
                               
 
for rates in aa_dict.keys():
    for indelrate in [25,50,100,200,300,400,500,1000,2000,3000]:
            #jukes = jukes_cantor(rate,time)
            ##jukes_ex = jukes[0][0]
            bosom_arr + aa_dict[rates]
            new_seq = ''
            seq_holder = ''
            new_seq_2 = ''
            seq_holder_2 = ''
            prob_dem = (1.0/(indelrate / rate))
           # print prob_dem
            total_internal = 0
            total_external = 0
            queue = [uppercasedna]
            while total_internal < 4 and total_external < 6 and len(queue) > 0:
                curr_dna = queue[0]
                queue = queue[1:]
                for n in curr_dna:
                    transition_1 = transition(jukes_ex, n)
                    transition_2 = transition(jukes_ex, n)
                    new_seq = new_seq + transition_1
                    new_seq_2 = new_seq_2 + transition_2
                    if transition_1 == n:
                        seq_holder = seq_holder + 'C'
                    else:
                        seq_holder = seq_holder + 'S'
                    if transition_2 == n:
                        seq_holder_2 = seq_holder_2 + 'C'
                    else:
                        seq_holder_2 = seq_holder_2 + 'S'
                    ran_holder = random.random()
                    #print ran_holder, prob_dem
                    if ran_holder < prob_dem:
                        #print ran_holder
                        if random.random() < .29:
                            rand_insert = int(abs(random.normalvariate(3.63, 4.66)))
                            #print rand_insert
                            insertion = generateinsertion(rand_insert)
                            new_seq= new_seq +insertion
                            seq_holder = seq_holder + 'I' * rand_insert
                        else:
                            random_del = int(abs(random.normalvariate(6.69, 15.04)))
                            if random_del < len(new_seq) :
                                print('-------1')
                                print len(new_seq)
                                new_seq = new_seq[0:(len(new_seq)-random_del)]
                                print len(new_seq)
                                seq_holder = seq_holder + 'D' * random_del
                    ran_holder = random.random()
                    if ran_holder < prob_dem:
                        if random.random() < .29:
                            rand_insert  = int(abs(random.normalvariate(3.63, 4.66)))
                            #print rand_insert                        
                            new_seq_2= new_seq_2 +insertion
                            seq_holder_2 = seq_holder_2 + 'I' * rand_insert
                        else:
                            random_del = int(abs(random.normalvariate(6.69, 15.04)))
                            print random_del
                            if random_del < len(new_seq_2) :
                                #print('-------2')
                                #print len(new_seq_2)
                                new_seq_2 = new_seq_2[0:(len(new_seq_2)-random_del )]
                                print len(new_seq_2)
                                seq_holder_2 = seq_holder_2 + 'D' * random_del
                print str(len(new_seq)) + ' , ' + str(len(new_seq_2))
                value_dict.append({'rate': rate, 'time': time, 'indelrate': indelrate, 'a': uppercasedna, 'b': new_seq, 'c': new_seq_2, 'b_changes':seq_holder, 'c_changes': seq_holder_2, 'b_len': len(new_seq), 'c_len': len(new_seq_2), 'a_len': len(uppercasedna)})
                               
                    
                
example_dict = {}
example_dict['data'] = value_dict

import json
            
with open('dna_synthetic.json', 'w') as outfile:
    json.dump(example_dict, outfile)       



    