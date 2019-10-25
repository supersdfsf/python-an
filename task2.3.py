# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:01:55 2019

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


#数据清洗
print("未清洗前2017年订单总量为",df.shape[0])
df=df.dropna()#清理缺失值
print("清除缺失值后2017年订单总量为",df.shape[0])

#数据去重
print('drop_duplicates方法去重之前订单总数为：',len(df))

df1 = df["订单号"].drop_duplicates()
print('drop_duplicates方法去重之后订单总数为：',len(df1))


#删除超出月份的异常值
new_DF=df.astype(str)
drity_data = new_DF[new_DF["支付时间"].str.contains("2017/2/29")]
print(drity_data)
NEW_DF = new_DF.drop(drity_data.index)
print (NEW_DF)
print (NEW_DF.shape)


#转换表格内时间类型
print("最终的订单信息表的长度为：", len(NEW_DF))
NEW_DF["支付时间"] = pd.to_datetime(NEW_DF["支付时间"])
print('进行转换后表的类型为：\n',  NEW_DF["支付时间"].dtypes)
print(NEW_DF.dtypes)
NEW_DF = pd.DataFrame(NEW_DF)
print(NEW_DF.shape)



orderGroup = NEW_DF.groupby(by = '商品',as_index=False)
print('分组后的订单详情表为：', orderGroup)

oder_group_data = orderGroup.count()
print(oder_group_data)



#统计标签频数
thing=NEW_DF["商品"].value_counts()#统计标签频数
print (thing)
print(thing.shape)


#合并清理后表格和附件二内容
df2=pd.read_csv('E:\泰迪\附件2.csv', encoding='gbk')#读取CSV文件

all_data = pd.merge(NEW_DF,df2,left_on ='商品',right_on = '商品')
#all_data.to_csv('总表.csv',encoding='gbk')#保存CSV文件


print("--------------------计算总毛利润分割线------------------------------") 

order_drink = all_data.loc[all_data['大类']=='饮料']
print("饮料类个数为",order_drink.shape[0])
order_not_drink = all_data.loc[all_data['大类']=='非饮料']
print("非饮料类个数为",order_not_drink.shape[0])

#总大类收入
order_drink_price_sum = order_drink["实际金额"].astype(float)
order_drink_pricesum = order_drink_price_sum.sum()
order_not_drink_price_sum = order_not_drink ["实际金额"].astype(float)
order_not_drink_pricesum = order_not_drink_price_sum.sum()
print("饮料类总收入为",order_drink_pricesum)
print("非饮料类总收入为",order_not_drink_pricesum)

#总毛利润
all_gross_profit_drink = order_drink_pricesum *0.25
all_gross_profit_not_drink = order_not_drink_pricesum *0.20
print("饮料类总毛利润为",all_gross_profit_drink)
print("非饮料类总毛利润为",all_gross_profit_not_drink)

print("--------------------结束结束-------------------------------")

#计算饮料类毛利润
def drinkgrossprofit(drink):
    gross_profit_drink = drink * 0.25
    return gross_profit_drink

#计算非饮料类毛利润
def notdrinkgrossprofit(notdrink):
    gross_profit_not_drink = notdrink * 0.2
    return gross_profit_not_drink

def pricealldrink(X_mac):
    Xorder_drink = X_mac.loc[X_mac['大类']=='饮料']
    MACorder_drink_price_sum = Xorder_drink["实际金额"].astype(float)
    MACorder_drink_pricesum = MACorder_drink_price_sum.sum()
    return MACorder_drink_pricesum

def priceallnotdrink(X_mac):   
    Xorder_not_drink = X_mac.loc[X_mac['大类']=='非饮料']
    MACorder_not_drink_price_sum = Xorder_not_drink ["实际金额"].astype(float)
    MACorder_not_drink_pricesum = MACorder_not_drink_price_sum.sum()
    return MACorder_not_drink_pricesum
print("---------------------计算各台售货机毛利润------------------------------")


#A售货机
A_mac=all_data.loc[all_data['地点']=="A"] #选择表格中“地点”列为A的行
print("A售货机订单数为",A_mac.shape[0])
A_drink = pricealldrink(A_mac)
print("A售货机饮料类总收入为",A_drink)
A_not_drink = priceallnotdrink(A_mac)
print("A售货机非饮料类总收入为",A_not_drink)
Agpd = drinkgrossprofit(A_drink)
Agpnd = notdrinkgrossprofit(A_not_drink)
print("A售货机饮料类毛利润为",Agpd)
print("A售货机非饮料类毛利润为",Agpnd)

print("---------------------------------------------------")

