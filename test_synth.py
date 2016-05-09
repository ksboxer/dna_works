# -*- coding: utf-8 -*-
"""
Created on Mon May 09 01:20:51 2016

@author: Kate
"""

import json

data = {}

path = 'C:\\Users\\Kate\\Desktop\\Computational Genomics\\final_project\\tree_synethic_a.json'

with open(path) as data_file:    
    data = json.load(data_file)
    
data.keys()

arr_pair_wise = [[ 0 for j in range(6)] for i in range(6)]    

leaves = data['blosum62'][(len(data['blosum62'])-6):]

d = DnaAligner()

for i in range(6):
    for j in range(6):
        arr_pair_wise[i][j] = d.run(leaves[i][0], leaves[j][0])
        
def cal_overlap(synth, real):
    total_right = 0
    for idx, aa in enumerate(real):
        if len(synth) > idx and aa == synth[idx]:
            total_right = total_right +1
    print total_right
    print len(real)
    return total_right/float(len(real))
    
    
    
two_synth = 'CLGIYHDDVLLNTRQSLKKYNMSWSHKDGSEPTRILVVNCPWTNQEAGMHRDGVLMLNDDNCALEIGDDVNVLVKYIPPPCGGAIDVDQKNNELNLVATTETAKHSNYYKITGTIGRQKGIMVKKDAWTIFVDINGRCNVRLIPKVHELELHTKNKKYFKKNAFEIADGRTANNQQGLGILKKNDCVLLPFCLGLANQEEPFSKLRYLCQGEDMLAYVDGTYNGTKPTWRGRSLPHQFNVFILPGNERIIEDGFDKWNYLMETYCRSLHHVRPRQPGLSIAVTDIERAQDASLVTSG'
two_real = 'VLGIFHLDFLGAKPSLSLLKLNWCHKDSHEPGQTTIYQCIWGYKLALHSGGRLMFNDDNCRTPVTLHIPKQLCKIPPPCDNLAVQQANGMLNLEAKPANAKDVIYRITGTGTNTKDIFDEGTAWPYFLDVNNRGNVCTIPEIHKQQFHTGEKRFYKFNQFQIANGRTTQGSLLGSAKLLCLCYGEASKEDPFGLGRRCAFPRVLILGRSAFYGTKHTQYDAALNMKYDLFVLEGNDTFICDGFSLWPYLVPKYCRVLKHKHNRTPNLCHPVATLEETSDAMKIQPG'

