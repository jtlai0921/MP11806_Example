# -*- coding: utf-8 -*-

'''
    【簡介】
    自訂訊號和內置槽範例

'''

from PyQt5.QtWidgets import  QApplication ,QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal
import sys

class WinForm(QWidget):
	button_clicked_signal = pyqtSignal() # 自訂訊號，不帶參

	def __init__(self, parent = None):
		super(WinForm,self).__init__(parent)
		self.resize(330,  50 ) 
		self.setWindowTitle('自訂訊號和內置槽範例')

		btn = QPushButton('關閉', self)
		# 連接訊號/槽
		btn.clicked.connect(self.btn_clicked) 
		# 接收訊號，連接到槽
		self.button_clicked_signal.connect(self.close) 
		
	def btn_clicked(self):
		# 發送無參數的自訂訊號
		self.button_clicked_signal.emit() 
                
if __name__ == '__main__':  
	app = QApplication(sys.argv)
	win = WinForm()
	win.show()
	sys.exit(app.exec_())
