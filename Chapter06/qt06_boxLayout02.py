# -*- coding: utf-8 -*-
 
'''
    【簡介】
    水平佈局管理範例
    
'''

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QHBoxLayout , QPushButton
from PyQt5.QtCore import Qt 

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("水平佈局管理範例") 
		self.resize(800, 200)
		
		# 水平佈局按照從左到右的順序增加按鈕控制項
		hlayout = QHBoxLayout()  
     
		# 水平靠左、垂直靠上對齊
		hlayout.addWidget( QPushButton(str(1)) , 0 , Qt.AlignLeft | Qt.AlignTop)
		hlayout.addWidget( QPushButton(str(2)) , 0 , Qt.AlignLeft | Qt.AlignTop)
		hlayout.addWidget( QPushButton(str(3)))
		# 水平靠左、垂直靠下對齊
		hlayout.addWidget( QPushButton(str(4)) , 0 , Qt.AlignLeft | Qt.AlignBottom )        
		hlayout.addWidget( QPushButton(str(5)), 0 , Qt.AlignLeft | Qt.AlignBottom)    
		
		self.setLayout(hlayout)   
  
if __name__ == "__main__":  
	app = QApplication(sys.argv) 
	form = Winform()
	form.show()
	sys.exit(app.exec_())
