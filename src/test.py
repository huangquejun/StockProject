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

# engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8')
# dfHistory = pd.read_sql('SELECT code,min(date) time FROM stockdata.stock_history group by code;', engine)
# dfHistory = dfHistory.set_index('code')
# print(dfHistory)
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

df1 = ts.get_h_data('000001',start='2016-09-26', end='2016-09-26', index=True)
df2 = ts.get_h_data('000001', start='2016-09-23', end='2016-09-23',index=True)
df3 = ts.get_h_data('000001', start='2016-09-23', end='2016-09-23',index=True)
tmp = [df1,df2,df3]
result = pd.concat(tmp)
result = result.drop_duplicates()
print(result)