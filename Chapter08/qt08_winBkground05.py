# -*- coding: utf-8 -*-
 
'''
    【簡介】
    使用paintEvent設定視窗背景圖片
    
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import  QPixmap, QPainter

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("以paintEvent設定視窗背景圖片")
         
	def paintEvent(self,event):
		painter = QPainter(self)
		pixmap = QPixmap("./images/screen1.jpg")
        #繪製視窗背景，平鋪到整個視窗，隨著視窗改變而改變
		painter.drawPixmap(self.rect(),pixmap)
        
if __name__ == "__main__":
		app = QApplication(sys.argv)
		form = Winform()
		form.show()
		sys.exit(app.exec_())
