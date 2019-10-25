# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:31:02 2019

@author: lenovo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time,datetime
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus']=False
DATA1=pd.read_csv('task1-1C.csv',encoding='gbk')

#删除超出月份的异常值
new_DF1=DATA1.astype(str)
drity_data = new_DF1[new_DF1["支付时间"].str.contains("2017/2/29")]
print(drity_data)
DATA = new_DF1.drop(drity_data.index)
print (DATA)
print ("数据格式为\n",DATA.dtypes)
print ("@@@@到这里的时候数据量为@@@@",DATA.shape)



DATA['支付时间']=pd.to_datetime(DATA['支付时间'])
data_6=DATA[(DATA['支付时间']>=pd.to_datetime('20170601'))&(DATA['支付时间']<=pd.to_datetime('20170901'))]
DATA_6=pd.date_range('20170601','20170701',freq='H') ##提取六月分的时间

l_6=[]
q_6=[]
k_6=0
delta=pd.Timedelta(hours=1)
for s in DATA_6:
    for d in data_6['支付时间']:
        if (d>=s)and(d<s+delta):
            l_6.append(d)
    t1=k_6
    k_6=len(l_6)
    t2=k_6-t1
    q_6.append(t2)
q_6.pop()

X_6=q_6
Y_6=np.array(X_6)
b_6=Y_6.reshape(30,24)##将数组重新格式化
f,ax_6=plt.subplots(figsize=(12,10))##设置画布大小
cmap=sns.cubehelix_palette(start=1.5,rot=3,gamma=0.8,as_cmap=True) ##cmap用cubeheli map颜色
sns.heatmap(b_6,linewidths=0.05,cmap='Blues_r')
ax_6.set_title('C售货机6月的订单量热力图')
ax_6.set_xticklabels(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
ax_6.set_xlabel('小时')
ax_6.set_yticklabels(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'])
ax_6.set_ylabel('月份/天')
plt.savefig('C售货机6月的订单量热力图.png')
plt.show()


print("----------------------C售货机7月的订单量热力图-------------------------------------")

data_7=DATA[(DATA['支付时间']>=pd.to_datetime('20170601'))&(DATA['支付时间']<=pd.to_datetime('20170901'))]
DATA_7=pd.date_range('20170701','20170801',freq='H') ##提取六月分的时间

l_7=[]
q_7=[]
k_7=0
delta=pd.Timedelta(hours=1)
for s in DATA_7:
    for d in data_7['支付时间']:
        if (d>=s)and(d<s+delta):
            l_7.append(d)
    t1=k_7
    k_7=len(l_7)
    t2=k_7-t1
    q_7.append(t2)
q_7.pop()

X_7=q_7
Y_7=np.array(X_7)
b_7=Y_7.reshape(31,24)##将数组重新格式化
f,ax_7=plt.subplots(figsize=(12,10))##设置画布大小
cmap=sns.cubehelix_palette(start=1.5,rot=3,gamma=0.8,as_cmap=True) ##cmap用cubeheli map颜色
sns.heatmap(b_7,linewidths=0.05,cmap='Blues_r')
ax_7.set_title('C售货机7月的订单量热力图')
ax_7.set_xticklabels(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
ax_7.set_xlabel('小时')
ax_7.set_yticklabels(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30',"31"])
ax_7.set_ylabel('月份/天')
plt.savefig('C售货机7月的订单量热力图.png')
plt.show()




print("----------------------C售货机8月的订单量热力图-------------------------------------")

data_8=DATA[(DATA['支付时间']>=pd.to_datetime('20170601'))&(DATA['支付时间']<=pd.to_datetime('20170901'))]
DATA_8=pd.date_range('20170801','20170901',freq='H') ##提取六月分的时间

l_8=[]
q_8=[]
k_8=0
delta=pd.Timedelta(hours=1)
for s in DATA_8:
    for d in data_8['支付时间']:
        if (d>=s)and(d<s+delta):
            l_8.append(d)
    t1=k_8
    k_8=len(l_8)
    t2=k_8-t1
    q_8.append(t2)
q_8.pop()

X_8=q_8
Y_8=np.array(X_8)
b_8=Y_8.reshape(31,24)##将数组重新格式化
f,ax_8=plt.subplots(figsize=(12,10))##设置画布大小
cmap=sns.cubehelix_palette(start=1.5,rot=3,gamma=0.8,as_cmap=True) ##cmap用cubeheli map颜色
sns.heatmap(b_8,linewidths=0.05,cmap='Blues_r')
ax_8.set_title('C售货机8月的订单量热力图')
ax_8.set_xticklabels(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
ax_8.set_xlabel('小时')
ax_8.set_yticklabels(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30',"31"])
ax_8.set_ylabel('月份/天')
plt.savefig('C售货机8月的订单量热力图.png')
plt.show()






