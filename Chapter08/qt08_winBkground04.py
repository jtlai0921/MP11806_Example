# -*- coding: utf-8 -*-
 
'''
    【簡介】
    使用paintEvent設定視窗背景色
    
'''

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import   QPainter 
from PyQt5.QtCore import Qt

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("以paintEvent設定視窗背景色") 
         
	def paintEvent(self,event):
		painter = QPainter(self)
		painter.setBrush(Qt.yellow );
        # 設定背景顏色
		painter.drawRect( self.rect()); 
        
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
