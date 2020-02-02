# -*- coding: utf-8 -*-

'''
    【簡介】
     關閉對話方塊時，返回值給主視窗範例
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DateDialog2 import DateDialog


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowTitle('訊號與槽傳遞參數的範例')

        self.open_btn = QPushButton('取得時間')
        self.lineEdit_inner = QLineEdit(self)
        self.lineEdit_emit = QLineEdit(self)
        self.open_btn.clicked.connect(self.openDialog)

        self.lineEdit_inner.setText('接收子視窗內建訊號的時間')
        self.lineEdit_emit.setText('接收子視窗自訂訊號的時間')

        grid = QGridLayout()
        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)

        grid.addWidget(self.open_btn)
        self.setLayout(grid)

    def openDialog(self):
        dialog = DateDialog(self)
        '''連結子視窗的內建訊號與主視窗的槽函數'''
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        '''連結子視窗的自訂訊號與主視窗的槽函數'''
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()

    def deal_inner_slot(self, date):
        self.lineEdit_inner.setText(date.toString())


    def deal_emit_slot(self, dateStr):
        self.lineEdit_emit.setText(dateStr)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
