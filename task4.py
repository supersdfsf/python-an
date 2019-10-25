# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:39:09 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import seaborn as sns
import datetime as datetime
import matplotlib.pyplot as plt
from sklearn import linear_model
from pandas import Series, DataFrame
df=pd.read_csv('E:\泰迪\附件1.csv', encoding='gbk')#读取CSV文件
plt.rcParams['font.sans-serif'] = 'SimHei' ## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
df = pd.DataFrame(df)

print("--------------------分割线------------------------------")  


#数据清洗
print("未清洗前2017年订单总量为",df.shape[0])
df=df.dropna()#清理缺失值
print("清除缺失值后2017年订单总量为",df.shape[0])

print("--------------------分割线------------------------------")

#数据去重
print('drop_duplicates方法去重之前订单总数为：',len(df))

df1 = df["订单号"].drop_duplicates()
print('drop_duplicates方法去重之后订单总数为：',len(df1))
print("@@@@到这里的时候数据量为@@@@",df1.shape)
print("--------------------分割线------------------------------")

print("--------------------分割线------------------------------")  


print("--------------------分割线------------------------------") 

#删除超出月份的异常值
new_DF=df.astype(str)
drity_data = new_DF[new_DF["支付时间"].str.contains("2017/2/29")]
print(drity_data)
NEW_DF = new_DF.drop(drity_data.index)
print (NEW_DF)
print ("数据格式为\n",NEW_DF.dtypes)
print ("@@@@到这里的时候数据量为@@@@",NEW_DF.shape)

print("--------------------分割线------------------------------") 


#转换表格内时间类型
print("使用read_csv读取的订单信息表的长度为：", len(NEW_DF))
NEW_DF["支付时间"] = pd.to_datetime(NEW_DF["支付时间"])
print('进行转换后表的类型为：\n',  NEW_DF["支付时间"].dtypes)

#合并清理后表格和附件二内容
df2=pd.read_csv('E:\泰迪\附件2.csv', encoding='gbk')#读取CSV文件

all_data = pd.merge(NEW_DF,df2,left_on ='商品',right_on = '商品')
print("--------------------分割线------------------------------") 
'''
#统计标签频数
thing = NEW_DF["商品"].value_counts()#统计标签频数
thing_order = NEW_DF["商品"].value_counts()[:5]
print (thing_order)
print(thing.shape)
#thing.to_csv('商品销量数据.csv', encoding='gbk')
'''

#提取某月数据
'''
NEW_DF1 = all_data.set_index("支付时间")
Jan_month_data=NEW_DF1.loc["2017-01"]
print(Jan_month_data)
'''

#A售货机
#A_mac=all_data.loc[all_data['地点']=="A"] #选择表格中“地点”列为A的行
#print("A售货机订单数为",A_mac.shape[0])
order_drink = all_data.loc[all_data['大类']=='饮料']
print("月饮料类个数为",order_drink.shape[0])
order_not_drink = all_data.loc[all_data['大类']=='非饮料']
print("月非饮料类个数为",order_not_drink.shape[0])

def funmoney(i,j,NEW_DF12) :#提取月的订单量数据
    begin = datetime.date(2017, i, 1)
    day = begin +datetime.timedelta(days = 1)
    if i == 12:
        end = datetime.date(2018,12,31)
    else:
        end = datetime.date(2017,j,1)
    subset = NEW_DF12[NEW_DF12["支付时间"] > begin]
    month_data = subset[subset["支付时间"] < end]
    #print(month_data.shape)
    #print(month_data)
    #month_data = pd.DataFrame(month_data)
    #print(month_data.columns)#获取列的索引名称
    h=month_data['实际金额']#获取列名为实际金额这一列的内容
    #转float64
    hh=h.apply(pd.to_numeric)
    #print(hh.shape)
    count=np.sum(hh)#列名为实际金额列的求和    
    #print("饮料类",i,"月交易总额为",count)
    return count

def funday(i,j,NEW_DF1) :#提取月的订单量数据
    begin = datetime.date(2017, i, 1)
    day = begin +datetime.timedelta(days = 1)
    if i == 12:
        end = datetime.date(2018,12,31)
    else:
        end = datetime.date(2017,j,1)
        
    subset = NEW_DF1[NEW_DF1["支付时间"] > begin]
    month_data = subset[subset["支付时间"] < end]
    #print(month_data.shape)
    #print(month_data)
    #month_data = pd.DataFrame(month_data)
    count_month_data = month_data.shape[0]
    #print("饮料类",i,"月订单总量为", count_month_data )#求所有售货机订单总量
    return count_month_data

