# -*- coding: utf-8 -*-

'''
    【簡介】
	 設定視窗樣式
     
'''

from PyQt5.QtCore import Qt 
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication

class MainWindow(QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.resize(477, 258) 
		self.setWindowTitle("設定無邊框視窗樣式範例") 
		# 設定無邊框視窗樣式
		self.setWindowFlags( Qt.SubWindow )
		self.setObjectName("MainWindow") 
		self.setStyleSheet("#MainWindow{border-image:url(images/python.jpg);}")
       
if __name__ == "__main__": 
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
