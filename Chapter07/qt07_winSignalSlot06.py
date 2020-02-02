# -*- coding: utf-8 -*-

'''
    【簡介】
    訊號/槽連結滑塊LCD範例

'''

import sys
from PyQt5.QtWidgets import QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication
from PyQt5.QtCore import Qt

class WinForm(QWidget):
    def __init__(self):
        super().__init__()   
        self.initUI()

    def initUI(self):
        #1 先建立滑塊和 LCD 控制項
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        
        #2 透過QVboxLayout設定佈局
        vBox = QVBoxLayout()
        vBox.addWidget(lcd)
        vBox.addWidget(slider)

        self.setLayout(vBox)
        #3 valueChanged()是Qslider的一個訊號函數，只要slider的值發生改變，
		#  它就會發射一個訊號，然後透過connect連結接收端的控制項，也就是lcd。
        slider.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,350,150)
        self.setWindowTitle("訊號與槽：連結滑塊LCD")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()                      
    sys.exit(app.exec_())
