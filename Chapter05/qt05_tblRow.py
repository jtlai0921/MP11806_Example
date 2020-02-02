# -*- coding: utf-8 -*- 
'''
    【簡介】
	PyQT5中儲存格的寬度和高度範例
 
  
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem )

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget範例")
        self.resize(530,300);
        conLayout = QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget )
        
        tableWidget.setHorizontalHeaderLabels(['姓名','性別','體重(kg)'])  
          
        newItem = QTableWidgetItem("張三")  
        tableWidget.setItem(0, 0, newItem)  
        
        #將第一行的儲存格寬度設為150
        tableWidget.setColumnWidth(0,150)  
        #將第一行的儲存格高度設為120
        tableWidget.setRowHeight(0,120)      

        newItem = QTableWidgetItem("男")  
        tableWidget.setItem(0, 1, newItem)  
          
        newItem = QTableWidgetItem("160")  
        tableWidget.setItem(0, 2, newItem)   
        
        self.setLayout(conLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())
