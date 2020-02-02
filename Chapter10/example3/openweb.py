# -*- coding: utf-8 -*-

import sys
import time

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *

class WebView(QWebEngineView):
     def __init__(self ):
        super(WebView, self).__init__()
        # 需改成自己所需的頁面網址
        url = 'http://localhost:8080/jsp2_1/ch02/author.htm'
        # url = 'http://www.cnblogs.com/wangshuo1/p/6707631.html'
		
        self.load( QUrl( url ) )             
        self.show()
        QTimer.singleShot(1000*5 , self.close)  
		

if __name__ == '__main__':   
	app = QApplication(sys.argv)
	web = WebView()  
	print('### exec succeed !')
	sys.exit(app.exec_())  	
