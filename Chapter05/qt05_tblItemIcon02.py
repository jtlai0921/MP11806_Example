# -*- coding: utf-8 -*- 

'''
    【簡介】
	PyQT5中儲存格改變每列儲存格顯示的圖示大小範例
   
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *

class Table(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QTableWidget範例")
		self.resize(1000,900);
		conLayout = QHBoxLayout()
		
		table = QTableWidget()
		table.setColumnCount(3)  
		table.setRowCount(5)  
		
		table.setHorizontalHeaderLabels(['圖片1','圖片2','圖片3'])  

		table.setEditTriggers(QAbstractItemView.NoEditTriggers)  

		table.setIconSize(QSize(300,200));

		for i in range(3):   # 讓行寬和圖片相同
			table.setColumnWidth(i , 300)  
		for i in range(5):   # 讓列高和圖片相同
			table.setRowHeight(i , 200)  

		for k in range(15): # 27 examples of DDA  
			i = k/3  
			j = k%3  
			item = QTableWidgetItem()  
			item.setFlags(Qt.ItemIsEnabled)  #使用者點擊表格時，便選中圖片 
			icon = QIcon(r'.\images\bao%d.png' % k)
			item.setIcon(QIcon(icon ))
									
			print('e/icons/%d.png i=%d  j=%d' %( k , i , j ) )   				   
			table.setItem(i,j,item)  
		
		conLayout.addWidget(table)  
		self.setLayout(conLayout)
      
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
