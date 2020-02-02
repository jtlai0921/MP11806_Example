# -*- coding: utf-8 -*- 

'''
    【簡介】
	QWebView開啟網頁範例 
  
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
		self.setGeometry(5, 30, 1355, 730)
		self.browser = QWebEngineView()
        #1 載入html標記
		self.browser = QWebEngineView()
		self.browser.setHtml('''
		<!DOCTYPE html>
		<html>
			<head>
				<meta charset="UTF-8">
				<title></title>
			</head>
			<body>
				<h1>Hello PyQt5</h1>
				<h1>Hello PyQt5</h1>
                <h1>hello PyQt5</h1>
                <h1>hello PyQt5</h1>
                <h1>hello PyQt5</h1>
                <h1>Hello PyQt5</h1>
                
			</body>
		</html>

		'''
		)
		
		self.setCentralWidget(self.browser)

if __name__ == '__main__':
	app = QApplication(sys.argv)
    
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
