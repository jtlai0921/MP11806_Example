# -*- coding: utf-8 -*-

'''
    【簡介】
    內建訊號和自訂槽函數範例


'''

from PyQt5.QtWidgets import *
import sys

class Winform(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent)
		self.setWindowTitle('內建訊號和自訂槽函數範例')
		self.resize(330,  50 ) 
		btn = QPushButton('關閉', self)		
		btn.clicked.connect(self.btn_close) 

	def btn_close(self):
		# 自訂槽函數
		self.close()
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Winform()
	win.show()
	sys.exit(app.exec_())
