# -*- coding: utf-8 -*- 

'''
    【簡介】
	PyQT5開啟外部網頁範例 
  
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):

	def __init__(self ):
		super(QMainWindow, self).__init__()
		self.setWindowTitle('開啟外部網頁範例')
		self.setGeometry(5, 30, 1355, 730)
		self.browser = QWebEngineView()
        # 載入外部網頁
		# self.browser.load(QUrl('http://www.cnblogs.com/wangshuo1'))
		self.browser.load(QUrl('https://translate.google.com.tw/?hl=zh-TW'))
		self.setCentralWidget(self.browser)

if __name__ == '__main__':
	app = QApplication(sys.argv)     
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
