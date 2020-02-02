# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWinSignalSlog02 import Ui_Form
from PyQt5.QtCore import pyqtSignal, Qt 

class MyMainWindow(QMainWindow, Ui_Form):
	helpSignal = pyqtSignal(str)
	printSignal = pyqtSignal(list)
	# 宣告一個多重載版本的訊號，包括一個帶int與str類型趁數的訊號，以及帶str參數的訊號
	previewSignal = pyqtSignal([int,str],[str])
	
	def __init__(self, parent=None):    
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		self.initUI()
		
	def initUI(self):  	
		self.helpSignal.connect(self.showHelpMessage)
		self.printSignal.connect(self.printPaper)
		self.previewSignal[str].connect(self.previewPaper)
		self.previewSignal[int,str].connect(self.previewPaperWithArgs)  
		
		self.printButton.clicked.connect(self.emitPrintSignal)
		self.previewButton.clicked.connect(self.emitPreviewSignal)

	# 發射預覽訊號
	def emitPreviewSignal(self):
		if self.previewStatus.isChecked() == True:
			self.previewSignal[int,str].emit(1080," Full Screen")
		elif self.previewStatus.isChecked() == False:
			self.previewSignal[str].emit("Preview")

	# 發射列印訊號
	def emitPrintSignal(self):
		pList = []
		pList.append(self.numberSpinBox.value() )
		pList.append(self.styleCombo.currentText())
		self.printSignal.emit(pList)
		
	def printPaper(self,list):
		self.resultLabel.setText("列印："+"份數："+ str(list[0]) +" 紙張："+str(list[1]))

	def previewPaperWithArgs(self,style,text):
		self.resultLabel.setText(str(style)+text)		

	def previewPaper(self,text):
		self.resultLabel.setText(text)  
		
    # 重載按鍵事件
	def keyPressEvent(self, event):
		if event.key() == Qt.Key_F1:
			self.helpSignal.emit("help message")

    # 顯示說明訊息
	def showHelpMessage(self,message):
		self.resultLabel.setText(message)
		self.statusBar().showMessage(message)
	     		
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MyMainWindow()  
	win.show()  
	sys.exit(app.exec_())  
