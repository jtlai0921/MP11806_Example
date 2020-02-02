# -*- coding: utf-8 -*- 

'''
    【簡介】
	QWebEngineView開啟本地網頁範例 
  
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):

	def __init__(self ):
		super(QMainWindow, self).__init__()
		self.setWindowTitle('載入並顯示本地網頁範例')
		self.setGeometry(5, 30, 755, 530)
		self.browser = QWebEngineView()   
        # 載入本地網頁
		url = r'c:/temp/PyQt5-master/Chapter05/index.html'
		self.browser.load( QUrl( url ))	
		self.setCentralWidget(self.browser)

if __name__ == '__main__':
	app = QApplication(sys.argv)       
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
