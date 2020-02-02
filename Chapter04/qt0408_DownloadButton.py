# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中QButton範例
    
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		layout = QVBoxLayout()

		self.btn4= QPushButton("&Download")
		self.btn4.setDefault(True)
		self.btn4.clicked.connect(lambda:self.whichbtn(self.btn4))
		layout.addWidget(self.btn4)
		self.setWindowTitle("Button demo")
		
		self.setLayout(layout)         


	def btnstate(self):
		if self.btn1.isChecked():
			print("button pressed" ) 
		else:
			print("button released" ) 

	def whichbtn(self,btn):
		print("clicked button is " + btn.text() ) 

if __name__ == '__main__':
	app = QApplication(sys.argv)
	btnDemo = Form()
	btnDemo.show()
	sys.exit(app.exec_())


