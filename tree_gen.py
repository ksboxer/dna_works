# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 01:58:04 2016

@author: Kate
"""

import read_in_bosom
import random

blosum  = BlosumMat()
mats = blosum.read_in()

def transition(aa, keys, blosum):
    #print keys
    rand_num = random.random()
    total_ran = 0
    total_ = []
    for p_aa in keys:
        if p_aa[0] == aa:
            #print "here"
            total_.append(blosum[p_aa])
    sum_ = sum(total_)  
    for p_aa in keys:
        if p_aa[0] == aa:
            #print p_aa[0]
            val = blosum[p_aa] / sum_
            print val
            #print total_ran
            total_ran = total_ran + val
            if rand_num <= total_ran:
                return p_aa[2]
    #print total_
    return generation_seq(1)
                
def generation_seq(length):
    new_seq = ''
    aa = 'ACDEFGHIKLMNPQRSTVWY'
    for i in range(0,length):
        rand_in = random.randint(0,19)
        new_seq = new_seq + aa[rand_in]
    return new_seq
        

def lookup_aa(index):
    for key in aa_index_dict.keys():
        if aa_index_dict[key] == index:
            return key

def new_transition(aa):
    arr = arr_aa[aa_index_dict[aa]]
    index = [i for i in range(20)]
    yx = zip(arr, index)
    yx.sort()
    yx.reverse()
    arr_sorted = [y for y, x in yx]
    arr_index_sorted = [x for y, x in yx]
    print arr_sorted
    print arr_index_sorted
    rand_num = random.random()
    total = 0
    for idx,a  in enumerate(arr_sorted):
        total =total + a
        if rand_num < total:
            return lookup_aa(arr_index_sorted[idx])

def new_seq(seq, blosum):
    blosum_keys = blosum.keys()
    new_seq = ''
    for aa in seq:
        rand_num = random.random()
        if rand_num < .000137:
            rand_in = random.random()
            if rand_in < (7/17.0):
                random_insert = int(abs(random.normalvariate(2.1, .3)))
                new_seq = new_seq + generation_seq(random_insert)
            else:
                random_deletion = int(abs(random.normalvariate(1.8, .3)))
                new_seq = new_seq[0:len(new_seq)-random_deletion]
        else:
            new_seq = new_seq + new_transition(aa)
    return new_seq


#C:\Users\Kate\Desktop\Computational Genomics\final_project\collected_amino_acids_seq\Loxodonta_africana\ENSLAFP00000000003
a = 'VLTSFSLDACGAPTRYETMKLRDPPKDHYTPGESVVYQCRLGYRIKPSFAMTAVCNDSNSWTPLQEACAKKLCSNPGDPVNGRVIQTNGTLEFGSQVDYVCDEGYRLIGEKTSYCYIYEDSVAWSSERPECNRIMCAPPPNIENGQYRNSEKEVYEYNEVVHYSCRSADYSLIGNERLICSTNGEWSTEPPKCKVVKCPFPRVDNADRIAGFGTKFVYKSKVVFQCHEGFVMNGSDTITCEGDSLWVPPVPQCVKVSTPPSTKPPILSHPVSTLPKTTSPVSSHPG'

dictionary = {}
for blos_k in mats.keys():
    blo = mats[blos_k]
    initial_list = [[a, "0"]]
    final_list = []
    count = 1
    while len(initial_list) < 6:
        rand = random.randint(0,len(initial_list)-1)
        holder = initial_list[rand]
        del initial_list[rand]
        h = new_seq(holder[0], blo)
        i = new_seq(holder[0], blo)
        final_list.append(holder)
        initial_list.append([h, holder[1] + '->'+str(count)])
        initial_list.append([i, holder[1] + '->'+str(count+1)])
        count = count + 2
    final_list = final_list + initial_list
    #print final_list
    dictionary[blos_k] = final_list
    
save_path = 'C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\tree_synethic_a.json'

import json
with open(save_path, 'w') as fp:
    json.dump(dictionary, fp)
    
    
    
    