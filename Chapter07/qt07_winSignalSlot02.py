# -*- coding: utf-8 -*-

'''
    【簡介】
    控制項中的訊號槽通信範例

'''


from PyQt5.QtWidgets import QMainWindow,QHBoxLayout, QPushButton ,  QApplication, QWidget  
import sys 

class WinForm(QMainWindow):  
	
	def __init__(self, parent=None):  
		super(WinForm, self).__init__(parent)
		self.setWindowTitle('控制項中的訊號槽通信')
     
		self.button1 = QPushButton('Button 1')  
		# 
		self.button1.clicked.connect(self.onButtonClick) 
        
		layout = QHBoxLayout()  
		layout.addWidget(self.button1)  
        
		main_frame = QWidget()  
		main_frame.setLayout(layout)    
		self.setCentralWidget(main_frame)  
  
	def onButtonClick(self ):  
        #sender 是發送訊號的物件
		sender = self.sender()         
		print( sender.text() + ' 被按下了' )   
		
        
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
