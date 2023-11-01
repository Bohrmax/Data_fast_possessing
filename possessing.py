# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:03:54 2023

@author: Bohr max
"""
import pandas as pd
import os
# 获取当前目录下所有的txt文件

files = os.listdir('.')
for file in files:
    [num,index] = file
    

    
txts = [file for file in files if file.endswith('.txt')]
for txt in txts:
    

    for i in range(len(txts)):
        txt = "file"+ i +".txt" 
        txt="file_{}.".format(i)
# 遍历所有txt文件并进行处理

    # 读取txt文件
        df = pd.read_csv(txt, sep='\t')

    # 进行数据处理
    # ...

    # 将处理后的数据写入新的txt文件
        df.to_csv('new_' + txt, sep='\t', index=False)
