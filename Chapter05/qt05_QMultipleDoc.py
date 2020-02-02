# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQT5中QMdiArea範例
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
            
class MainWindow(QMainWindow):
	count=0
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.mdi = QMdiArea()
		self.setCentralWidget(self.mdi)
		bar=self.menuBar()
		file=bar.addMenu("File")
		file.addAction("New")
		file.addAction("Cascade")
		file.addAction("Tiled")
		file.triggered[QAction].connect(self.windowaction)
		self.setWindowTitle("MDI Demo")

	def windowaction(self, q): 
		print( "triggered")
		
		if q.text()=="New":
			MainWindow.count=MainWindow.count+1
			sub=QMdiSubWindow()
			sub.setWidget(QTextEdit())
			sub.setWindowTitle("subwindow"+str(MainWindow.count))
			self.mdi.addSubWindow(sub)
			sub.show()
		if q.text()=="Cascade":
			self.mdi.cascadeSubWindows()
		if q.text()=="Tiled":
			self.mdi.tileSubWindows()
             	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = MainWindow()
	demo.show()
	sys.exit(app.exec_())
