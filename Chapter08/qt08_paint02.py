# -*- coding: utf-8 -*-
 
'''
    【簡介】
    不規則視窗的實作
    
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QBitmap

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("不規則視窗的實作範例")

		self.pix = QBitmap("./images/mask.png")
		self.resize(self.pix.size())
		self.setMask(self.pix)
         
	def paintEvent(self,event):
		painter = QPainter(self)
        #在指定區域直接繪製視窗背景
		painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap("./images/screen1.jpg"))
		#繪製視窗背景，平鋪到整個視窗，隨著視窗改變而改變
        #painter.drawPixmap(0,0,self.width(),self.height(),QPixmap("./images/screen1.jpg"))
    
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
