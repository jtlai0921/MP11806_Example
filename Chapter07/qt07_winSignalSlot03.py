# -*- coding: utf-8 -*-

'''
    【簡介】
    控制項中的訊號槽通訊範例

'''

from PyQt5.QtCore import pyqtSignal  
from PyQt5.QtWidgets import QMainWindow,QHBoxLayout, QPushButton ,  QApplication, QWidget  , QMessageBox
import sys 

class WinForm(QMainWindow):  
	btnlickedSignal = pyqtSignal(int) 

	def __init__(self, parent=None):  
		super(WinForm, self).__init__(parent)
		self.setWindowTitle('控制項中的訊號槽通訊範例')
        # 宣告自訂的訊號
		self.btnlickedSignal.connect(self.getSignal)  
		self.button1 = QPushButton('Button 1')  
		# 使用訊號連接槽函數，槽函數不用加括弧 
		self.button1.clicked.connect(self.onButtonClick ) 
        
		layout = QHBoxLayout()  
		layout.addWidget(self.button1)  
		main_frame = QWidget()  
		main_frame.setLayout(layout)    
		self.setCentralWidget(main_frame)  
  
	def onButtonClick(self ):      
		print('The button1 被按下了' )   		     
		self.btnlickedSignal.emit(10)
        
	def getSignal(self, intVal ): 
		QMessageBox.information(self, "資訊提示框", '收到訊號傳過來的值：' +  str(intVal) )   
        
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
