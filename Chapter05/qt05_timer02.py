# -*- coding: utf-8 -*- 
'''
    【簡介】
	PyQT5中QTimer關閉程式範例
 
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	label = QLabel("<font color=red size=128><b>Hello PyQt，視窗會在10秒後消失！</b></font>")
	
	# 無邊框視窗
	label.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
	label.show()

    # 設定10秒後自動退出
	QTimer.singleShot(10000, app.quit) 
	sys.exit(app.exec_())
