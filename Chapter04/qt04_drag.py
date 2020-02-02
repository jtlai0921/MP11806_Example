# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中Drag and Drop範例
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
   
class Combo(QComboBox):

	def __init__(self, title, parent):
		super(Combo, self).__init__( parent)
		self.setAcceptDrops(True)
		
	def dragEnterEvent(self, e):
		print( e)
		if e.mimeData().hasText():
			e.accept()
		else:
			e.ignore() 

	def dropEvent(self, e):
		self.addItem(e.mimeData().text()) 
		
class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		lo = QFormLayout()
		lo.addRow(QLabel("請把左邊的文字拖曳到右邊的下拉式清單中"))
		edit = QLineEdit()
		edit.setDragEnabled(True)
		com = Combo("Button", self)
		lo.addRow(edit,com)
		self.setLayout(lo)
		self.setWindowTitle('簡單的拖曳範例')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example() 
	ex.show()
	sys.exit(app.exec_())
