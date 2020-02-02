# -*- coding: utf-8 -*- 

'''
    【簡介】
	PyQT5中儲存格裡面放控制項
    
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView ,QComboBox, QPushButton )

class Table(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QTableWidget範例")
		self.resize(430,300);
		conLayout = QHBoxLayout()
		tableWidget = QTableWidget()
		tableWidget.setRowCount(4)
		tableWidget.setColumnCount(3)
		conLayout.addWidget(tableWidget )
		
		tableWidget.setHorizontalHeaderLabels(['姓名','性別','體重(kg)'])  
		  
		newItem = QTableWidgetItem("張三")  
		tableWidget.setItem(0, 0, newItem)  
		  
		comBox = QComboBox()
		comBox.addItem("男")
		comBox.addItem("女")
		comBox.setStyleSheet("QComboBox{margin:3px};")
		tableWidget.setCellWidget(0,1,comBox)
		
		searchBtn = QPushButton("修改")  
		searchBtn.setDown( True )
		searchBtn.setStyleSheet("QPushButton{margin:3px};")
		tableWidget.setCellWidget(0, 2, searchBtn) 
		 				
		self.setLayout(conLayout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
