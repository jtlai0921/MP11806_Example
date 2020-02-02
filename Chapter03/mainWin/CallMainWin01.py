# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog 
from MainForm import Ui_MainWindow  

class MainForm( QMainWindow , Ui_MainWindow):  
	def __init__(self):  
		super(MainForm,self).__init__()  
		self.setupUi(self) 
		# 功能表的點擊事件，當點擊關閉功能表時連接槽函數 close()     
		self.fileCloseAction.triggered.connect(self.close)  
		# 功能表的點擊事件，當點擊開啟功能表時連接槽函數 openMsg()     
		self.fileOpenAction.triggered.connect(self.openMsg)    

	def openMsg(self):  
		file,ok= QFileDialog.getOpenFileName(self,"開啟","C:/","All Files (*);;Text Files (*.txt)") 
		# 在狀態列顯示檔案位址  		
		self.statusbar.showMessage(file)                   
    
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainForm()  
	win.show()  
	sys.exit(app.exec_()) 
