# -*- coding: utf-8 -*-

'''
Module implementing MainWindow.
'''

import pandas as pd
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Ui_fundFOF import Ui_MainWindow
# from PandasModel import PandasModel
from Plotly_PyQt5 import Plotly_PyQt5


class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    Class documentation goes here.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        '''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.plotly_pyqt5 = Plotly_PyQt5()

        '''手動調整視窗控制項的大小，使其更加美觀'''
        self.widget_parameter_tree.setMaximumWidth(300)
        self.widget_parameter_tree.setMinimumWidth(200)
        self.QWebEngineView_ProductVsHs300.setMinimumHeight(400)  #500
        self.tabWidget.setMinimumHeight(400)


        '''顯示parametertree，這裡透過佈局管理器把ParameterTree間接地嵌套入Widget視窗'''
        from mypyqtgraph import  p
        from pyqtgraph.parametertree import  ParameterTree

        t = ParameterTree()
        t.setParameters(p, showTop=False)
        t.setHeaderLabels(["參數", "數值"])
        # t.setWindowTitle('pyqtgraph example: Parameter Tree')
        layout = QtGui.QGridLayout()
        self.widget_parameter_tree.setLayout(layout)
        layout.addWidget(
            QtGui.QLabel("千石資本-和聚光明1號資產管理計畫基本資訊"), 0, 0, 1, 1)
        layout.addWidget(t)

        '''顯示繪圖函數'''
        self.QWebEngineView_ProductVsHs300.load(
            QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_product_vs_hs300()))
        self.QWebEngineView_LagestBack.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_lagest_back()))
        self.QWebEngineView_PeriodReturn.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_period_return()))
        self.QWebEngineview_MonthReturn.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_month_return()))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.showMaximized()
    sys.exit(app.exec_())
