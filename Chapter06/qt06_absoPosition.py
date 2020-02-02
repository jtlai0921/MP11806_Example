# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQT5中Absolute positioning(絕對位置)範例
  
'''

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
      
class Example(QWidget):
    def __init__(self): 
        super().__init__()
        self.initUI()
          
    def initUI(self):
        lbl1 = QLabel('歡迎', self)
        lbl1.move(15, 10)
  
        lbl2 = QLabel('學習', self)
        lbl2.move(35, 40)
          
        lbl3 = QLabel('PyQt5!', self)
        lbl3.move(55, 70)
          
        self.setGeometry(300, 300, 320, 120)
        self.setWindowTitle('絕對位置佈局範例')
                                  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Example()  
    demo.show()
    sys.exit(app.exec_())
