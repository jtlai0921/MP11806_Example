# -*- coding: utf-8 -*- 

'''
    【簡介】
	QWebView中網頁呼叫JavaScript 
  
'''

from PyQt5.QtWidgets  import QApplication , QWidget , QVBoxLayout 
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  
from MySharedObject  import MySharedObject
from PyQt5.QtWebChannel import  QWebChannel 
import sys


# 建立一個應用程式實例
app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('Web頁面的JavaScript與QWebEngineView互動範例')

# 建立一個垂直佈局器
layout = QVBoxLayout()
win.setLayout(layout)

# 建立一個QWebEngineView物件
view =  QWebEngineView()
htmlUrl = 'http://127.0.0.1:8080/pyqt5/index.html'
view.load( QUrl( htmlUrl ))

# 建立一個QWebChannel物件，用來傳遞pyqt參數到JavaScript
channel =  QWebChannel( )
myObj = MySharedObject()   
channel.registerObject( "bridge", myObj )  
view.page().setWebChannel(channel)
 
# 將QWebView和button載入layout佈局
layout.addWidget(view)
           
# 顯示視窗和執行
win.show()
sys.exit(app.exec_())
