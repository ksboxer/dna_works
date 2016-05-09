# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:18:04 2016

@author: Kate
"""

from glob import glob
import json


import numpy 

def add_into(mat1, mat2):
    for idx_i,i in enumerate(mat1):
        for idx_j,j in enumerate(mat1[0]):
            #print mat2[idx_i][idx_j]
            if type(mat2[idx_i][idx_j]) is float :
                mat1[idx_i][idx_j].append(mat2[idx_i][idx_j])
            else:
                #print type()
                #print mat2[idx_i][idx_j]
                mat1[idx_i][idx_j].append(mat2[idx_i][idx_j][0])
    return mat1

processed_data = 'C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\processed_cluster_data_v2\\'


dis_mat = [[ [] for x in range(6)] for y in range(6)]
print dis_mat

import math
import numpy

for f_name in glob(processed_data+'*.json'):
    with open(f_name) as data_file:
        seq_2 = json.load(data_file)
        dis = seq_2['dist_mat']
        list_=[]
        for i in dis:
            for j in i:
                if type(j) is not float:
                    list_.append(j[0])
        std = numpy.std(list_)
        avg = numpy.average(list_)
        for idx,i in enumerate(dis):
            for idx_j, j in enumerate(dis[0]):
                if type(dis[idx][idx_j]) is not float and idx <> idx_j:
                    dis[idx][idx_j][0] =dis[idx][idx_j][0] 
        total_list = []
        dis_mat = add_into(dis_mat, dis)

dis_mat_fin = [[ (0,0,0) for x in range(6)] for y in range(6)]
dis_mat_just_dis = [[ 0 for x in range(6)] for y in range(6)]
n_count = [[ 0 for x in range(6)] for y in range(6)]
std_count =[[ 0 for x in range(6)] for y in range(6)]

freq_count = []
it = 0
total_list = []
for idx, i in enumerate(dis_mat):
    for idx_j, i in enumerate(dis_mat[0]):
        non_nan_count = 0
        non_nan_list = []
        for t in dis_mat[idx][idx_j]:
            if math.isnan(t) == False:
                freq_count.append(t)
                non_nan_count = non_nan_count + 1
                non_nan_list.append(t)
        total_list = total_list + non_nan_list
        sum_ = sum(non_nan_list)
        std =  numpy.std(non_nan_list)
        #plt.figure(it)
        it = it +1
        #plt.hist(non_nan_list, bins=20)
        avg = sum_ / non_nan_count
        dis_mat_fin[idx][idx_j] = (avg, std, non_nan_count)
        dis_mat_just_dis[idx][idx_j] = round(avg, 3)
        std_count[idx][idx_j] = round(std,2)
        n_count[idx][idx_j] = non_nan_count

str_ = ''     
for d in dis_mat_fin:

    for i in d:
        str_ = str_ + "  s=" + str(i[0]) + '  std=' + str(i[1]) + '  n=' + str(i[2]) + ' , '
        
    print str_