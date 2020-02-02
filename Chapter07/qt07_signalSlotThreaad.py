# -*- coding: utf-8 -*-

'''
    【簡介】
    多執行緒更新資料，pyqt5介面即時刷新範例 

'''

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime 
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
import time
import sys

class BackendThread(QThread):
    # 透過類別成員物件定義訊號物件  
	update_date = pyqtSignal(str)
	
    # 處理邏輯
	def run(self):
		while True:
			data = QDateTime.currentDateTime()
			currTime = data.toString("yyyy-MM-dd hh:mm:ss")
			self.update_date.emit( str(currTime) )
			time.sleep(1)

class Window(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setWindowTitle('PyQt 5介面即時更新範例')
		self.resize(400, 100)
		self.input = QLineEdit(self)
		self.input.resize(400, 100)
		self.initUI()

	def initUI(self):
        # 建立執行緒  
		self.backend = BackendThread()
        # 連結訊號 
		self.backend.update_date.connect(self.handleDisplay)
        # 開始執行緒  
		self.backend.start()
    
    # 輸出目前時間到文字方塊
	def handleDisplay(self, data):
		self.input.setText(data)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Window()
	win.show() 
	sys.exit(app.exec_())
