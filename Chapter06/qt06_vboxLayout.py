# -*- coding: utf-8 -*-
 
'''
    【簡介】
    垂直佈局管理範例
    
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("垂直佈局管理範例") 
		self.resize(330, 150)  
        # 垂直佈局按照從上到下的順序增加按鈕控制項
		vlayout = QVBoxLayout()
		vlayout.addWidget( QPushButton(str(1)))
		vlayout.addWidget( QPushButton(str(2)))
		vlayout.addWidget( QPushButton(str(3)))
		vlayout.addWidget( QPushButton(str(4)))
		vlayout.addWidget( QPushButton(str(5)))
		self.setLayout(vlayout)   
  
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
