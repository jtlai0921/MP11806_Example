#!/usr/bin/env python3

'''
    【簡介】
	PyQT5中QTreeView範例
   
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
        
if __name__ == '__main__':
	app =  QApplication(sys.argv)
	#Windows系統提供的模式
	model = QDirModel()
	#建立一個QTreeView控制項  
	tree = QTreeView()
	#為控制項增加模式
	tree.setModel(model)
	tree.setWindowTitle( "QTreeView範例" )
	tree.resize(640, 480)
	tree.show()
	sys.exit(app.exec_())
