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
from wordcloud import WordCloud
from scipy.misc import imread
from pandas import Series, DataFrame
df=pd.read_csv('E:\泰迪\附件1.csv', encoding='gbk')#读取CSV文件
plt.rcParams['font.sans-serif'] = 'SimHei' ## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
df = pd.DataFrame(df)
print("--------------------分割线------------------------------")  
'''#提取各台售货机数据
def machine():
    df
'''


print("--------------------分割线------------------------------")  


#数据清洗
print("未清洗前2017年订单总量为",df.shape[0])
df=df.dropna()#清理缺失值
print("清除缺失值后2017年订单总量为",df.shape[0])

#数据去重
print('drop_duplicates方法去重之前订单总数为：',len(df))

df1 = df["订单号"].drop_duplicates()
print('1111drop_duplicates方法去重之后订单总数为：',len(df1))


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
print("3333看这里看这里，是一样的吗？",NEW_DF.shape)


print("--------------------分组分割线------------------------------") 

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

df2title = df2["商品"]

df2title.to_csv('userdict.txt',encoding='utf-8',index = 0)#保存CSV文件

print("---------------------提取各台售货机数据------------------------------")
#A售货机
A_mac=all_data.loc[all_data['地点']=="A"] #选择表格中“地点”列为A的行
print("A售货机订单数为",A_mac.shape[0])
A_order_drink = A_mac.loc[A_mac['大类']=='饮料']
print("饮料类个数为",A_order_drink.shape[0])

#A_mac.to_csv('A_mac.csv',encoding='gbk')#保存CSV文件

print("---------------------------------------------------")

#B售货机
B_mac=all_data.loc[all_data['地点']=="B"] #选择表格中“地点”列为B的行
print("B售货机订单数为",B_mac.shape[0])
B_order_drink = B_mac.loc[B_mac['大类']=='饮料']
print("饮料类个数为",B_order_drink.shape[0])

print("---------------------------------------------------")

#C售货机
C_mac=all_data.loc[all_data['地点']=="C"] #选择表格中“地点”列为C的行
print("C售货机订单数为",C_mac.shape[0])
C_order_drink = C_mac.loc[C_mac['大类']=='饮料']
print("饮料类个数为",C_order_drink.shape[0])


print("---------------------------------------------------")

#D售货机
D_mac=all_data.loc[all_data['地点']=="D"] #选择表格中“地点”列为D的行
print("D售货机订单数为",D_mac.shape[0])
D_order_drink = D_mac.loc[D_mac['大类']=='饮料']
print("饮料类个数为",D_order_drink.shape[0])


print("---------------------------------------------------")

#E售货机
E_mac=all_data.loc[all_data['地点']=="E"] #选择表格中“地点”列为E的行
print("E售货机订单数为",E_mac.shape[0])
E_order_drink = E_mac.loc[E_mac['大类']=='饮料']
print("饮料类个数为",E_order_drink.shape[0])


print("--------------------提取结束-------------------------------")

def fun(X_order_drink):
    
    #计算不重复值个数
    XX =X_order_drink["商品"].nunique()
    XXX = X_order_drink["商品"].count()
    print("商品类别个数",XX)
    print("商品个数",XXX)
    
    XXXX = X_order_drink["商品"]
    print(XXXX)
    XXXX_list1 = XXXX.value_counts()
    XXXX_list = pd.DataFrame(XXXX_list1)
    XXXX_list=XXXX_list.reset_index(drop=False)#重新设置列索引
    XXXX_list.rename(columns={'index':"饮料类商品", '商品':"销售量"}, inplace = True)
    print("商品销售数据统计",XXXX_list)
    print("--------------------------------------------------")
    
    
    ##画出箱线图图
    plt.figure(figsize=(10,8)) 
    #label1 = ["商品数目"]## 标签1
    pic=(XXXX_list1)
    p=plt.boxplot(pic,notch=True,meanline = True)  
    outlier1 = p['fliers'][0].get_ydata()   ##fliers为异常值的标签 
    plt.title('A售货机销售数据箱线图')
    plt.ylabel('数量')## 添加y轴名称
    plt.show()
    print('销售量数据异常值为：',outlier1)
    print('销售量数据异常值个数为：',len(outlier1))
    print('销售量数据异常值的最大值为：',max(outlier1))
    print('销售量数据异常值的最小值为：',min(outlier1))
    
    Q1=np.percentile(XXXX_list["销售量"],25)
    Q2=np.percentile(XXXX_list["销售量"],50)
    Q3=np.percentile(XXXX_list["销售量"],75)
    print("中位数为",Q2)
    print("分位数3为",Q3)
    
    XXXX_list["标签"] = XXXX_list["销售量"].apply(lambda x : 3 if x >min(outlier1) else 0)

    
    XXXX_list.loc[XXXX_list[(XXXX_list["销售量"]>=Q1)&(XXXX_list["销售量"]<=min(outlier1))].index,["标签"]]='正常'
    XXXX_list.loc[XXXX_list[XXXX_list["销售量"]>=min(outlier1)].index,["标签"]]='热销'
    XXXX_list.loc[XXXX_list[XXXX_list["销售量"]<Q1].index,["标签"]]='滞销'
    
    return XXXX_list

