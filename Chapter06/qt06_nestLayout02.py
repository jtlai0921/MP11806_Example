# -*- coding: utf-8 -*-
 
'''
    【簡介】
     巢狀佈局範例
    
'''

from PyQt5.QtWidgets import *
import sys   
 
class MyWindow(QWidget):  

	def __init__(self):  
		super().__init__()
		self.setWindowTitle('巢狀佈局範例')
		self.resize(700, 200)
        
        # 全域控制項（注意參數 self），用來「承載」全域佈局
		wwg = QWidget(self)
        
        # 全域佈局（注意參數 wwg）
		wl = QHBoxLayout(wwg)
		hlayout =  QHBoxLayout()
		vlayout =  QVBoxLayout()
		glayout = QGridLayout()
		formlayout =  QFormLayout()
        
        # 局部佈局增加控制預（例如：按鈕）
		hlayout.addWidget( QPushButton(str(1)) )
		hlayout.addWidget( QPushButton(str(2)) )
		vlayout.addWidget( QPushButton(str(3)) )
		vlayout.addWidget( QPushButton(str(4)) )
		glayout.addWidget( QPushButton(str(5)) , 0, 0 )
		glayout.addWidget( QPushButton(str(6)) , 0, 1 )
		glayout.addWidget( QPushButton(str(7)) , 1, 0 )
		glayout.addWidget( QPushButton(str(8)) , 1, 1 )
		formlayout.addWidget( QPushButton(str(9)) )
		formlayout.addWidget( QPushButton(str(10)) )
		formlayout.addWidget( QPushButton(str(11)) )
		formlayout.addWidget( QPushButton(str(12)) )
        
        # 對局部佈局增加控制項，然後加到全域佈局
		wl.addLayout(hlayout)  
		wl.addLayout(vlayout)
		wl.addLayout(glayout)
		wl.addLayout(formlayout)       

if __name__=="__main__":    
 
	app = QApplication(sys.argv)    
	win = MyWindow()  
	win.show()  
	sys.exit(app.exec_())
    
