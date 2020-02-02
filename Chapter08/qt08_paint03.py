# -*- coding: utf-8 -*-
 
'''
    【簡介】
    不規則，但可以拖動的視窗實作範例
    
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtGui import  QPixmap, QPainter, QCursor, QBitmap
from PyQt5.QtCore import Qt

class ShapeWidget(QWidget):
	def __init__(self,parent=None):
		super(ShapeWidget,self).__init__(parent)
		self.setWindowTitle("不規則，但可以拖動的視窗範例")
		self.mypix()

    # 顯示不規則 pic
	def mypix(self):
		self.pix = QBitmap( "./images/mask.png" )
		self.resize(self.pix.size())
		self.setMask(self.pix)
		print( self.pix.size())
		self.dragPosition = None

	# 重新定義滑鼠按下回應函數mousePressEvent(QMouseEvent)和滑鼠移動回應函數mouseMoveEvent(QMouseEvent)，
	# 使不規則表單能夠回應滑鼠事件，隨意拖動。
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.m_drag=True
			self.m_DragPosition=event.globalPos()-self.pos()
			event.accept()
			self.setCursor(QCursor(Qt.OpenHandCursor))
		if event.button()==Qt.RightButton:  
			self.close()  
			
	def mouseMoveEvent(self, QMouseEvent):
		if Qt.LeftButton and self.m_drag:
		    # 當以左鍵移動表單時，修改偏移值
			self.move(QMouseEvent.globalPos()- self.m_DragPosition )
			QMouseEvent.accept()
	
	def mouseReleaseEvent(self, QMouseEvent):
		self.m_drag=False
		self.setCursor(QCursor(Qt.ArrowCursor))
    
    # 一般在表單首次繪製時載入paintEvent。若想重新載入paintEvent，必須重新載入視窗。使用self.update() or self.repaint()    
	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawPixmap(0,0,self.width(),self.height(),QPixmap("./images/boy.png"))
			
if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=ShapeWidget()
    form.show()
    app.exec_()
