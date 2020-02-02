# -*- coding: utf-8 -*-

'''
    【簡介】
    重新實現訊號槽函數 範例

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class WinForm(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  
		self.setGeometry(300, 300, 400, 300)
		self.setWindowTitle('重新實現訊號槽函數範例')

	# 重新實現訊號槽函數
	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.close()

		elif e.key() == Qt.Key_Alt:
			self.setWindowTitle('按下Alt鍵')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()                      
    sys.exit(app.exec_())
