# -*- coding: utf-8 -*-
 
'''
    【簡介】
    使用paintEvent在視窗實作畫線範例
    
'''

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import   QPainter ,QPixmap
from PyQt5.QtCore import Qt , QPoint

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("簡單繪圖範例") 
		self.pix =  QPixmap()
		self.lastPoint =  QPoint()
		self.endPoint =  QPoint()
		self.initUi()
		
	def initUi(self):
		# 視窗大小設為600*500
		self.resize(600, 500)  
		# 畫布大小為400*400，背景為白色
		self.pix = QPixmap(400, 400)
		self.pix.fill(Qt.white)
         
	def paintEvent(self,event):
		pp = QPainter( self.pix)
		# 根據滑鼠指標前後兩個位置繪製直線
		pp.drawLine( self.lastPoint, self.endPoint)
		# 讓前一個座標值等於後一個座標值，
		# 這樣就能畫出連續的線
		self.lastPoint = self.endPoint
		painter = QPainter(self)
		painter.drawPixmap(0, 0, self.pix)	

	def mousePressEvent(self, event) :   
		# 按下滑鼠左鍵  
		if event.button() == Qt.LeftButton :
			self.lastPoint = event.pos()   
			self.endPoint = self.lastPoint
	
	def mouseMoveEvent(self, event):	
		# 按下滑鼠左鍵的同時移動滑鼠
		if event.buttons() and Qt.LeftButton :
			self.endPoint = event.pos()
			# 重新繪製
			self.update()

	def mouseReleaseEvent( self, event):
		# 釋放滑鼠左鍵   
		if event.button() == Qt.LeftButton :
			self.endPoint = event.pos()
			# 重新繪製
			self.update()
			
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
