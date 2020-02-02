# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class EventFilter(QDialog):
    def __init__(self, parent=None):
        super(EventFilter, self).__init__(parent)
        self.setWindowTitle("事件篩選程式")

        self.label1 = QLabel("請點擊")
        self.label2 = QLabel("請點擊")
        self.label3 = QLabel("請點擊")
        self.LabelState = QLabel("test")

        self.image1 = QImage("images/cartoon1.ico")
        self.image2 = QImage("images/cartoon1.ico")
        self.image3 = QImage("images/cartoon1.ico")

        self.width = 600
        self.height = 300

        self.resize(self.width, self.height)

        # self.label1.installEventFilter(self)
        # self.label2.installEventFilter(self)
        # self.label3.installEventFilter(self)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(self.label1, 500, 0)
        mainLayout.addWidget(self.label2, 500, 1)
        mainLayout.addWidget(self.label3, 500, 2)
        mainLayout.addWidget(self.LabelState, 600, 1)
        self.setLayout(mainLayout)

    def eventFilter(self, watched, event):
        print(type(watched))
        if watched == self.label1: # 只過濾label1的點擊事件，重寫其行為，並忽略其他事件
            if event.type() == QEvent.MouseButtonPress: # 這裡過濾滑鼠按下事件，重寫其行為
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.LabelState.setText("按下滑鼠左鍵")
                elif mouseEvent.buttons() == Qt.MidButton:
                    self.LabelState.setText("按下滑鼠中間鍵")
                elif mouseEvent.buttons() == Qt.RightButton:
                    self.LabelState.setText("按下滑鼠右鍵")

                '''轉換圖片大小'''
                transform = QTransform()
                transform.scale(0.5, 0.5)
                tmp = self.image1.transformed(transform)
                self.label1.setPixmap(QPixmap.fromImage(tmp))
            if event.type() == QEvent.MouseButtonRelease: # 這裡過濾滑鼠釋放事件，重寫其行為
                self.LabelState.setText("釋放滑鼠按鈕")
                self.label1.setPixmap(QPixmap.fromImage(self.image1))
        return QDialog.eventFilter(self, watched, event) # 其他情況會返回系統預設的事件處理方法


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = EventFilter()
    app.installEventFilter(dialog)
    dialog.show()
    sys.exit(app.exec_())
