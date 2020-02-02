# -*- coding: utf-8 -*-
'''
    【簡介】
    訊號和槽範例

'''
     
from PyQt5.QtWidgets import  QPushButton ,  QApplication, QWidget 
from  PyQt5.QtWidgets import QMessageBox  
import sys 
   
app =  QApplication(sys.argv)
widget =  QWidget()

def showMsg():
     QMessageBox.information(widget, "訊息提示框", "ok，彈出測試訊息")      

btn = QPushButton("測試點擊按鈕", widget)
btn.clicked.connect(showMsg)
widget.show()
sys.exit(app.exec_())
