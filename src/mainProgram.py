'''
Created on 2016年9月24日

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

def createStockData(stockCode,timeToMarket,nowUpdateTime):
    pass

def updateStockDate(stockCode,lastUpdateTime,nowUpdateTime):
    pass

def getAndStoreLatestStockData():
    stockBasicData=ts.get_stock_basics()
    engine = create_engine('mysql://root:iloveyou@127.0.0.1/stockdata?charset=utf8',echo=True)
    stockBasicData.to_sql('stock_basics',engine,if_exists='replace',dtype={'code': String(10),'timeToMarket': String(10)})
    engine.execute("update stock_basics set name=replace(name,' ','');")
    return stockBasicData

def getStockDataBookMark():
    pass

if __name__ == "__main__":
    start = time.clock()
    print(getAndStoreLatestStockData())
    end = time.clock()
    print("execute: %f s" % (end - start))