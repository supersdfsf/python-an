# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:58:25 2019

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


def function(i,j,NEW_DF1) :#提取月的订单量数据
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
    print("售货机",i,"月售货机交易总额为",count)
    
    count_month_data = month_data.shape[0]
    print("售货机",i,"月订单总量为", count_month_data ,"\n--------------------结束分割线------------------------------")#求所有售货机订单总量
           #print('A售货机',i,'月总交易额为：', price_sum)
    return count
    

#一次性输出每台每月总交易额       
'''for i in range(1,13):
    j = i +1
    function(i,j)
'''

print("--------------------月环比增长率-------------------------------")

    
    
def monprice(X):
    
    #每月总交易额
    Jan_month =function(1,2,X)
    Feb_month =function(2,3,X)
    Mar_month =function(3,4,X)
    Apr_month =function(4,5,X)
    May_month =function(5,6,X)
    June_month=function(6,7,X) 
    July_month=function(7,8,X) 
    Aug_month =function(8,9,X)
    Sept_month=function(9,10,X) 
    Oct_month =function(10,11,X)
    Nov_month =function(11,12,X)
    Dec_month =function(12,1,X)

    
    monthsdata=[Jan_month,Feb_month,Mar_month,Apr_month,May_month,June_month, July_month, Aug_month ,Sept_month, Oct_month ,Nov_month ,Dec_month]
    monthsdata= pd.DataFrame(monthsdata)
    monthsdata.index=["1", "2", "3","4", "5", "6","7", "8", "9","10", "11", "12"]
    print("月总交易额",monthsdata)
    huanbi_data=monthsdata.pct_change()
    huanbi_data = huanbi_data[0].apply(lambda x: format(x, '.2%'))#format(res,'.2%') 小数格式化为百分数
    print("月环比 \n",huanbi_data)
    
    print("--------------------月环比增长率画图画图-------------------------------")
    monthsdata.rename(columns={'index':"商品", 0:"销售额"}, inplace = True)
    
    rng = monthsdata.index #生成日期
    mony = monthsdata["销售额"] #销售额
    
    data = pd.DataFrame({"月份":rng,"销售额":monthsdata["销售额"]}) #组成一个dataframe
    data['huanbi_1'] = '1'
#使用diff（periods=1, axis=0)） 一阶差分函数
#periods：移动的幅度 默认值为1
#axis:移动的方向，{0 or ‘index’, 1 or ‘columns’}，如果为0或者’index’，则上下移动，如果为1或者’columns’，则左右移动。默认列向移动
    for i in range(0,len(data)):
        
        if i == 0:
            data['huanbi_1'][i] = '0'
        else:
            data['huanbi_1'][i] = ((data["销售额"][i] - data["销售额"][i-1])/data["销售额"][i-1])
        #format(res,'.2%') 小数格式化为百分数
    print("环比列表\n",data)
    return data 




A=NEW_DF.loc[NEW_DF['地点']=='A']#选择表格中“地点”列为D的行
B=NEW_DF.loc[NEW_DF['地点']=='B']#选择表格中“地点”列为D的行
C=NEW_DF.loc[NEW_DF['地点']=='C']#选择表格中“地点”列为D的行
D=NEW_DF.loc[NEW_DF['地点']=='D']#选择表格中“地点”列为D的行
E=NEW_DF.loc[NEW_DF['地点']=='E']#选择表格中“地点”列为D的行

A_monprice = monprice(A)
print("A售货机月环比数据",A_monprice)

B_monprice = monprice(B)
print("B售货机月环比数据",B_monprice)

C_monprice = monprice(C)
print("C售货机月环比数据",C_monprice)

D_monprice = monprice(D)
print("D售货机月环比数据",D_monprice)

E_monprice = monprice(E)
print("E售货机月环比数据",E_monprice)

da = ["1", "2", "3","4", "5", "6","7", "8", "9","10", "11", "12"]

ALL_MONPRICE = pd.DataFrame({"月份":da,"A售货机":A_monprice["huanbi_1"],"B售货机":B_monprice["huanbi_1"],"C售货机":C_monprice["huanbi_1"],"D售货机":D_monprice["huanbi_1"],"E售货机":E_monprice["huanbi_1"]}) #组成一个dataframe
print("总月交易额环比表",ALL_MONPRICE)
ALL_MONPRICE.to_csv('2017年各售货机交易额月环比增长率数据.csv', encoding='gbk')

