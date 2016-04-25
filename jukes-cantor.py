# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:15:05 2016

@author: Kate
"""


    
import numpy as np

plot_values_time_1 = []
plot_values_time_2 = []
plot_values_time_3 = []
for i in np.arange(0,1,0.01).tolist():
    arr = jukes_cantor(i,1)
    arr_2 = jukes_cantor(i , 2)
    arr_3 = jukes_cantor(i , 3)
    plot_values_time_1.append([i, arr[0][0], arr[0][1]])
    plot_values_time_2.append([i, arr_2[0][0], arr_2[0][1]])
    plot_values_time_2.append([i, arr_3[0][0], arr_3[0][1]])
    
    
    
#[row[1] for row in A]
    
import matplotlib.pyplot as plt
plt.plot(np.arange(0,1,0.01), [row[1] for row in plot_values_time_3], np.arange(0,1,0.01), [row[2] for row in plot_values_time_3])
plt.xlabel('rate', fontsize = 40)
plt.ylabel('pr', fontsize = 40)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

mean = 3.63
variance = 1
sigma = 4.66
x = 59
plt.plot(x,mlab.normpdf(x,mean,sigma))

plt.show()


import pylab
from scipy.stats import norm
x = np.linspace(-100,100,1000)
y = norm.pdf(x, loc=3.63, scale=4.66)  
x1 =  np.linspace(-100,100,1000)
y1 = norm.pdf(x, loc=mean, scale=15.04)    # for example
pylab.plot(x,y)
pylab.plot(x1,y1)
pylab.show()