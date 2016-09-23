# coding:utf8
'''
Created on 2016年9月22日

@author: Administrator
'''
import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8',echo=True)
df = pd.read_sql('select * from stock_basics;', engine)
df = df.set_index('code')

