# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中QSlider範例
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SliderDemo(QWidget):
	def __init__(self, parent=None):
		super(SliderDemo, self).__init__(parent)
		self.setWindowTitle("QSlider 範例")  
		self.resize(300, 100)
        
		layout = QVBoxLayout()
		self.l1 = QLabel("Hello PyQt5")
		self.l1.setAlignment(Qt.AlignCenter)
		layout.addWidget(self.l1)
        # 水平方向
		self.sl = QSlider(Qt.Horizontal)
        # 設定最小值
		self.sl.setMinimum(10)
		# 設定最大值
		self.sl.setMaximum(50)
		# 步長
		self.sl.setSingleStep( 3 ) 
		# 設置目前值
		self.sl.setValue(20)
		# 刻度位置，刻度在下方
		self.sl.setTickPosition(QSlider.TicksBelow)
        # 設定刻度間隔
		self.sl.setTickInterval(5)
		layout.addWidget(self.sl)
        # 連接訊號/槽
		self.sl.valueChanged.connect(self.valuechange)
		self.setLayout(layout)
                      
	def valuechange(self):
		print('current slider value=%s' % self.sl.value() )
		size = self.sl.value()
		self.l1.setFont(QFont("Arial",size))
                      
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = SliderDemo()
	demo.show()
	sys.exit(app.exec_())
