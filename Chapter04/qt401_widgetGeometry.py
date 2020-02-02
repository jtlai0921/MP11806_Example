# -*- coding: utf-8 -*-

'''
    【簡介】
     PyQt5中坐標系統

'''

from PyQt5.QtWidgets import QApplication  ,QWidget  ,QPushButton
import sys  
              
app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton( widget )
btn.setText("Button")
#以QWidget左上角為(0, 0)點
btn.move(20, 20)   
#不同的作業系統可能對視窗的最小寬度有限制，若設定的寬度小於規定值，則以規定值為主
widget.resize(300, 200) 
#以螢幕左上角為(0, 0)點
widget.move(250, 200)

widget.setWindowTitle('PyQt坐標系統範例')
widget.show()
print("#1 QWidget")
print("widget.x()=%d" % widget.x() )
print("widget.y()=%d" % widget.y() )
print("widget.width()=%d" % widget.width() )
print("widget.height()=%d" % widget.height() )

print("#2 QWidget.geometry")
print("widget.geometry().x()=%d" %  widget.geometry().x() )
print("widget.geometry().y()=%d" %  widget.geometry().y() )
print("widget.geometry().width()=%d" %  widget.geometry().width() )
print("widget.geometry().height()=%d" %  widget.geometry().height() )
print("widget.size().width() =%d" %  widget.size().width() )
print("widget.size().height() =%d" %  widget.size().height() )

print("#3 QWidget.frameGeometry")
print("widget.frameGeometry().width()=%d" %  widget.frameGeometry().width() )
print("widget.frameGeometry().height()=%d" %  widget.frameGeometry().height() )
print("widget.pos().x()=%d" %  widget.pos().x() )
print("widget.pos().y()=%d" %  widget.pos().y() )

sys.exit(app.exec_())  
    
