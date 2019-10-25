# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:08:21 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import datetime as datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from pandas import Series, DataFrame
df=pd.read_csv('E:\泰迪\附件1.csv', encoding='gbk')#读取CSV文件
plt.rcParams['font.sans-serif'] = 'SimHei' ## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
df = pd.DataFrame(df)

#数据清洗————缺失值处理
print("未清洗前2017年订单总量为",df.shape[0])
df=df.dropna()#清理缺失值
print("清除缺失值后2017年订单总量为",df.shape[0])

#数据去重
print('drop_duplicates方法去重之前订单总数为：',len(df))

df1 = df["订单号"].drop_duplicates()
print('drop_duplicates方法去重之后订单总数为：',len(df1))
print("@@@@到这里的时候数据量为@@@@",df1.shape)
print("--------------------分割线------------------------------")  

#删除超出月份的异常值
new_DF=df.astype(str)
drity_data = new_DF[new_DF["支付时间"].str.contains("2017/2/29")]
print(drity_data)
NEW_DF = new_DF.drop(drity_data.index)
print (NEW_DF)
print ("数据格式为\n",NEW_DF.dtypes)
print ("@@@@到这里的时候数据量为@@@@",NEW_DF.shape)


#转换表格内时间类型
print("最终的订单信息表的长度为：", len(NEW_DF))
NEW_DF["支付时间"] = pd.to_datetime(NEW_DF["支付时间"])
print('进行转换后表的类型为：\n',  NEW_DF["支付时间"].dtypes)
print(NEW_DF.dtypes)
NEW_DF = pd.DataFrame(NEW_DF)
print("@@@@到这里的时候数据量为@@@@",NEW_DF.shape)

#提取每台售货机数据
A1=NEW_DF.loc[NEW_DF['地点']=='A']#选择表格中“地点”列为D的行
B1=NEW_DF.loc[NEW_DF['地点']=='B']#选择表格中“地点”列为D的行
C1=NEW_DF.loc[NEW_DF['地点']=='C']#选择表格中“地点”列为D的行
D1=NEW_DF.loc[NEW_DF['地点']=='D']#选择表格中“地点”列为D的行
E1=NEW_DF.loc[NEW_DF['地点']=='E']#选择表格中“地点”列为D的行


#所有售货机交易总额
h= NEW_DF["实际金额"]
h= h.astype(float)
ALL_sumprice=h.sum()
print("所有售货机交易总额为",ALL_sumprice)
#所有售货机订单总量
print("所有售货机订单总量为",len(NEW_DF))



#提取月的订单量数据
def function(i,j,NEW_DF1,name) :
    begin = datetime.date(2017, i, 1)
    day = begin +datetime.timedelta(days = 1)
    if i == 12:
        end = datetime.date(2018,12,31)
    else:
        end = datetime.date(2017,j,1)
        
    subset = NEW_DF1[NEW_DF1["支付时间"] > begin]
    month_data = subset[subset["支付时间"] < end]
    print(month_data.shape)
    #print(month_data)
    #month_data = pd.DataFrame(month_data)
    print("---------------------------------------------------")
    print("--------------------分割线------------------------------")
    #print(month_data.columns)#获取列的索引名称
    h=month_data['实际金额']#获取列名为实际金额这一列的内容
    #转float64
    hh=h.apply(pd.to_numeric)
    print(hh.shape)
    count=np.sum(hh)#列名为实际金额列的求和
    print(name,"售货机",i,"月售货机交易总额为",count)
    count_month_data = month_data.shape[0]
    print(name,"售货机",i,"月订单总量为", count_month_data ,"\n--------------------结束分割线------------------------------")#求所有售货机订单总量
           #print('A售货机',i,'月总交易额为：', price_sum)
    return count,count_month_data
    
#A售货机
aaaa=function(5,6,A1,"A")
print(aaaa)

#print(aaaa.dtypes)
#B售货机
function(5,6,B1,"B")
#C售货机
function(5,6,C1,"C")

#D售货机
function(5,6,D1,"D")

#E售货机
function(5,6,E1,"E")





















