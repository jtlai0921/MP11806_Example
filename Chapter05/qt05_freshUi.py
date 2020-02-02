# -*- coding: utf-8 -*- 
'''
    【簡介】
	PyQT5中即時刷新介面範例
 
  
'''

from PyQt5.QtWidgets import QWidget,  QPushButton ,  QApplication ,QListWidget,  QGridLayout 
import sys
import time

class WinForm(QWidget):
	
	def __init__(self,parent=None):
		super(WinForm,self).__init__(parent)
		self.setWindowTitle("即時刷新介面範例")
		self.listFile= QListWidget()
		self.btnStart = QPushButton('開始')
		layout = QGridLayout(self)
		layout.addWidget(self.listFile,0,0,1,2)
		layout.addWidget(self.btnStart,1,1)
		self.btnStart.clicked.connect( self.slotAdd)
		self.setLayout(layout)
		
	def slotAdd(self):
		for n in range(10):
			str_n='File index {0}'.format(n)
			self.listFile.addItem(str_n)
			QApplication.processEvents()
			time.sleep(1)
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = WinForm()
	form.show()
	sys.exit(app.exec_())
