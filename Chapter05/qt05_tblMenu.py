# -*- coding: utf-8 -*- 
'''
    【簡介】
	PyQT5的表格中支援右鍵選單範例
    
  
'''

import sys
from PyQt5.QtWidgets import ( QMenu , QPushButton,  QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import  QObject, Qt 

class Table( QWidget ):
                   
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QTableWidget範例")
		self.resize(500,300);
		conLayout = QHBoxLayout()
		self.tableWidget= QTableWidget()
		self.tableWidget.setRowCount(5)
		self.tableWidget.setColumnCount(3)
		conLayout.addWidget(self.tableWidget )
				
		self.tableWidget.setHorizontalHeaderLabels(['姓名','性別','體重' ])  
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		
		newItem = QTableWidgetItem("張三")      
		self.tableWidget.setItem(0, 0, newItem)  
		  
		newItem = QTableWidgetItem("男")  
		self.tableWidget.setItem(0, 1, newItem)  
		  
		newItem = QTableWidgetItem("160")  
		self.tableWidget.setItem(0, 2, newItem)   
		#表格中第二列記錄
		newItem = QTableWidgetItem("李四")      
		self.tableWidget.setItem(1, 0, newItem)  
		  
		newItem = QTableWidgetItem("女")  
		self.tableWidget.setItem(1, 1, newItem)  
		  
		newItem = QTableWidgetItem("170")  
		self.tableWidget.setItem(1, 2, newItem)   
		
		self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu) ######允許右鍵產生選單
		self.tableWidget.customContextMenuRequested.connect(self.generateMenu)   ####右鍵選單
		self.setLayout(conLayout)
        
	def generateMenu(self,pos):
		#rint( pos)
		row_num = -1
		for i in self.tableWidget.selectionModel().selection().indexes():
			row_num = i.row()
		
		if row_num < 2 :
			menu = QMenu()
			item1 = menu.addAction(u"選項一")
			item2 = menu.addAction(u"選項二")
			item3 = menu.addAction(u"選項三" )
			action = menu.exec_(self.tableWidget.mapToGlobal(pos))
			if action == item1:
				print( '您選了選項一，此列的文字內容是：',self.tableWidget.item(row_num,0).text(),self.tableWidget.item(row_num,1).text() ,self.tableWidget.item(row_num,2).text())

			elif action == item2:
				print( '您選了選項二，此列的文字內容是：',self.tableWidget.item(row_num,0).text(),self.tableWidget.item(row_num,1).text() ,self.tableWidget.item(row_num,2).text() )

			elif action == item3:
				print( '您選了選項三，此列的文字內容是：', self.tableWidget.item(row_num,0).text(),self.tableWidget.item(row_num,1).text() ,self.tableWidget.item(row_num,2).text() )
			else:
				return
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
