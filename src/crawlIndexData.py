'''
Created on 2016年9月26日

@author: Administrator
'''
import tushare as ts
import time

# now = time.strftime("%H:%M:%S")
# nowtime = time.strptime(now,'%H:%M:%S')

tmpnow = '9:35:15'
now = time.strptime(tmpnow,'%H:%M:%S')
tmpMoningS = '9:30:00' 
tmpMoningE = '11:30:00' 
tmpNoonS = '13:00:00' 
tmpNoonE = '15:00:00'
MoningS = time.strptime(tmpMoningS,'%H:%M:%S')
MoningE = time.strptime(tmpMoningE,'%H:%M:%S')
NoonS = time.strptime(tmpNoonS,'%H:%M:%S')
NoonE = time.strptime(tmpNoonE,'%H:%M:%S')
while True:
    if(now > NoonE):
        print('now > NoonE')
        break
    if(now < MoningS or (now >MoningE and now <MoningE)):
        print('second tiaojian')
        continue
    print('交易时间')
    time.sleep(5)
     

