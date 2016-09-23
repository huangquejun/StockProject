'''
Created on 2016年9月23日

@author: Administrator
'''
import urllib.request
import json
html = urllib.request.urlopen(r'http://shuorel.com/ws/share/valuation/v1/601398?date=2016-3-5')
data = html.read().decode('utf-8')
print(data)
jsondata = json.loads(data)
print(jsondata['data'])
print(jsondata.keys())
print(len(jsondata['data']))
print(type(jsondata['data']))
for num in jsondata['data']:
    print(num['code'])
# [1]['pe_ratio']