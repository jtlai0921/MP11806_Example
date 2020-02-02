# -*- coding: utf-8 -*- 
'''
    【簡介】
	PyQT5中QThread範例
 
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
    
global sec
sec=0

class WorkThread(QThread):
	trigger = pyqtSignal()
	def __int__(self):
		super(WorkThread,self).__init__()

	def run(self):
		for i in range(2000000000):
			pass
		
		# 迴圈完畢後發射訊號
		self.trigger.emit()        

def countTime():
	global  sec
	sec += 1
	# LED顯示數字+1
	lcdNumber.display(sec)          

def work():
	# 計時器每秒計數
	timer.start(1000)   
	# 計時開始
	workThread.start()       
	# 當收到迴圈完畢的訊號時，停止計數
	workThread.trigger.connect(timeStop)  

def timeStop():
	timer.stop()
	print("執行結束，耗時：",lcdNumber.value())
	global sec
	sec=0

if __name__ == "__main__":  	
	app = QApplication(sys.argv) 
	top = QWidget()
	top.resize(300,120)
    
	# 垂直佈局類別QVBoxLayout
	layout = QVBoxLayout(top) 
    # 增加一個顯示面板
	lcdNumber = QLCDNumber()             
	layout.addWidget(lcdNumber)
	button = QPushButton("測試")
	layout.addWidget(button)

	timer = QTimer()
	workThread = WorkThread()

	button.clicked.connect(work)
    # 每次計時結束，觸發countTime
	timer.timeout.connect(countTime)      

	top.show()
	sys.exit(app.exec_())
