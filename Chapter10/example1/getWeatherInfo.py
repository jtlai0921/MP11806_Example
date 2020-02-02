# -*- coding: utf-8 -*-
'''
    【簡介】
	查詢城市天氣資訊
    
'''

import requests

#rep = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
rep = requests.get('http://www.weather.com.cn/data/sk/101340101.html')

rep.encoding = 'utf-8'

print('返回結果：%s' % rep.json() ) 
print('城市：%s' % rep.json()['weatherinfo']['city'] )
print('風向：%s' % rep.json()['weatherinfo']['WD'] )
print('溫度：%s' % rep.json()['weatherinfo']['temp'] + " 度")
print('風力：%s' % rep.json()['weatherinfo']['WS'] )
print('濕度：%s' % rep.json()['weatherinfo']['SD'] )

