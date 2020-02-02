# -*- coding: utf-8 -*-

'''
    【簡介】
	ui轉換成py的轉換工具
     
'''

import os 
import os.path 

# UI檔案所在的路徑
dir = './'  

# 列出目錄下的所有ui檔案
def listUiFile(): 
	list = []
	files = os.listdir(dir)  
	for filename in files:  
		#print( dir + os.sep + f  )
		#print(filename)
		if os.path.splitext(filename)[1] == '.ui':
			list.append(filename)
	
	return list

# 把副檔名為ui的檔案更名為.py的檔案名稱
def transPyFile(filename): 
	return os.path.splitext(filename)[0] + '.py' 

# 呼叫系統命令把ui轉換成py
def runMain():
	list = listUiFile()
	for uifile in list :
		pyfile = transPyFile(uifile)
		cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)  
		#print(cmd)
		os.system(cmd)

###### 程式的主入口		
if __name__ == "__main__":  	
	runMain()
