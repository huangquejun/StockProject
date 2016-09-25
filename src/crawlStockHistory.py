'''
Created on 2016年9月23日

@author: Administrator
'''
import tushare as ts
import pymysql
import time
import pandas as pd
from sqlalchemy.types import String
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
#读取股票基本数据
engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8')
stockData = pd.read_sql('SELECT * FROM stockdata.stock_basics where timeToMarket<>0;', engine)
stockData = stockData.set_index('code')
engine.execute("drop table stock_history;")
loop = 0
for stockCode in stockData.index:   
    if loop == 2: break
    print(loop)
    tmp =stockData['timeToMarket'][stockCode]
    timeArray = time.strptime(tmp, "%Y%m%d")
    stockDate = time.strftime("%Y-%m-%d", timeArray)
    loop+= 1
    print(stockCode)
    print(stockDate)
    df = ts.get_h_data(stockCode,stockDate,'2016-09-23',drop_factor = False)
    df['code'] = stockCode
    df = df.set_index([df.index,df.code])
    del df['code']
    df.to_sql('stock_history',engine,if_exists='append',dtype={'code': String(10),'date': String(20)})
