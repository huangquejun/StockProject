# coding:utf8
'''
Created on 2016年9月19日

@author: Administrator
'''
import urllib.request
import json
url = 'http://shuorel.com/ws/share/valuation/v1/601398?dates=2015-3-5,2016-3-5'
stdout=urllib.request.urlopen(url)
htmlCode = stdout.read().decode('utf-8')
print(htmlCode.splitlines())
jsonData = json.loads(htmlCode)

print(type(jsonData['data']))
print(jsonData['data'])