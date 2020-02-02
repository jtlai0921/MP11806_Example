# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中DateTimeEdit範例
   
  
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate,   QDateTime , QTime 

class DateTimeEditDemo(QWidget):
	def __init__(self):
		super(DateTimeEditDemo, self).__init__()
		self.initUI()
		
	def initUI(self): 
		self.setWindowTitle('QDateTimeEdit範例')
		self.resize(300, 90)   

		vlayout = QVBoxLayout()
		dateTimeEdit = QDateTimeEdit(self)
		# dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime(), self)
		# dateEdit = QDateTimeEdit(QDate.currentDate(), self)
		# timeEdit = QDateTimeEdit(QTime.currentTime(), self)

		# 設定日期/時間格式
		dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
		# dateTimeEdit.setDisplayFormat("yyyy/MM/dd HH:mm")
		
		# dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
		# dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH:mm")

		# dateEdit.setDisplayFormat("yyyy.MM.dd")
		# dateEdit.setDisplayFormat("yyyy/MM/dd")
		
		# timeEdit.setDisplayFormat("HH:mm:ss")
                
		vlayout.addWidget( dateTimeEdit )
		# vlayout.addWidget( dateTimeEdit2)
		# vlayout.addWidget( dateEdit )
		# vlayout.addWidget( timeEdit )
		
		self.btn4= QPushButton("取得日期和時間")
		self.btn4.setDefault(True)
		# self.btn4.clicked.connect(lambda:self.whichbtn(self.btn4))
		vlayout.addWidget(self.btn4)
		
		self.setLayout(vlayout)   
        
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = DateTimeEditDemo()
	demo.show()
	sys.exit(app.exec_())
