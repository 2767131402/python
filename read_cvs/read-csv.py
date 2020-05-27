#!/usr/bin/python
# -*- coding:utf8 -*-

import pandas as pd
import numpy as np

# DATA = {
#     'english': ['one','two','three'],
#     'number': [1,2,3]
# }
# save = pd.DataFrame(DATA,index=['row1','row2','row3'],columns=['english','number'])
# print(save)
# save.to_csv('test1.csv',sep=',')

# df = pd.read_csv('name.csv',sep=',',encoding='gbk',names=['column1','column2','column3'],index_col=['column1'],skiprows=[0],na_values=['NULL'])
df1 = pd.read_csv('name.csv',sep='\t',encoding='gbk',na_values=['NULL'])
print(df1)