# -*- coding: utf-8 -*-


'''
    【簡介】
	PyQT5中Qlabel範例
     
'''

from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget, QVBoxLayout 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap ,QPalette
import sys  
    
class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
                
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        
        #1 初始化標籤控制項
        label1.setText("這是一個文字標籤。")
        label1.setAutoFillBackground(True) 
        palette = QPalette()   
        palette.setColor(QPalette.Window,Qt.blue)  
        label1.setPalette(palette) 
        label1.setAlignment( Qt.AlignCenter)
          
        label2.setText("<a href='#'>歡迎使用Python GUI應用程式</a>")
        
        label3.setAlignment( Qt.AlignCenter)    
        label3.setToolTip('這是一個圖片標籤')
        label3.setPixmap( QPixmap("./images/python.jpg"))

        label4.setText("<A href='http://www.cnblogs.com/wangshuo1/'>歡迎連結信平的小屋</a>")
        label4.setAlignment( Qt.AlignRight)
        label4.setToolTip('這是一個超連結標籤')
        
        #2 在視窗佈局中加入控制項
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget( label3 )
        vbox.addStretch()
        vbox.addWidget( label4)
        
        #3 允許label1控制項存取超連結
        label1.setOpenExternalLinks(True)
        # 開放允許存取超連結，預設是不允許，必須透過 setOpenExternalLinks(True)開放
        label4.setOpenExternalLinks( False )
        # 點擊文字方塊繫結槽事件  
        label4.linkActivated.connect( link_clicked )
        
        # 滑過文字方塊繫結槽事件       
        label2.linkHovered.connect( link_hovered )
        label1.setTextInteractionFlags( Qt.TextSelectableByMouse )

        self.setLayout(vbox)
        self.setWindowTitle("QLabel範例")
        
def link_hovered():
    print("當滑鼠滑過label-2標籤時，觸發事件。")
        
def link_clicked():
    print("當用滑鼠點擊label-4標籤時，觸發事件。" )
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())
