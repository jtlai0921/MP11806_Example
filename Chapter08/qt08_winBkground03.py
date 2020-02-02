# -*- coding: utf-8 -*-

'''
    【簡介】
	設定視窗背景顏色
    
'''

from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget, QVBoxLayout , QPushButton, QMainWindow
from PyQt5.QtGui import QPalette , QBrush , QPixmap
from PyQt5.QtCore import Qt 
import sys
	
app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("設定視窗背景顏色")
win.resize(350,  250)
palette	= QPalette()
palette.setColor(QPalette.Background, Qt.red)
win.setPalette(palette)
win.show()
sys.exit(app.exec_())
