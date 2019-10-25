# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:39:09 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import datetime as datetime
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
df=pd.read_csv('E:\泰迪\附件1.csv', encoding='gbk')#读取CSV文件
plt.rcParams['font.sans-serif'] = 'SimHei' ## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
df = pd.DataFrame(df)

#数据清洗
print("未清洗前2017年订单总量为",df.shape[0])
df=df.dropna()#清理缺失值
print("清除缺失值后2017年订单总量为",df.shape[0])

#数据去重
print('drop_duplicates方法去重之前订单总数为：',len(df))

df1 = df["订单号"].drop_duplicates()
print('drop_duplicates方法去重之后订单总数为：',len(df1))
print("@@@@到这里的时候数据量为@@@@",df1.shape)

#删除超出月份的异常值
new_DF=df.astype(str)
drity_data = new_DF[new_DF["支付时间"].str.contains("2017/2/29")]
print(drity_data)
NEW_DF = new_DF.drop(drity_data.index)
print (NEW_DF)
print ("数据格式为\n",NEW_DF.dtypes)
print ("@@@@到这里的时候数据量为@@@@",NEW_DF.shape)


#转换表格内时间类型
print("使用read_csv读取的订单信息表的长度为：", len(NEW_DF))
NEW_DF["支付时间"] = pd.to_datetime(NEW_DF["支付时间"])
print('进行转换后表的类型为：\n',  NEW_DF["支付时间"].dtypes)

year = [i.year for i in NEW_DF["支付时间"]]## 提取年份信息
month = [i.month for i in NEW_DF["支付时间"]]## 提取月份信息
day = [i.day for i in  NEW_DF["支付时间"]]## 提取日期信息
week = [i.week for i in  NEW_DF["支付时间"]]## 提取周信息
weekday = [i.weekday() for i in  NEW_DF["支付时间"]]##提取星期信息
weekname = [i.weekday_name for i in  NEW_DF["支付时间"]]## 提取星期名称信息

timemin = NEW_DF["支付时间"].min()
timemax = NEW_DF["支付时间"].max()
print('订单最早的时间为：',timemin)
print('订单最晚的时间为：',timemax)

#提取某月数据
NEW_DF1 = NEW_DF.set_index("支付时间")
June_month_data=NEW_DF1.loc["2017-06"]
print(June_month_data)

print("--------------------分割线------------------------------") 

#统计标签频数
thing = June_month_data["商品"].value_counts()#统计标签频数
thing_order = June_month_data["商品"].value_counts()[:5]
print (thing_order)
print(thing.shape)

print("--------------------分割线------------------------------") 

#画柱状图
plt.xlabel('商品名称')## 添加横轴标签
plt.ylabel('销量（件）')## 添加纵轴标签
print(thing_order.index)
label1 = thing_order.index
plt.bar(range(len(thing_order)), thing_order,width = 0.35,label = label1)
plt.xticks(range(5),label1,rotation=90)
my_height=thing_order.values
for i in range(len(my_height)):
    plt.text(i, my_height[i], my_height[i], va='bottom', ha='center')
plt.title("2017商品6月销量前5的柱状图")
plt.tight_layout()
plt.savefig('2017年6月销量前5的商品.png')
plt.show()




