# -*- coding: utf-8 -*-

'''
    【簡介】
	縮放圖片大小
    
'''

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui  import QImage, QPixmap
from PyQt5.QtCore import Qt
import sys

class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
        filename = r".\images\Cloudy_72px.png"
        img = QImage( filename )
               
        label1 = QLabel(self)
        label1.setFixedWidth(120)
        label1.setFixedHeight(120)
         
        result = img.scaled(label1.width(), label1.height(),Qt.IgnoreAspectRatio, Qt.SmoothTransformation);
        label1.setPixmap(QPixmap.fromImage(result))
        
        #3
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
      
        self.setLayout(vbox)
        self.setWindowTitle("縮放圖片大小範例")
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())
