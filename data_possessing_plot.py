# -*- coding: utf-8 -*-
# @Time    : 2023/9/12 14:41
# @Author  : max
# @FileName: data_possessing_plot.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

originpath = "F:\\实验测试\\20231101\\"

z=range(1,150,1) # z= [1,3,5,7]

for i in z:
    if i<10:
        name = "file_00"+str(i)
    elif i<100:
        name =  "file_0" + str(i)
    else:
        name =  "file_" + str(i)
    path = originpath + name +".dat"
    with open(path,'r') as f:
        for i, line in enumerate(f):
            if i == 15:
                pre = line.split(';')
                RBW = pre[1]
            if i == 16:
                pre = line.split(';')
                VBW = pre[1]
    raw_data = pd.read_csv(path,sep=';',skiprows=30) #notice: the sep may be different
    data_array = np.array(raw_data)
    x_data = data_array[:,0]
    y_data = data_array[:,1]
    if min(x_data)>1e9:
        x_min = min(x_data)/1e9
        x_max = max(x_data)/1e9
        x_caption = "Frequency (GHz)"
    else:
        x_min = min(x_data)/1e9
        x_max = max(x_data)/1e9
        x_caption = "Frequency (MHz)"
    y_min = min(y_data)-5
    y_max = max(y_data)+5
    title = name + " RBW = " + RBW + "Hz VBW = " +VBW + " Hz"
    plt.figure(figsize=(16,8))
    plt.plot(x_data/1e6,y_data)
    plt.xlabel(x_caption)  # 此处需要与上面匹配
    plt.ylabel("Power(dBm)")
    plt.xlim((x_min,x_max))
    plt.ylim((y_min,y_max))
    plt.text(1,0,RBW)
    path_figure = originpath + name + ".jpg"
    plt.title(title)
    plt.savefig(path_figure)
    plt.close()
    #plt.grid()
    plt.show()

