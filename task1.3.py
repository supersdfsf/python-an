# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:42:20 2019

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

print("--------------------分割线------------------------------") 

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
#提取各售货机数据
A=new_DF.loc[new_DF['地点']=='A']#选择表格中“地点”列为D的行
B=new_DF.loc[new_DF['地点']=='B']#选择表格中“地点”列为D的行
C=new_DF.loc[new_DF['地点']=='C']#选择表格中“地点”列为D的行
D=new_DF.loc[new_DF['地点']=='D']#选择表格中“地点”列为D的行
E=new_DF.loc[new_DF['地点']=='E']#选择表格中“地点”列为D的行

def function(i,j,NEW_DF1,X) :#提取月的订单量数据
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
    
    print(X,"售货机",i,"月交易总额为",count)
    price_mean = count / DAY.loc[i-1]
    print(X,"售货机",i,"月每单平均交易额为：", price_mean)
    count_month_data = month_data.shape[0]
    print(X,"售货机",i,"月订单总量为", count_month_data )#求所有售货机订单总量
           #print('A售货机',i,'月总交易额为：', price_sum)
    daliy_count_month_data = round(count_month_data / DAY.loc[i-1])
    print(X,"售货机",i,"月日均订单总量为: ",daliy_count_month_data)

    return daliy_count_month_data

#A售货机
a1=function(1,2,A,"A")
a2=function(2,3,A,"A")
a3=function(3,4,A,"A")
a4=function(4,5,A,"A")
a5=function(5,6,A,"A")
a6=function(6,7,A,"A")
a7=function(7,8,A,"A")
a8=function(8,9,A,"A")
a9=function(9,10,A,"A")
a10=function(10,11,A,"A")
a11=function(11,12,A,"A")
a12=function(12,1,A,"A")
Adata=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12]
Adata= pd.DataFrame(Adata)
print(Adata)
#B售货机
b1=function(1,2,B,"B")
b2=function(2,3,B,"B")
b3=function(3,4,B,"B")
b4=function(4,5,B,"B")
b5=function(5,6,B,"B")
b6=function(6,7,B,"B")
b7=function(7,8,B,"B")
b8=function(8,9,B,"B")
b9=function(9,10,B,"B")
b10=function(10,11,B,"B")
b11=function(11,12,B,"B")
b12=function(12,1,B,"B")
Bdata=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]
Bdata= pd.DataFrame(Bdata)
print(Bdata)



#C售货机
c1=function(1,2,C,"C")
c2=function(2,3,C,"C")
c3=function(3,4,C,"C")
c4=function(4,5,C,"C")
c5=function(5,6,C,"C")
c6=function(6,7,C,"C")
c7=function(7,8,C,"C")
c8=function(8,9,C,"C")
c9=function(9,10,C,"C")
c10=function(10,11,C,"C")
c11=function(11,12,C,"C")
c12=function(12,1,C,"C")
Cdata=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
Cdata= pd.DataFrame(Cdata)
print(Cdata)


#D售货机
d1=function(1,2,D,"D")
d2=function(2,3,D,"D")
d3=function(3,4,D,"D")
d4=function(4,5,D,"D")
d5=function(5,6,D,"D")
d6=function(6,7,D,"D")
d7=function(7,8,D,"D")
d8=function(8,9,D,"D")
d9=function(9,10,D,"D")
d10=function(10,11,D,"D")
d11=function(11,12,D,"D")
d12=function(12,1,D,"D")
Ddata=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
Ddata= pd.DataFrame(Ddata)
print(Ddata)


#E售货机
e1=function(1,2,E,"E")
e2=function(2,3,E,"E")
e3=function(3,4,E,"E")
e4=function(4,5,E,"E")
e5=function(5,6,E,"E")
e6=function(6,7,E,"E")
e7=function(7,8,E,"E")
e8=function(8,9,E,"E")
e9=function(9,10,E,"E")
e10=function(10,11,E,"E")
e11=function(11,12,E,"E")
e12=function(12,1,E,"E")
Edata=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]
Edata= pd.DataFrame(Edata)
print(Edata)




'''
rang =[1,2,3,4,5,6,7,8,9,10,11,12]
#日均订单总量折线图
List = pd.DataFrame({"月份":rang,"A日均订单量":Adata[0],"B日均订单量":Bdata[0],"C日均订单量":Cdata[0],"D日均订单量":Ddata[0],"E日均订单量":Edata[0]})

#List = pd.DataFrame({"A每月平均交易额":Adata[0],"B每月平均交易额":Bdata[0]，"C每月平均交易额":Cdata[0]，"D每月平均交易额":Ddata[0]，"E每月平均交易额":Edata[0]})
plt.plot(List["月份"],List["A日均订单量"],'bs-',
       List["月份"],List["B日均订单量"],'ro-.',
       List["月份"],List["C日均订单量"],'gH--',
       List["月份"],List["D日均订单量"],'go-',
       List["月份"],List["E日均订单量"],'yo-')## 绘制折线图
plt.xlabel('月份')## 添加横轴标签
plt.ylabel('日均订单量（条')## 添加y轴名称
#plt.xticks(range(0,12,1))
plt.title('每台售货机每月日均订单量折线图')## 添加图表标题
plt.legend(["A售货机","B售货机","C售货机","D售货机","E售货机"],loc='best')
plt.savefig('2017每台售货机每月日均订单量折线图.png')
plt.show()
#print("月总交易额",all_mon)
List.to_csv('2017年各售货机每月日均订单量数据.csv', encoding='gbk')

'''













