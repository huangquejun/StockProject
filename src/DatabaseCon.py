# coding:utf8
'''
Created on 2016年9月15日

@author: Administrator
'''
import tushare as ts
import pymysql
from sqlalchemy.types import String
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
df=ts.get_stock_basics()
engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8',echo=True)
df.to_sql('stock_basics',engine,if_exists='replace',dtype={'code': String(10),'timeToMarket': String(10)})
engine.execute("update stock_basics set name=replace(name,' ','');")
