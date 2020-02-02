# -*- coding: utf-8 -*- 
'''
    【簡介】
    PyQT5中關閉視窗範例
 
  
'''

from PyQt5.QtWidgets import QMainWindow,QHBoxLayout, QPushButton ,  QApplication, QWidget  
import sys 

class WinForm(QMainWindow):  
	
	def __init__(self, parent=None):  
		super(WinForm, self).__init__(parent)
		self.resize(330,  100)  
		self.setWindowTitle('關閉主視窗範例') 		
		self.button1 = QPushButton('關閉主視窗')  		
		self.button1.clicked.connect(self.onButtonClick) 
        
		layout = QHBoxLayout()  
		layout.addWidget(self.button1)  
        
		main_frame = QWidget()  
		main_frame.setLayout(layout)    
		self.setCentralWidget(main_frame)  
  
	def onButtonClick(self ):  
        #sender 是發送訊號的物件，此處傳送訊號的物件是button1按鈕 
		sender = self.sender()         
		print( sender.text() + ' 被按下了' )
		qApp = QApplication.instance()
		qApp.quit()
		
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
