# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中QMessage範例
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WinForm( QWidget):  
	def __init__(self):  
		super(WinForm,self).__init__()  
		self.setWindowTitle("QMessageBox範例")  
		self.resize(300, 100)              
		self.myButton = QPushButton(self)    
		self.myButton.setText("點擊彈出訊息對話方塊")  
		self.myButton.clicked.connect(self.msg)  

	def msg(self):  
        # 使用infomation訊息對話方塊
		reply = QMessageBox.information(self, "標題", "訊息文字", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )
		
		# reply = QMessageBox.information(self, "標題", "訊息對話方塊文字", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )
		# reply = QMessageBox.question(self, "標題", "提問框訊息文字", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )
		# reply = QMessageBox.warning(self, "標題", "警告框訊息文字", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes ) 
		# reply = QMessageBox.critical(self, "標題", "嚴重錯誤對話方塊訊息文字", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )
		# reply = QMessageBox.about(self, "標題", "關於對話方塊" )
		print( reply )
		
if __name__ == '__main__':
	app= QApplication(sys.argv)    
	demo = WinForm()  
	demo.show() 
	sys.exit(app.exec_())
