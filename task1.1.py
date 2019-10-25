# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series, DataFrame

df=pd.read_csv('E:\泰迪\附件1.csv', encoding='gbk')#读取CSV文件
print(df.shape)#计算出表格的行列数值
print(df.columns)#展示表格列的内容
d=df.loc[df['地点']=='D']#选择表格中“地点”列为D的行
d.to_csv('task1-1D.csv',encoding='gbk')#存入文件名为task1-1D.csv的表格中

b=df.loc[df['地点']=='B']#选择表格中“地点”列为B的行
b.to_csv('task1-1B.csv',encoding='gbk')#存入文件名为task1-1B.csv的表格中

a=df.loc[df['地点']=='A']#选择表格中“地点”列为A的行
a.to_csv('task1-1A.csv',encoding='gbk')#存入文件名为task1-1A.csv的表格中

c=df.loc[df['地点']=='C']#选择表格中“地点”列为C的行
c.to_csv('task1-1C.csv',encoding='gbk')#存入文件名为task1-1C.csv的表格中

e=df.loc[df['地点']=='E']#选择表格中“地点”列为E的行
e.to_csv('task1-1E.csv',encoding='gbk')#存入文件名为task1-1E.csv的表格中

