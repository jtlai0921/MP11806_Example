# -*- coding: utf-8 -*- 

'''
    【簡介】
	PyQT5中儲存格內的文字顏色
   
  
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem )
from PyQt5.QtGui import QBrush,  QColor ,  QFont 

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
        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 0, newItem)  
                 
        newItem = QTableWidgetItem("男")  
        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 1, newItem)  
          
        newItem = QTableWidgetItem("160") 
        newItem.setForeground(QBrush(QColor(255, 0, 0))) 
        tableWidget.setItem(0, 2, newItem)     
        
        self.setLayout(conLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())
