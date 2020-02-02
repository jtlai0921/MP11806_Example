# -*- coding: utf-8 -*-
 
"""
    【簡介】
    列印圖片範例
    
    
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage , QIcon, QPixmap
from PyQt5.QtWidgets import QApplication  , QMainWindow, QLabel,  QSizePolicy , QAction
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import sys  
      
class MainWindow(QMainWindow):  
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)  
		self.setWindowTitle(self.tr("列印圖片"))  
		# 建立一個置放圖形的QLabel物件imageLabel，並將該QLabel物件設定為中心視窗。 
		self.imageLabel=QLabel()  
		self.imageLabel.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)  
		self.setCentralWidget(self.imageLabel)  

		self.image=QImage()  
		  
		# 建立功能表、工具列等元件
		self.createActions()  
		self.createMenus()  
		self.createToolBars()  

		# 在imageLabel物件中置放圖形
		if self.image.load("./images/screen.png"):  
			self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  
			self.resize(self.image.width(),self.image.height())  
									
	def createActions(self):  
		self.PrintAction=QAction(QIcon("./images/printer.png"),self.tr("列印"),self)  
		self.PrintAction.setShortcut("Ctrl+P")  
		self.PrintAction.setStatusTip(self.tr("列印"))  
		self.PrintAction.triggered.connect(self.slotPrint) 

	def createMenus(self):  
		PrintMenu=self.menuBar().addMenu(self.tr("列印"))  
		PrintMenu.addAction(self.PrintAction)  

	def createToolBars(self):  
		fileToolBar=self.addToolBar("Print")  
		fileToolBar.addAction(self.PrintAction)  

	def slotPrint(self):  
		# 新建一個QPrinter物件 
		printer=QPrinter()  
		# 建立一個QPrintDialog物件，參數為QPrinter物件
		printDialog=QPrintDialog(printer,self)  

		'''
		判斷列印對話方塊顯示後是否點擊「列印」鈕，如果是，
		則相關列印屬性可以透過建立QPrintDialog物件時以QPrinter物件取得，
		若點擊「取消」鈕，則不執行後續的列印操作。 
		''' 		
		if printDialog.exec_():  
			# 建立一個QPainter物件，並指定繪圖設備為一個QPrinter物件。
			painter=QPainter(printer)  
			# 取得QPainter物件的視窗矩形
			rect=painter.viewport()  
			# 取得圖形的大小
			size=self.image.size()  
			# 依照圖形的比例大小重新設定視窗矩形
			size.scale(rect.size(),Qt.KeepAspectRatio)  
			painter.setViewport(rect.x(),rect.y(),size.width(),size.height())  
			# 設定QPainter視窗大小為圖形的大小
			painter.setWindow(self.image.rect()) 
			# 列印			
			painter.drawImage(0,0,self.image)  

if __name__ == "__main__":                    
	app=QApplication(sys.argv)  
	main=MainWindow()  
	main.show()  
	sys.exit(app.exec_()) 
