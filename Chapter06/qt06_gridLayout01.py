# -*- coding: utf-8 -*-
 
'''
    【簡介】
    格子佈局管理範例
    
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.initUI()

	def initUI(self):            
        #1
		grid = QGridLayout()  
		self.setLayout(grid)  
   
        #2
		names = ['Cls', 'Back', '', 'Close',  
                 '7', '8', '9', '/',  
                '4', '5', '6', '*',  
                 '1', '2', '3', '-',  
                '0', '.', '=', '+']  
        
        #3        
		positions = [(i,j) for i in range(5) for j in range(4)]  
         
        #4 
		for position, name in zip(positions, names):                
			if name == '':  
				continue  
				
			button = QPushButton(name)  
			grid.addWidget(button, *position)  
              
		self.move(300, 150)  
		self.setWindowTitle('格子佈局管理範例')  
  
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