AAAA_list = fun(A_order_drink)

BBBB_list= fun(B_order_drink)

CCCC_list= fun(C_order_drink)

DDDD_list= fun(D_order_drink)

EEEE_list= fun(E_order_drink)

AAAA_list.to_csv('task3-2A.csv',encoding='gbk')#保存CSV文件
BBBB_list.to_csv('task3-2B.csv',encoding='gbk')#保存CSV文件
CCCC_list.to_csv('task3-2C.csv',encoding='gbk')#保存CSV文件
DDDD_list.to_csv('task3-2D.csv',encoding='gbk')#保存CSV文件
EEEE_list.to_csv('task3-2E.csv',encoding='gbk')#保存CSV文件


print("---------------------------------------------------")

import jieba


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r').readlines()]
    return stopwords
def fenci(orderdata,O):
    
    title = orderdata["商品"].values.tolist()
    jieba.load_userdict("userdict.txt")
    #jieba.set_dictionary("userdict.txt")#切换分割词词典
    stopwords = stopwordslist('stopwords.txt')  # 这里加载停用词的路径
    title_s = []
    for line in title:
        title_cut = jieba.lcut(line)
        title_s.append(title_cut)
    
    # 剔除不需要的单词，使用停用表
    
    title_clean = []
    for line in title_s:
        line_clean = []
        for word in line:
            if word not in stopwords:
                line_clean.append(word)
        title_clean.append(line_clean)
    
    # 统计每个词语的个数，先去重
    title_clean_dist = []
    for line in title_clean:
        line_dist = []
        for word in line:
            if word not in line_dist:
                line_dist.append(word)
        title_clean_dist.append(line_dist)
    
    # 将所有词转换为一个list
    allwords_clean_dist = []
    for line in title_clean_dist:
        for word in line:
            allwords_clean_dist.append(word)
    
    # 将所有词语转换数据框
    df_allwords_clean_dist = pd.DataFrame({
        'allwords': allwords_clean_dist
    })
    
    word_count = df_allwords_clean_dist.allwords.value_counts().reset_index()
    word_count.columns = ['word', 'count']
    print(word_count.head())
    
    
    jieba.add_word('100g*5瓶益力多')
    jieba.add_word('农夫果园 (芒果+菠萝+番石榴)')
    
    cut = jieba.cut(str(allwords_clean_dist))
    
    #以空格拼接起来
    result = " ".join(cut)
    # 生成词云
    wc = WordCloud(
            font_path='simhei.ttf',     #字体路劲
            background_color='white',   #背景颜色            
            max_font_size=60,            #字体大小
            min_font_size=10,
            mask=plt.imread('233333333.png'),  #背景图片
            max_words=1000
    )
    wc.generate(result)
    if O == "A":
       wc.to_file('A售货机画像.png')    #图片保存
    if O == "B":
       wc.to_file('B售货机画像.png')
    if O == "C":
       wc.to_file('C售货机画像.png')
    if O == "D":
       wc.to_file('D售货机画像.png')
    if O == "E":
       wc.to_file('E售货机画像.png')
    #显示图片
    plt.figure('售货机画像')   #图片显示的名字
    plt.imshow(wc)
    plt.axis('off')        #关闭坐标
    plt.show()
    #-------换成中间的--------------
    return fenci


#A售货机画像
fenci(A_order_drink,"A")
#B售货机画像
fenci(B_order_drink,"B")
  
#C售货机画像
fenci(C_order_drink,"C")
    
#D售货机画像
fenci(D_order_drink,"D")
    
fenci(E_order_drink,"E")
#E售货机画像


print("--------------------结束结束-------------------------------")



