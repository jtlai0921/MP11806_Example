# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中QFontDialog範例
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FontDialogDemo(QWidget):
	def __init__(self, parent=None):
		super(FontDialogDemo, self).__init__(parent)
		layout = QVBoxLayout()
		self.fontButton  = QPushButton("choose font")
		self.fontButton .clicked.connect(self.getFont)
		layout.addWidget(self.fontButton )
		self.fontLineEdit  = QLabel("Hello, 測試字體範例")
		layout.addWidget(self.fontLineEdit )
		self.setLayout(layout)
		self.setWindowTitle("Font Dialog範例")
		
	def getFont(self):
		font, ok = QFontDialog.getFont()
		if ok:
			self.fontLineEdit .setFont(font)
					
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = FontDialogDemo()
	demo.show()
	sys.exit(app.exec_())
