'''
Created on 2016年9月26日

@author: Administrator
'''
import tushare as ts
import time
now = time.strftime('%H-%M-%S',time.localtime(time.time()))
print(now)
tmpMoningS = '9:30:00' 
tmpMoningE = '11:30:00' 
tmpNoonS = '13:00:00' 
tmpNoonE = '15:00:00'
MoningS = time.strptime(tmpMoningS,'%H:%M:%S')
MoningE = time.strptime(tmpMoningE,'%H:%M:%S')
NoonS = time.strptime(tmpNoonS,'%H:%M:%S')
NoonE = time.strptime(tmpNoonE,'%H:%M:%S')
print(MoningS)
# df = ts.get_index()
# print(df)
