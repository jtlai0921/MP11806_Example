# -*- coding: utf-8 -*-
 
"""
    【簡介】
    在視窗中畫點的範例
    
    
"""

import sys, math
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 

class Drawing(QWidget):
	def __init__(self, parent=None):
		super(Drawing, self).__init__(parent)
		self.resize(300, 200)  
		self.setWindowTitle("在視窗中畫點")         

	def paintEvent(self, event):
		# 初始化繪圖工具
		qp = QPainter()
		qp.begin(self)
		# 自訂畫點方法
		self.drawPoints(qp)
		qp.end()
		
	def drawPoints(self,  qp):
		qp.setPen( Qt.red)
		size = self.size()
		
		for i in range(1000):
			# 繪製正弦函數圖形，它的週期是[-100, 100] 
			x = 100 *(-1+2.0*i/1000)+ size.width()/2.0
			y = -50 * math.sin((x - size.width()/2.0)*math.pi/50) + size.height()/2.0
			qp.drawPoint(x, y)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo  = Drawing()
	demo.show()
	sys.exit(app.exec_())
