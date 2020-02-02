# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQT5中QDockWidget範例
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DockDemo(QMainWindow):
	def __init__(self, parent=None):
		super(DockDemo, self).__init__(parent)
		layout = QHBoxLayout()
		bar=self.menuBar()
		file=bar.addMenu("File")
		file.addAction("New")
		file.addAction("Save")
		file.addAction("Quit")
		self.items = QDockWidget("Dockable", self)
		self.listWidget = QListWidget()
		self.listWidget.addItem("item1")
		self.listWidget.addItem("item2")
		self.listWidget.addItem("item3")
		self.items.setWidget(self.listWidget)
		self.items.setFloating(False)
		self.setCentralWidget(QTextEdit())
		self.addDockWidget(Qt.RightDockWidgetArea, self.items)
		self.setLayout(layout)
		self.setWindowTitle("Dock範例")
					
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = DockDemo()
	demo.show()
	sys.exit(app.exec_())
