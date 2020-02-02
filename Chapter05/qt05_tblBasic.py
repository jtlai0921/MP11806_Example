# -*- coding: utf-8 -*- 

'''
    【簡介】
	PyQT5中儲存格的基本範例
    
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView )

class Table(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QTableWidget範例")
		self.resize(430,230);
		conLayout = QHBoxLayout()
		tableWidget = QTableWidget()
		tableWidget.setRowCount(4)
		tableWidget.setColumnCount(3)
		conLayout.addWidget(tableWidget )
		
		tableWidget.setHorizontalHeaderLabels(['姓名','性別','體重(kg)'])  
		  
		newItem = QTableWidgetItem("張三")  
		tableWidget.setItem(0, 0, newItem)  
		  
		newItem = QTableWidgetItem("男")  
		tableWidget.setItem(0, 1, newItem)  
		  
		newItem = QTableWidgetItem("160")  
		tableWidget.setItem(0, 2, newItem)   
		
		# 將表格變為禁止編輯
		# tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		
		# 設定表格為整列選擇
		# tableWidget.setSelectionBehavior(tableWidget.SelectRows)

		# 將列與行的大小設為和內容相符合
		# tableWidget.resizeColumnsToContents()
		# tableWidget.resizeRowsToContents()
		
		# 顯示與隱藏表格表頭
		# tableWidget.verticalHeader().setVisible(False)
		# tableWidget.horizontalHeader().setVisible(False)
		
		# 不顯示表格儲存格的分隔線
		# tableWidget.setShowGrid(False)
		
        # 不顯示垂直表頭
		# tableWidget.verticalHeader().setVisible(False)
		
		self.setLayout(conLayout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