#B售货机
B_mac=all_data.loc[all_data['地点']=="B"] #选择表格中“地点”列为B的行
print("B售货机订单数为",B_mac.shape[0])
B_drink = pricealldrink(B_mac)
print("B售货机饮料类总收入为",B_drink)
B_not_drink = priceallnotdrink(B_mac)
print("B售货机非饮料类总收入为",B_not_drink)
Bgpd = drinkgrossprofit(B_drink)
Bgpnd = notdrinkgrossprofit(B_not_drink)
print("B售货机饮料类毛利润为",Bgpd)
print("B售货机非饮料类毛利润为",Bgpnd)
print("---------------------------------------------------")

#C售货机
C_mac=all_data.loc[all_data['地点']=="C"] #选择表格中“地点”列为C的行
print("C售货机订单数为",C_mac.shape[0])
C_drink = pricealldrink(C_mac)
print("C售货机饮料类总收入为",C_drink)
C_not_drink = priceallnotdrink(C_mac)
print("C售货机非饮料类总收入为",C_not_drink)
Cgpd = drinkgrossprofit(C_drink)
Cgpnd = notdrinkgrossprofit(C_not_drink)
print("C售货机饮料类毛利润为",Cgpd)
print("C售货机非饮料类毛利润为",Cgpnd)

print("---------------------------------------------------")

#D售货机
D_mac=all_data.loc[all_data['地点']=="D"] #选择表格中“地点”列为D的行
print("D售货机订单数为",D_mac.shape[0])
D_drink = pricealldrink(D_mac)
print("D售货机饮料类总收入为",D_drink)
D_not_drink = priceallnotdrink(D_mac)
print("D售货机非饮料类总收入为",D_not_drink)
Dgpd = drinkgrossprofit(D_drink)
Dgpnd = notdrinkgrossprofit(D_not_drink)
print("D售货机饮料类毛利润为",Dgpd)
print("D售货机非饮料类毛利润为",Dgpnd)

print("---------------------------------------------------")

#E售货机
E_mac=all_data.loc[all_data['地点']=="E"] #选择表格中“地点”列为E的行
print("E售货机订单数为",E_mac.shape[0])
E_drink = pricealldrink(E_mac)
print("E售货机饮料类总收入为",E_drink)
E_not_drink = priceallnotdrink(E_mac)
print("E售货机非饮料类总收入为",E_not_drink)
Egpd = drinkgrossprofit(E_drink)
Egpnd = notdrinkgrossprofit(E_not_drink)
print("E售货机饮料类毛利润为",Egpd)
print("E售货机非饮料类毛利润为",Egpnd)

print("--------------------结束结束-------------------------------")
print("---------------------------------------------------")


print("---------------------------------------------------")

P = pd.DataFrame([[Agpd,Bgpd,Cgpd,Dgpd,Egpd],[Agpnd,Bgpnd,Cgpnd,Dgpnd,Egpnd,]], columns=['A', 'B', 'C','D','E'], index = [0,1])
print(P)

ha = P.loc[0,:] / all_gross_profit_drink
print(ha)

plt.figure(figsize=(6,6))
labels = ['A', 'B', 'C', 'D','E']
explode = (0.01, 0.01, 0.01,0.01,0.01)

patches, l_text, p_text = plt.pie(ha, explode=explode, labels=labels,labeldistance=1.1, autopct='%2.1f%%', shadow=False, startangle=90, pctdistance=0.6)
plt.axis('equal')
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
# loc: 表示legend的位置，包括'upper right','upper left','lower right','lower left'等
# bbox_to_anchor: 表示legend距离图形之间的距离，当出现图形与legend重叠时，可使用bbox_to_anchor进行调整legend的位置
# 由两个参数决定，第一个参数为legend距离左边的距离，第二个参数为距离下面的距离
plt.title('售货机饮料类毛利润占总毛利润比例')
plt.grid()
plt.savefig('售货机饮料类毛利润占总毛利润比例.png')
plt.show()




haha = P.loc[1,:] / all_gross_profit_not_drink
print(haha)

plt.figure(figsize=(6,6))
labels = ['A', 'B', 'C', 'D','E']
explode = (0.01, 0.01, 0.01,0.01,0.01)

patches, l_text, p_text = plt.pie(haha, explode=explode, labels=labels,labeldistance=1.1, autopct='%3.1f%%', shadow=False, startangle=90, pctdistance=0.6)
plt.axis('equal')
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
# loc: 表示legend的位置，包括'upper right','upper left','lower right','lower left'等
# bbox_to_anchor: 表示legend距离图形之间的距离，当出现图形与legend重叠时，可使用bbox_to_anchor进行调整legend的位置
# 由两个参数决定，第一个参数为legend距离左边的距离，第二个参数为距离下面的距离
plt.title('售货机非饮料类毛利润占总毛利润比例')
plt.grid()
plt.savefig('售货机非饮料类毛利润占总毛利润比例.png')
plt.show()
