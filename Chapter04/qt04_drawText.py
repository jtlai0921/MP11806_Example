# -*- coding: utf-8 -*-
 
"""
    【簡介】
    在視窗中繪製文字的範例
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import QPainter ,QColor ,QFont
from PyQt5.QtCore import Qt 

class Drawing(QWidget):
	def __init__(self,parent=None):
		super(Drawing,self).__init__(parent)
		self.setWindowTitle("在視窗中繪製文字") 
		self.resize(300, 200)        
		self.text = '歡迎學習 PyQt5'
         
	def paintEvent(self,event):
		painter = QPainter(self)        
		painter.begin(self)
        # 自訂繪製方法
		self.drawText(event, painter)
		painter.end()

	def drawText(self, event, qp):
        # 設定畫筆的顏色
		qp.setPen( QColor(168, 34, 3) )
        # 設定字體
		qp.setFont( QFont('SimSun', 20))
        # 繪製文字
		qp.drawText(event.rect(), Qt.AlignCenter, self.text)
		
if __name__ == "__main__":  
	app = QApplication(sys.argv) 
	demo = Drawing()
	demo.show()
	sys.exit(app.exec_())
