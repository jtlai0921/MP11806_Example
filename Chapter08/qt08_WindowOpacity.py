# -*- coding: utf-8 -*-

'''
    【簡介】
	設定視窗的透明度
    
'''

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("設定視窗的透明度") 
    win.setWindowOpacity(0.5)
    
    win.resize(350,  250) 
    win.show()
    sys.exit(app.exec_())