a1=funday(1,2,order_drink)
a2=funday(2,3,order_drink)
a3=funday(3,4,order_drink)
a4=funday(4,5,order_drink)
a5=funday(5,6,order_drink)
a6=funday(6,7,order_drink)
a7=funday(7,8,order_drink)
a8=funday(8,9,order_drink)
a9=funday(9,10,order_drink)
a10=funday(10,11,order_drink)
a11=funday(11,12,order_drink)
a12=funday(12,1,order_drink)
drinkdata=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12]
drinkdata= pd.DataFrame(drinkdata)
print(drinkdata)

aa1=funmoney(1,2,order_drink)
aa2=funmoney(2,3,order_drink)
aa3=funmoney(3,4,order_drink)
aa4=funmoney(4,5,order_drink)
aa5=funmoney(5,6,order_drink)
aa6=funmoney(6,7,order_drink)
aa7=funmoney(7,8,order_drink)
aa8=funmoney(8,9,order_drink)
aa9=funmoney(9,10,order_drink)
aa10=funmoney(10,11,order_drink)
aa11=funmoney(11,12,order_drink)
aa12=funmoney(12,1,order_drink)
drink_data=[aa1,aa2,aa3,aa4,aa5,aa6,aa7,aa8,aa9,aa10,aa11,aa12]
drink_data= pd.DataFrame(drink_data)
print(drink_data)
dorder_list = pd.DataFrame({"饮料类月消费金额":drink_data[0],"饮料类月订单量":drinkdata[0]})



#非饮料类数据
b1=funday(1,2,order_not_drink)
b2=funday(2,3,order_not_drink)
b3=funday(3,4,order_not_drink)
b4=funday(4,5,order_not_drink)
b5=funday(5,6,order_not_drink)
b6=funday(6,7,order_not_drink)
b7=funday(7,8,order_not_drink)
b8=funday(8,9,order_not_drink)
b9=funday(9,10,order_not_drink)
b10=funday(10,11,order_not_drink)
b11=funday(11,12,order_not_drink)
b12=funday(12,1,order_not_drink)
notdrinkdata=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]
notdrinkdata= pd.DataFrame(notdrinkdata)
print(notdrinkdata)

bb1=funmoney(1,2,order_not_drink)
bb2=funmoney(2,3,order_not_drink)
bb3=funmoney(3,4,order_not_drink)
bb4=funmoney(4,5,order_not_drink)
bb5=funmoney(5,6,order_not_drink)
bb6=funmoney(6,7,order_not_drink)
bb7=funmoney(7,8,order_not_drink)
bb8=funmoney(8,9,order_not_drink)
bb9=funmoney(9,10,order_not_drink)
bb10=funmoney(10,11,order_not_drink)
bb11=funmoney(11,12,order_not_drink)
bb12=funmoney(12,1,order_not_drink)
notdrink_data=[bb1,bb2,bb3,bb4,bb5,bb6,bb7,bb8,bb9,bb10,bb11,bb12]
notdrink_data= pd.DataFrame(notdrink_data)
print(notdrink_data)
ndorder_list = pd.DataFrame({"非饮料类月消费金额":notdrink_data[0],"非饮料类月订单量":notdrinkdata[0]})


x=dorder_list["饮料类月消费金额"]
y=dorder_list["饮料类月订单量"]
plt.scatter(x, y)    # 用散点图展示x和y
plt.xlabel("月消费金额")
plt.ylabel("月订单量")
plt.title('2017年饮料类销售数据线性分析')## 添加图表标题
plt.savefig('2017年饮料类销售数据线性分析散点图.png')
plt.show()

x1=ndorder_list["非饮料类月消费金额"]
y1=ndorder_list["非饮料类月订单量"]
plt.scatter(x1, y1)    # 用散点图展示x和y
plt.xlabel("月消费金额")
plt.ylabel("月订单量")
plt.title('2017年非饮料类销售数据线性分析')## 添加图表标题
plt.savefig('2017年非饮料类销售数据线性分析散点图.png')
plt.show()

x1 = np.array(x1).reshape([12, 1])
y1 = np.array(y1).reshape([12, 1])
#数据建模
model = linear_model.LinearRegression()#创建一个模型对象
model.fit(x1, y1)#将x和y分别作为自变量和因变量输入模型进行训练

#模型评估
model_coef = model.coef_    # 获取模型的自变量系数并赋值为 model_coef
model_intercept = model.intercept_    # 获取模型的截距并赋值为 model_intercept
r2 = model.score(x1, y1)    # 获取模型的决定系数R的平方
print(model_coef,model_intercept,r2)

#2018年1月销售预测
#new_y = 2000 
#pre_x = model.predict( np.array(new_y).reshape(-1, 1))#对常量new_y输入模型进行预测
#print (pre_x)    


#用seaborn里面的线型回归查看拟合直线
sns.lmplot(x='饮料类月消费金额',y='饮料类月订单量',data=dorder_list)
sns.lmplot(x='非饮料类月消费金额',y='非饮料类月订单量',data=ndorder_list)




