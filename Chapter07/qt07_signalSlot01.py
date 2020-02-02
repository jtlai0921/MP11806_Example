# -*- coding: utf-8 -*-

'''
    【簡介】
    內建訊號、自訂槽的範例

'''

import sys
from PyQt5.QtWidgets import QWidget,QPushButton, QApplication

class Winform(QWidget):
	def __init__(self):
		super(Winform, self).__init__()        
		self.setGeometry(200,300,350,50)
		self.setWindowTitle("內建訊號、自訂槽的範例")
		
		self.btn = QPushButton("按鈕文字",self)  
		self.btn.clicked.connect(self.changeBtnText)  
	
	def changeBtnText(self):  
		self.btn.setText("按鈕的內容和寬度改變了！")  
		self.btn.setStyleSheet("QPushButton{max-width:200px; min-width:200px}")
	
if __name__ == '__main__':
    app = QApplication(sys.argv)
    qb = Winform()
    qb.show()
    sys.exit(app.exec_())
    
