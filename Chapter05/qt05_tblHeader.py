# -*- coding: utf-8 -*- 
'''
    【簡介】
	PyQT5中表格表頭為自我調整模式
  
  
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication , QTableWidgetItem, QHeaderView)

class Table(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QTableWidget demo")
		self.resize(500,300);
		conLayout = QHBoxLayout()
		tableWidget= QTableWidget()
		tableWidget.setRowCount(4)
		tableWidget.setColumnCount(3)
		conLayout.addWidget(tableWidget )
		
		tableWidget.setHorizontalHeaderLabels(['姓名','性別','體重(kg)'])  
		# tableWidget.setVerticalHeaderLabels(['列1','列2','列3','列4' ])        
		
		tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		# select row height and column width match to cell content
		# tableWidget.resizeColumnsToContents()
		# tableWidget.resizeRowsToContents()
				 
		newItem = QTableWidgetItem("張三")  
		tableWidget.setItem(0, 0, newItem)  
		  
		newItem = QTableWidgetItem("男")  
		tableWidget.setItem(0, 1, newItem)  
		  
		newItem = QTableWidgetItem("160")  
		tableWidget.setItem(0, 2, newItem)   

		# select entire row
		# tableWidget.setSelectionBehavior(tableWidget.SelectRows)
		
		# show/hide vertical and horizontal headers
		# tableWidget.verticalHeader().setVisible(False)
		# tableWidget.horizontalHeader().setVisible(False)
		
		self.setLayout(conLayout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
