# coding:utf8
'''
Created on 2016年9月22日

@author: Administrator
'''
import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
# import time
engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8')
df = pd.read_sql('select * from stock_basics;', engine)
df = df.set_index('code')

print(df['timeToMarket']['600908'])
# timeArray = time.strptime(str(df['timeToMarket']['600908']), "%Y%m%d")
# otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
# print(type(otherStyleTime))