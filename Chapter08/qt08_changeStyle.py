# -*- coding: utf-8 -*-

'''
    【簡介】
     視窗樣式範例
    
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore 
from PyQt5.QtGui  import *

class AppWidget( QWidget):
	def __init__(self, parent=None):
		super(AppWidget, self).__init__(parent)
		self.setWindowTitle("視窗樣式範例")
		horizontalLayout =  QHBoxLayout()
		self.styleLabel =  QLabel("設定樣式：")
		self.styleComboBox =  QComboBox()
		# 從QStyleFactory增加styles
		self.styleComboBox.addItems( QStyleFactory.keys())
		# 選擇目前視窗樣式
		index = self.styleComboBox.findText(
					 QApplication.style().objectName(),
					QtCore.Qt.MatchFixedString)
		# 設定目前視窗樣式
		self.styleComboBox.setCurrentIndex(index)
		# 透過comboBox選擇視窗樣式
		self.styleComboBox.activated[str].connect(self.handleStyleChanged)
		horizontalLayout.addWidget(self.styleLabel)
		horizontalLayout.addWidget(self.styleComboBox)
		self.setLayout(horizontalLayout)

	# 改變視窗樣式
	def handleStyleChanged(self, style):
		QApplication.setStyle(style)

if __name__ == "__main__":
	app =  QApplication(sys.argv)
	widgetApp = AppWidget()
	widgetApp.show()
	sys.exit(app.exec_())

