# -*- coding: utf-8 -*-

'''
    【簡介】
     範例

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

class CustWin( QWidget):  
	# 宣告帶一個清單類型參數的訊號
	signal1 = pyqtSignal(list)
	
	# 宣告帶一個字典類型參數的訊號
	signal2 = pyqtSignal(dict)

	# 宣告帶一個元祖類型參數的訊號
	signal3 = pyqtSignal(tuple)
	
	def __init__(self, parent=None):  
		super(CustWin, self).__init__(parent)  
		btnLayout = QHBoxLayout()  
		mainLayout = QVBoxLayout()  
		  
		btn1 = QPushButton("發射帶參數的訊號")  
		btnLayout.addStretch()  
		btnLayout.addWidget(btn1)  		
		mainLayout.addLayout(btnLayout)  
		self.setLayout(mainLayout)  
		btn1.clicked.connect(self.emitDictSign)  

	def emitDictSign(self):  
		self.signal1.emit([1,2,3,4])  
		self.signal2.emit({"monday":1, "tuesday":2, "Wednesday":3})  
		self.signal3.emit( (1,'2',('learn', 'python') ))  
	  
class MainWin( QWidget):  
	def __init__(self, parent=None):  
		super(MainWin, self).__init__(parent)
		self.setWindowTitle('控制項中的訊號發射參數')		
		widget = CustWin(self)  
		mainLayout = QVBoxLayout()  
		mainLayout.addWidget(widget)  
		self.setLayout(mainLayout)   
		widget.signal1.connect(self.displayDict)  
		widget.signal2.connect(self.displayList)  
		widget.signal3.connect(self.displayTuple) 
		
	def displayDict(self, data):  
		print( '--- displayDict ---' ) 
		print( type(data ) )  

	def displayList(self,data):
		print( '--- displayList ---' ) 
		print( data)  

	def displayTuple(self,data):
		print( '--- displayTuple ---' ) 
		print( data)  
		
if __name__ == '__main__':   
	app = QApplication(sys.argv)  
	win = MainWin()  
	win.show()  
	sys.exit(app.exec_())  
