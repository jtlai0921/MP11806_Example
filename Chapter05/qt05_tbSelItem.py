# -*- coding: utf-8 -*- 
'''
    【簡介】
	PyQT5的表格控制項選中儲存格
   
  
'''

import sys
from PyQt5.QtWidgets import  *
from PyQt5 import QtCore  
from PyQt5.QtGui import  QColor , QBrush

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget範例")
        self.resize(600,800);
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(30)
        tableWidget.setColumnCount(4)
        conLayout.addWidget(tableWidget )
        
        for i in range(30):
            for j in range(4):
                itemContent = '(%d,%d)'% (i,j)  
                tableWidget.setItem(i,j, QTableWidgetItem( itemContent ) )
        self.setLayout(conLayout)
        
        # 巡訪表格找尋對應的儲存格
        text = "(10,1)"
        items = tableWidget.findItems(text, QtCore.Qt.MatchExactly)             
        item = items[0]
        # 選中儲存格
        #item.setSelected( True)
        # 設定儲存格的背景顏色為紅色
        item.setForeground(QBrush(QColor(255, 0, 0))) 
                
        row = item.row()   
        # 模擬滑鼠滾輪快速定位到指定列
        tableWidget.verticalScrollBar().setSliderPosition(row)  
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())
    
