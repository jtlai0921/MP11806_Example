2# -*- coding: utf-8 -*-

'''
    【簡介】
	 佈局中使用addStretch函數範例
    
'''

from PyQt5.QtWidgets import QApplication ,QWidget, QVBoxLayout , QHBoxLayout  ,QPushButton
import sys  
    
class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
            
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)      
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')
        
        hbox = QHBoxLayout()
        # 設定伸縮量為1
        hbox.addStretch(1)
        hbox.addWidget( btn1 )
        # 設定伸縮量為1
        hbox.addStretch(1)
        hbox.addWidget( btn2 )
        # 設定伸縮量為1
        hbox.addStretch(1)
        hbox.addWidget( btn3 )
        # 設定伸縮量為1
        hbox.addStretch(1 )        

        self.setLayout(hbox)
        self.setWindowTitle("addStretch範例")
                 
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())


