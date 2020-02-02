# -*- coding: utf-8 -*-

'''
    【簡介】
     關閉對話方塊時，返回值給主視窗範例
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DateDialog import DateDialog


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowTitle('關閉對話方塊時，返回值給主視窗範例')

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('彈出對話方塊1')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton('彈出對話方塊2')
        self.button2.clicked.connect(self.onButton2Click)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)
        self.setLayout(gridLayout)

    def onButton1Click(self):
        dialog = DateDialog(self)
        result = dialog.exec_()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        print('\n日期對話方塊的返回值：')
        print('date=%s' % str(date.date()))
        print('time=%s' % str(date.time()))
        print('result=%s' % result)
        dialog.destroy()

    def onButton2Click(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        print('\n日期對話方塊的返回值：')
        print('date=%s' % str(date))
        print('time=%s' % str(time))
        print('result=%s' % result)
        if result == QDialog.Accepted:
            print('點擊確認按鈕')
        else:
            print('點擊取消按鈕')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
