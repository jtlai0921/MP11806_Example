# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from MainForm2 import Ui_MainWindow
from ChildrenForm2 import Ui_ChildrenForm


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        # self.child = children() 產生子視窗實例self.child
        self.child = ChildrenForm()

        # 功能表的點擊事件，當單擊關閉功能表時連接槽函數 close()
        self.fileCloseAction.triggered.connect(self.close)
        # 功能表的點擊事件，當單擊開啟功能表時連接槽函數 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)

        # 點擊actionTst，子視窗就會顯示在主視窗的MaingridLayout中
        self.addWinAction.triggered.connect(self.childShow)

    def childShow(self):
        # 增加子視窗
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "開啟", "C:/", "All Files (*);;Text Files (*.txt)")
        # 在狀態列顯示檔案位址
        self.statusbar.showMessage(file)


class ChildrenForm(QWidget, Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
