# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQT5將視窗放在螢幕中間例子
    
'''

from PyQt5.QtWidgets import QDesktopWidget, QApplication ,QMainWindow
import sys  
    
class Winform( QMainWindow): 
    
    def __init__(self, parent=None):
        super( Winform, self).__init__(parent)
          
        self.setWindowTitle('主視窗放在螢幕中間例子')  
        self.resize(370,  250)  
        self.center()  
          
    def center(self):  
        screen = QDesktopWidget().screenGeometry()  
        size = self.geometry()        
        self.move((screen.width() - size.width()) / 2,  (screen.height() - size.height()) / 2)  
  
if __name__ == "__main__": 
    app = QApplication(sys.argv)   
    win = Winform()  
    win.show()  
    sys.exit(app.exec_())  
