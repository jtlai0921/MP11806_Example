# -*- coding: utf-8 -*-

'''
    【簡介】
	 設定視窗背景圖片
    
'''

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QPalette , QBrush , QPixmap


app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("設定視窗背景圖片") 
palette	= QPalette()
palette.setBrush(QPalette.Background,QBrush(QPixmap("./images/python.jpg")))
win.setPalette(palette)  
#當背景圖片的寬度和高度大於視窗的寬度和高度時
#win.resize(460,  255 )  

#當背景圖片的寬度和高度小於視窗的寬度和高度時
win.resize(800,  600 )  

win.show()
sys.exit(app.exec_())
