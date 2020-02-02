#!/usr/bin/env python3

'''
    【簡介】
	PyQT5中QTreeWidget範例
   
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon ,  QBrush , QColor
from PyQt5.QtCore import Qt 

class TreeWidgetDemo(QMainWindow):   
	def __init__(self,parent=None):
		super(TreeWidgetDemo,self).__init__(parent)
		self.setWindowTitle('TreeWidget範例')
		self.tree = QTreeWidget()
        # 設定行數
		self.tree.setColumnCount(2)
        # 設定樹狀控制項的標題
		self.tree.setHeaderLabels(['Key','Value'])
		# 設定根節點
		root= QTreeWidgetItem(self.tree)
		root.setText(0,'root')
		root.setIcon(0,QIcon("./images/root.png"))
		# 設定行寬
		self.tree.setColumnWidth(0, 160)
		
		### 設定節點的背景顏色
		#brush_red = QBrush(Qt.red)
		#root.setBackground(0, brush_red) 
		#brush_green = QBrush(Qt.green)
		#root.setBackground(1, brush_green) 
		
		# 設定子節點1
		child1 = QTreeWidgetItem(root)
		child1.setText(0,'child1')
		child1.setText(1,'ios')
		child1.setIcon(0,QIcon("./images/IOS.png"))
		child1.setCheckState(0, Qt.Checked)
				
		# 設定子節點2
		child2 = QTreeWidgetItem(root)
		child2.setText(0,'child2')
		child2.setText(1,'')
		child2.setIcon(0,QIcon("./images/android.png"))
				
		# 設定子節點3
		child3 = QTreeWidgetItem(child2)
		child3.setText(0,'child3')
		child3.setText(1,'android')
		child3.setIcon(0,QIcon("./images/music.png"))
	
		self.tree.addTopLevelItem(root)
		# 展開全部節點
		self.tree.expandAll()
		
		self.setCentralWidget(self.tree)  

        
if __name__ == '__main__':
	app = QApplication(sys.argv)
	tree = TreeWidgetDemo()
	tree.show()
	sys.exit(app.exec_())