ALL_MONPRICE = ALL_MONPRICE.astype(float)
print(ALL_MONPRICE.dtypes)
ALL_MONPRICE_copy = ALL_MONPRICE[["A售货机","B售货机","C售货机","D售货机","E售货机"]]
ALL_MONPRICE_copy = pd.DataFrame(ALL_MONPRICE_copy)
ALL_MONPRICE_copy.plot(kind='bar')
plt.xlabel("月份")
plt.title("2017每台售货机每月交易额月环比增长率柱状图")
plt.savefig('2017每台售货机每月交易额月环比增长率柱状图.png')

print("--------------------每月总交易额画图画图-------------------------------")


def monallprice(X):
    
    #每月总交易额
    Jan_month =function(1,2,X)
    Feb_month =function(2,3,X)
    Mar_month =function(3,4,X)
    Apr_month =function(4,5,X)
    May_month =function(5,6,X)
    June_month=function(6,7,X) 
    July_month=function(7,8,X) 
    Aug_month =function(8,9,X)
    Sept_month=function(9,10,X) 
    Oct_month =function(10,11,X)
    Nov_month =function(11,12,X)
    Dec_month =function(12,1,X)

    monthsdata=[Jan_month,Feb_month,Mar_month,Apr_month,May_month,June_month, July_month, Aug_month ,Sept_month, Oct_month ,Nov_month ,Dec_month]
    monthsdata= pd.DataFrame(monthsdata)
    monthsdata.index=["1", "2", "3","4", "5", "6","7", "8", "9","10", "11", "12"]
    print("月总交易额",monthsdata)
    return monthsdata

A_monallprice = monallprice(A)
print("A售货机总交易额数据",A_monallprice)
A_monallprice = A_monallprice.astype(float)
print(A_monallprice.dtypes)

B_monallprice = monallprice(B)
print("B售货机总交易额数据",B_monallprice)
B_monallprice = B_monallprice.astype(float)

C_monallprice = monallprice(C)
print("C售货机总交易额数据",C_monallprice)
C_monallprice = C_monallprice.astype(float)

D_monallprice = monallprice(D)
print("D售货机总交易额数据",D_monallprice)
D_monallprice = D_monallprice.astype(float)

E_monallprice = monallprice(E)
print("E售货机总交易额数据",E_monallprice)
E_monallprice = E_monallprice.astype(float)

dayy = ["31", "28", "31","30", "31", "30","31", "31", "30","31", "30", "31"]

all_monallprice =pd.DataFrame({"月份":da,"A售货机":A_monallprice[0],"B售货机":B_monallprice[0],"C售货机":C_monallprice[0],"D售货机":D_monallprice[0],"E售货机":E_monallprice[0]}) #组成一个dataframe
print(all_monallprice)
all_monpriceeq =pd.DataFrame({"月份":da,"A售货机":A_monallprice[0],"B售货机":B_monallprice[0],"C售货机":C_monallprice[0],"D售货机":D_monallprice[0],"E售货机":E_monallprice[0],"天数":dayy}) #组成一个dataframe
print(all_monpriceeq)



## 绘制折线图
plt.plot(all_monallprice["月份"],all_monallprice["A售货机"],'bs-',
       all_monallprice["月份"],all_monallprice["B售货机"],'ro-.',
       all_monallprice["月份"],all_monallprice["C售货机"],'gH--',
       all_monallprice["月份"],all_monallprice["D售货机"],'go-',
       all_monallprice["月份"],all_monallprice["E售货机"],'yo-')## 绘制折线图
plt.xlabel('月份')## 添加横轴标签
plt.ylabel('总交易额（元')## 添加y轴名称
#plt.xticks(range(0,12,1))
plt.title('每台售货机每月总交易额折线图')## 添加图表标题
plt.legend(["A售货机","B售货机","C售货机","D售货机","E售货机"],loc='best')
plt.savefig('2017每台售货机每月总交易额折线图.png')
plt.show()
print("月总交易额",all_monallprice)
#all_monallprice.to_csv('2017年各售货机每月总交易额数据.csv', encoding='gbk')

print("--------------------结束结束-------------------------------")

















