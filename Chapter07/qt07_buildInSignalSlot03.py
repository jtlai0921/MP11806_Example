# -*- coding: utf-8 -*-

'''
    【簡介】
    自訂訊號和內建槽函數範例


'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys

class Winform(QWidget):
	# 自訂訊號，沒有參數
	button_clicked_signal = pyqtSignal()

	def __init__(self,parent=None):
		super().__init__(parent)
		self.setWindowTitle('自訂訊號和內建槽函數範例')
		self.resize(330,  50 ) 
		btn = QPushButton('關閉', self)
		# 連接訊號與槽函數
		btn.clicked.connect(self.btn_clicked)
		# 接收訊號，連接到槽
		self.button_clicked_signal.connect(self.close) 

	def btn_clicked(self):
		# 發送自訂訊號，無參數
		self.button_clicked_signal.emit()
		                    		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Winform()
	win.show()
	sys.exit(app.exec_())
