# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:45:58 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
df=pd.read_csv('E:\泰迪\附件1.csv',encoding='gbk')
plt.rcParams['font.sans-serif'] = 'SimHei' ## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False


#数据去重
print('drop_duplicates方法去重之前订单总数为：',len(df))
df1 = df["订单号"].drop_duplicates()
print('drop_duplicates方法去重之后订单总数为：',len(df1))
print("@@@@到这里的时候数据量为@@@@",df1.shape)


#数据去除缺失值
print("所有售货机订单总量为",df1.shape[0])#求所有售货机订单总量
new_DF1=df1.dropna()#清理缺失值
print("清除缺失值后订单总量为",new_DF1.shape[0])


#删除超出月份的异常值
new_DF1=df.astype(str)
drity_data = new_DF1[new_DF1["支付时间"].str.contains("2017/2/29")]
print(drity_data)
new_DF = new_DF1.drop(drity_data.index)
print (new_DF)
print ("数据格式为\n",new_DF.dtypes)
print ("@@@@到这里的时候数据量为@@@@",new_DF.shape)


print(new_DF.columns)#获取列的索引名称
h=new_DF["应付金额"]#获取列名为实际金额这一列的内容
count=h.sum()#列名为实际金额列的求和
print("所有售货机交易总额为",count)

new_DF=pd.DataFrame(new_DF)
#转换表格内时间类型
print("读取的订单信息表的长度为：", len(new_DF))
new_DF["支付时间"] = pd.to_datetime(new_DF["支付时间"])
print('进行转换后表的类型为：\n',  new_DF["支付时间"].dtypes)



def function(i,j,NEW_DF1) :#提取月的订单量数据
    DAY = pd.DataFrame([31, 28, 31,30, 31, 30,31, 31, 30,31, 30, 31])

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

    
    print(month_data.columns)#获取列的索引名称
    h=month_data['实际金额']#获取列名为实际金额这一列的内容
    #转float64
    hh=h.apply(pd.to_numeric)
    print(hh.shape)
    count=np.sum(hh)#列名为实际金额列的求和
    
    #print("售货机",i,"月交易总额为",count)
    price_mean = count / DAY.loc[i-1]
    #print("售货机",i,"月每单平均交易额为：", price_mean)
    count_month_data = month_data.shape[0]
    #print("售货机",i,"月订单总量为", count_month_data )#求所有售货机订单总量
           #print('A售货机',i,'月总交易额为：', price_sum)
    daliy_count_month_data = round(count_month_data / DAY.loc[i-1])
    #print("售货机",i,"月日均订单总量为: ",daliy_count_month_data)

    return price_mean

print("--------------------分割线------------------------------")

#提取每月交易额均值
jan_month =function(1,2,new_DF)
feb_month =function(2,3,new_DF)
mar_month =function(3,4,new_DF)
apil_month =function(4,5,new_DF)
may_month =function(5,6,new_DF)
june_month =function(6,7,new_DF)
july_month =function(7,8,new_DF)
aug_month =function(8,9,new_DF)
sept_month =function(9,10,new_DF)
oct_month =function(10,11,new_DF)
nove_month =function(11,12,new_DF)
dce_month =function(12,1,new_DF)


df2=pd.read_csv('E:\泰迪\附件2.csv', encoding='gbk')#读取CSV文件

all_data = pd.merge(new_DF,df2,left_on ='商品',right_on = '商品')

y=all_data["二级类"].value_counts()[0:12]
print(y)
plt.figure(figsize=(8,6))
z=[jan_month,feb_month,mar_month,apil_month,may_month,june_month,july_month,aug_month,sept_month,oct_month,nove_month,dce_month]#输入每月交易额均值
x=[1,2,3,4,5,6,7,8,9,10,11,12]
colors=np.random.rand(len(x))
print(z)
size=z
plt.scatter(x,y,s=size,c=colors,alpha=0.8)
plt.ylim([0,10000])
plt.xlim([0,13])
plt.xlabel('时间(月份)')
plt.ylabel('二类目')
plt.title('每月交易额均值气泡图，横轴为时间，纵轴为商品的二级类')
plt.savefig('每月交易额均值气泡图.png')
plt.show()  
