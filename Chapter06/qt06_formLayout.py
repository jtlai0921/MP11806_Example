# -*- coding: utf-8 -*-
 
'''
    【簡介】
    表單佈局管理範例
    
'''

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QFormLayout , QLineEdit, QLabel

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("表單佈局管理範例") 
		self.resize(400, 100)  
         
		fromlayout = QFormLayout()
		labl1 = QLabel("標籤1")
		lineEdit1 = QLineEdit()
		labl2 = QLabel("標籤2")
		lineEdit2 = QLineEdit()
		labl3 = QLabel("標籤3")
		lineEdit3 = QLineEdit()

		fromlayout.addRow(labl1, lineEdit1)
		fromlayout.addRow(labl2, lineEdit2)
		fromlayout.addRow(labl3, lineEdit3)
		
		self.setLayout(fromlayout)   
  
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
