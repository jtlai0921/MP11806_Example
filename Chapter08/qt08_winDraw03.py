# -*- coding: utf-8 -*-
 
'''
    【簡介】
   雙緩衝繪圖
    
'''

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import   QPainter ,QPixmap
from PyQt5.QtCore import Qt , QPoint

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("雙緩衝繪圖範例") 
		self.pix =  QPixmap()
		self.lastPoint =  QPoint()
		self.endPoint =  QPoint()
		# 輔助畫布
		self.tempPix = QPixmap()
		# 標示是否正在繪圖
		self.isDrawing = False    
		self.initUi()
		
	def initUi(self):
		# 視窗大小設為600*500
		self.resize(600, 500);   
		# 畫布大小為400*400，背景為白色
		self.pix = QPixmap(400, 400);
		self.pix.fill(Qt.white);
         
	def paintEvent(self,event):
		painter = QPainter(self)
		x = self.lastPoint.x()
		y = self.lastPoint.y()
		w = self.endPoint.x() - x
		h = self.endPoint.y() - y
					
		# 如果正在繪圖，就在輔助畫布上繪製
		if self.isDrawing :			
			# 將以前pix的內容複製到tempPix中，保留以前的內容
			self.tempPix = self.pix
			pp = QPainter( self.tempPix)
			pp.drawRect(x,y,w,h)
			painter.drawPixmap(0, 0, self.tempPix)
		else :
			pp = QPainter(self.pix )
			pp.drawRect(x, y, w, h)
			painter.drawPixmap(0, 0, self.pix)
		
	def mousePressEvent(self, event) :   
		# 按下滑鼠左鍵
		if event.button() == Qt.LeftButton :
			self.lastPoint = event.pos()   
			self.endPoint = self.lastPoint
			self.isDrawing = True
	
	def mouseReleaseEvent( self, event):	
		# 釋放滑鼠左鍵
		if event.button() == Qt.LeftButton :
			self.endPoint = event.pos()
			# 重新繪製
			self.update()
			self.isDrawing = False
						
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
		

