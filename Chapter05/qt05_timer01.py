# -*- coding: utf-8 -*- 
'''
    【簡介】
	PyQT5中QTimer範例
 
  
'''

from PyQt5.QtWidgets import QWidget,  QPushButton ,  QApplication ,QListWidget,  QGridLayout , QLabel
from PyQt5.QtCore import QTimer ,QDateTime
import sys 

class WinForm(QWidget):  
	
	def __init__(self,parent=None): 
		super(WinForm,self).__init__(parent) 
		self.setWindowTitle("QTimer demo")
		self.listFile= QListWidget() 
		self.label = QLabel('顯示目前時間')
		self.startBtn = QPushButton('開始') 
		self.endBtn = QPushButton('結束') 
		layout = QGridLayout(self) 

        # 初始化計時器
		self.timer = QTimer(self)
        # showTime()方法
		self.timer.timeout.connect(self.showTime)
		
		layout.addWidget(self.label,0,0,1,2)   
		layout.addWidget(self.startBtn,1,0) 
		layout.addWidget(self.endBtn,1,1) 		
		
		self.startBtn.clicked.connect( self.startTimer) 
		self.endBtn.clicked.connect( self.endTimer) 
				
		self.setLayout(layout)   
		
	def showTime(self): 
		# 取得系統現在的時間
		time = QDateTime.currentDateTime() 
		# 設定系統時間顯示格式
		timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd");
		# 在標籤上顯示時間
		self.label.setText( timeDisplay ) 

	def startTimer(self): 
        # 設定時間間隔，並啟動計時器
		self.timer.start(1000)
		self.startBtn.setEnabled(False)
		self.endBtn.setEnabled(True)

	def endTimer(self): 
		self.timer.stop()
		self.startBtn.setEnabled(True)
		self.endBtn.setEnabled(False)
		
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
