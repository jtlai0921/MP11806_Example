# -*- coding: utf-8 -*-
 
'''
    【簡介】
     巢狀佈局範例
    
'''

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget , QHBoxLayout,  QVBoxLayout,  QGridLayout ,  QFormLayout, QPushButton 
  
class MyWindow( QWidget):  

    def __init__(self):  
        super().__init__()
        self.setWindowTitle('巢狀佈局範例')
       
        # 全域佈局（1個）：水平
        wlayout =  QHBoxLayout() 
        # 局部佈局（4個）：水平、垂直、格子、表單
        hlayout =  QHBoxLayout()
        vlayout =  QVBoxLayout()
        glayout = QGridLayout()
        formlayout =  QFormLayout()
        
        # 局部佈局增加控制預（例如：按鈕）
        hlayout.addWidget( QPushButton(str(1)) ) 
        hlayout.addWidget( QPushButton(str(2)) )
        vlayout.addWidget( QPushButton(str(3)) )
        vlayout.addWidget( QPushButton(str(4)) )
        glayout.addWidget( QPushButton(str(5)) , 0, 0 )
        glayout.addWidget( QPushButton(str(6)) , 0, 1 )
        glayout.addWidget( QPushButton(str(7)) , 1, 0)
        glayout.addWidget( QPushButton(str(8)) , 1, 1)
        formlayout.addWidget( QPushButton(str(9))  )
        formlayout.addWidget( QPushButton(str(10)) )
        formlayout.addWidget( QPushButton(str(11)) )
        formlayout.addWidget( QPushButton(str(12)) )
        
        # 準備四個控制項
        hwg =  QWidget() 
        vwg =  QWidget()
        gwg =  QWidget()
        fwg =  QWidget()
                
        # 四個控制項設定局部佈局
        hwg.setLayout(hlayout) 
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(formlayout)
        
        # 四個控制項加到全域佈局
        wlayout.addWidget(hwg)
        wlayout.addWidget(vwg)
        wlayout.addWidget(gwg)
        wlayout.addWidget(fwg)
        
        # 將視窗本身設為全域佈局
        self.setLayout(wlayout) 
  
if __name__=="__main__":    
    app =  QApplication(sys.argv)    
    win = MyWindow()  
    win.show()  
    sys.exit(app.exec_())
    
