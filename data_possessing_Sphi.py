# -*- coding: utf-8 -*-
# @Time    : 2023/10/10 11:12
# @Author  : max
# @FileName: data_possessing_Sphi.py
# -*- coding: utf-8 -*-
# @Time    : 2023/9/28 9:49
# @Author  : max
# @FileName: data_possessing_phase_noise.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

originpath = "F:\\实验测试\\20231007_DCScombline_phasenoise\\"

#fig = plt.figure(figsize=(16,8))
z=[6,13,17,23,28,33,41,46,51,56]
for i in z:
    if i<10:
        name = "file_00"+str(i)
    elif i<100:
        name =  "file_0" + str(i)
    else:
        name =  "file_" + str(i)
    path = originpath + name +".csv"
    raw_data = pd.read_csv(path,sep=',',skiprows=174)
    data_array = np.array(raw_data)
    x_data = data_array[:,0]
    y_data = data_array[:,1]
    x_min = min(x_data)
    x_max = max(x_data)
    y_min = min(y_data)-5
    y_max = max(y_data)+5


    line, = plt.plot(x_data,y_data,label = name)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Sφ(f) [dB/Hz]")
    plt.xscale('log')
    plt.grid()
    #plt.yscale('log')

    plt.xlim((x_min,x_max))
    #plt.ylim((-160,60))
    #plt.legend(handles = [line])
    path_figure = originpath + name + ".jpg"
    plt.title(name)
    plt.savefig(path_figure)
    plt.close()

    #plt.show()

#fig.legend()