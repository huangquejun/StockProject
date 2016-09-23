'''
Created on 2016年9月23日

@author: Administrator
'''
import tushare as ts
import pymysql
import pandas as pd
from sqlalchemy.types import String
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
#读取股票基本数据
engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8',echo=True)
stockData = pd.read_sql('SELECT * FROM stockdata.stock_basics where timeToMarket<>0;', engine)
stockData = stockData.set_index('code')

for stockCode in stockData.index:
    stockTime = stockData['timeToMarket'][stockCode]
    print(type(stockTime))
    break
# df = ts.get_h_data('000001','2016-09-01','2016-09-23')
# df['code'] = '000001'
# df = df.set_index([df.index,df.code])
# del df['code']
# engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8',echo=True)
# df.to_sql('stock_history',engine,if_exists='append',dtype={'code': String(10)})
# # print(df)