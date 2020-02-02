# -*- coding: utf-8 -*-

'''
Module implementing MainWindow.
'''

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from Ui_my_back_test_show import Ui_MainWindow
import pickle
import numpy as np
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    Class documentation goes here.
    '''

    def __init__(self, qx=None, parent=None):
        '''
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        '''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        if qx != None: # 與zwquant結合，qx是zwquant的一個實例物件
            self.qx = qx
            self.show_result(self.qx)
            self.matplotlibwidget_static.mpl.start_static_plot(self.qx)
        else: # 用於測試，不需要zwquant也能執行，以利於快速開發自己的GUI介面
            self.show_result()
            self.matplotlibwidget_static.mpl.start_static_plot()

    def show_result(self, qx=None):

        if qx != None: # 回測的話就傳入回測的資料
            list_result = qx.result_info
            pickle_file = open('my_list.pkl', 'wb')  # 以 wb 的方式寫入
            pickle.dump(list_result, pickle_file)  # 對pickle_file寫入my_list
            pickle_file.close()
        else: # 不跑回測的話就讀取測試資料
            pickle_file = open('my_list.pkl', 'rb')  # 以 rb 的方式讀取
            list_result = pickle.load(pickle_file)  # 讀取以pickle方式寫入的檔案pickle_file
            pickle_file.close()

        list_result.append(['', ''])  # 湊足24*2（原來23*2），
        len_index = 6
        len_col = 8
        list0, list1, list2, list3 = [list_result[6 * i:6 * i + 6] for i in range(0, 4)]
        arr_result = np.concatenate([list0, list1, list2, list3], axis=1)
        self.tableWidget.setRowCount(len_index) # 設定列數
        self.tableWidget.setColumnCount(len_col) # 設定行數
        self.tableWidget.setHorizontalHeaderLabels(['回測內容', '回測結果'] * 4) # 設定垂直方向的標題
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in range(1, len_index + 1)]) # 設定水平方向的標題


        for index in range(len_index):
            for col in range(len_col):
                self.tableWidget.setItem(index, col, QTableWidgetItem(arr_result[index, col]))
        self.tableWidget.resizeColumnsToContents() # 根據內容調整行寬

    @pyqtSlot()
    def on_pushButton_show_dataPre_clicked(self):
        '''
        Slot documentation goes here.
        '''
        if hasattr(self, 'qx'):# 與zwquant結合，才進行下一步
            if hasattr(self.qx,'path_dataPre'):
                os.system(np.random.choice(self.qx.path_dataPre)) # 隨機選取資料預先處理的檔案結果，並開啟

    @pyqtSlot()
    def on_pushButton_show_money_flow_clicked(self):
        '''
        Slot documentation goes here.
        '''
        if hasattr(self, 'qx'): # 與zwquant結合，才進行下一步
        	os.system(self.qx.fn_qxLib)

    @pyqtSlot()
    def on_pushButton_show_trade_flow_clicked(self):
        '''
        Slot documentation goes here.
        '''
        if hasattr(self, 'qx'):# 與zwquant結合，才進行下一步
        	os.system(self.qx.fn_xtrdLib)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.showMaximized()
    # ui.show()
    sys.exit(app.exec_())
