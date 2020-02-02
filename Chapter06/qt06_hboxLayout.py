# -*- coding: utf-8 -*-
 
'''
    【簡介】
    水平佈局管理範例
    
'''

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QHBoxLayout , QPushButton

class Winform(QWidget):
    def __init__(self,parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("水平佈局管理範例") 
	
        # 水平佈局按照從左到右的順序增加按鈕控制項
        hlayout = QHBoxLayout()       
        hlayout.addWidget( QPushButton(str(1)))
        hlayout.addWidget( QPushButton(str(2)))
        hlayout.addWidget( QPushButton(str(3)))
        hlayout.addWidget( QPushButton(str(4)))        
        hlayout.addWidget( QPushButton(str(5)))        
        self.setLayout(hlayout)   
  
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
