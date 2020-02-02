# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中QDialog範例
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DialogDemo( QMainWindow ):

	def __init__(self, parent=None):
		super(DialogDemo, self).__init__(parent) 		
		self.setWindowTitle("Dialog 範例")
		self.resize(350,300)
    
		self.btn = QPushButton( self)
		self.btn.setText("彈出對話方塊")  
		self.btn.move(50,50)		
		self.btn.clicked.connect(self.showdialog)  
                
	def showdialog(self ):
		dialog = QDialog()
		btn = QPushButton("ok", dialog )
		btn.move(50,50)
		dialog.setWindowTitle("Dialog")
		dialog.setWindowModality(Qt.ApplicationModal)
		dialog.exec_()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = DialogDemo()
	demo.show()
	sys.exit(app.exec_())
