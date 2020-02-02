# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中QStatusBar範例
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StatusDemo(QMainWindow):
	def __init__(self, parent=None):
		super(StatusDemo, self).__init__(parent)
		bar = self.menuBar()
		file = bar.addMenu("File")
		file.addAction("Show")
		file.triggered[QAction].connect(self.processTrigger)
		self.setCentralWidget(QTextEdit())
		self.statusBar= QStatusBar() 
		self.setWindowTitle("QStatusBar範例")
		self.setStatusBar(self.statusBar)
	
	def processTrigger(self,q):
		if (q.text()=="Show"):
			self.statusBar.showMessage(q.text()+" 功能表選項被點擊了",5000)
	    
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = StatusDemo()
	demo.show()
	sys.exit(app.exec_())
