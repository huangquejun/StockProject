'''
Created on 2016年9月24日

@author: Administrator
'''
import tushare as ts
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import time
pymysql.install_as_MySQLdb()

engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8')
dfHistory = pd.read_sql('SELECT code,min(date) time FROM stockdata.stock_history group by code;', engine)
dfHistory = dfHistory.set_index('code')
print(dfHistory)
# stockData = pd.read_sql('SELECT * FROM stockdata.stock_basics where timeToMarket<>0;', engine)
# stockData = stockData.set_index('code')
# 
# for code in dfHistory.index:
#     tmpDate = dfHistory['time'][code]
#     print(tmpDate)
#     earlyDate = tmpDate[0:10]
#     print(earlyDate)
#     tmp =stockData['timeToMarket'][code]
#     timeArray = time.strptime(tmp, "%Y%m%d")
#     stockDate = time.strftime("%Y-%m-%d", timeArray)