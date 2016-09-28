'''
Created on 2016年9月28日

@author: Administrator
'''
import tushare as ts
import pymysql
import time
import os
import pandas as pd
from sqlalchemy.types import String
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
#读取股票基本数据
engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8')
stockData = pd.read_sql('SELECT * FROM stockdata.stock_basics where timeToMarket<>0;', engine)
stockData = stockData.set_index('code')
now = '2016-09-27'
print(now)
data_stockHistory = 'd:/crawlData/stockDataAll.csv'
data_stockMark = 'd:/crawlData/stockDataAll_mark.csv'
isExists = os.path.exists(data_stockMark)
flag =False

if os.path.exists(data_stockHistory):
    historyFileName = open(data_stockHistory, 'a')

else:
    historyFileName = open(data_stockHistory, 'a')
    flag =True

if isExists:

    stockMark = pd.read_csv(data_stockMark,dtype={'code': str, 'date': str})
    stockMark = stockMark.set_index('code')
    f= open(data_stockMark,'a')
else:
    f= open(data_stockMark,'a')
    f.write('code,date\n')
    f.flush()
    stockMark = pd.DataFrame()

for stockCode in stockData.index:
    tmp =stockData['timeToMarket'][stockCode]
    timeArray = time.strptime(tmp, "%Y%m%d")
    stockDate = time.strftime("%Y-%m-%d", timeArray)
    print(stockCode)
    print(stockDate)
    if stockCode in stockMark.index : continue
    df = ts.get_h_data(stockCode,stockDate,now,drop_factor = False)
    df['code'] = stockCode
    df = df.set_index([df.index,df.code])
    del df['code']
    if flag:
        df.to_csv(historyFileName)
        f.write(stockCode+','+now+'\n')
        f.flush()
        flag = False
    else:

        start = time.clock()
        df.to_csv(historyFileName, mode='a', header=None)
        f.write(stockCode+','+now+'\n')
        f.flush()
        end = time.clock()
        print("execute: %f s" % (end - start))
        
f.close()
historyFileName.close()
