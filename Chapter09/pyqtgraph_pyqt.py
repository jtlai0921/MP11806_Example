# -*- coding: utf-8 -*-

'''
Module implementing MainWindow.
'''

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
import pyqtgraph as pg
from Ui_pyqtgraph_pyqt import Ui_MainWindow
import numpy as np


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

        pg.setConfigOption('background', '#f0f0f0')  # 設定背景為灰色
        pg.setConfigOption('foreground', 'd')  # 設定前景（包括坐標軸，線條，文本等等）為黑色。

        pg.setConfigOptions(antialias=True) # 使曲線看起來更光滑，而不是鋸齒狀
        # pg.setConfigOption('antialias',True) # 等價於上一句，所不同之處在於setconfigOptions可以設定多個參數，
		# 而setConfigOption一次只能設定一個參數。
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        '''
        Slot documentation goes here.
        '''
        self.pyqtgraph1.clear() # 清空裡面的內容，否則會發生重複繪圖的結果

        '''第一種繪圖方式'''
        self.pyqtgraph1.addPlot(title="繪圖一條線", y=np.random.normal(size=100), pen=pg.mkPen(color='b', width=2))

        '''第二種繪圖方式'''
        plt2 = self.pyqtgraph1.addPlot(title='繪製多條線')

        plt2.plot(np.random.normal(size=150), pen=pg.mkPen(color='r', width=2), name="Red curve") # pg.mkPen的使用方法，設定線條顏色為紅色，寬度為2。
        plt2.plot(np.random.normal(size=110) + 5, pen=(0, 255, 0), name="Green curve")
        plt2.plot(np.random.normal(size=120) + 10, pen=(0, 0, 255), name="Blue curve")


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        '''
        Slot documentation goes here.
        '''
        '''如果沒有進行第一次繪圖，就開始繪圖，然後做繪圖標記，否則就什麼都不做'''
        try:
            self.first_plot_flag # 檢測是否進行過第一次繪圖。
        except:

            plt = self.pyqtgraph2.addPlot(title='繪製長條圖')
            x = np.arange(10)
            y1 = np.sin(x)
            y2 = 1.1 * np.sin(x + 1)
            y3 = 1.2 * np.sin(x + 2)

            bg1 = pg.BarGraphItem(x=x, height=y1, width=0.3, brush='r')
            bg2 = pg.BarGraphItem(x=x + 0.33, height=y2, width=0.3, brush='g')
            bg3 = pg.BarGraphItem(x=x + 0.66, height=y3, width=0.3, brush='b')

            plt.addItem(bg1)
            plt.addItem(bg2)
            plt.addItem(bg3)

            self.pyqtgraph2.nextRow()

            p4 = self.pyqtgraph2.addPlot(title="參數圖+顯示格子")
            x = np.cos(np.linspace(0, 2 * np.pi, 1000))
            y = np.sin(np.linspace(0, 4 * np.pi, 1000))
            p4.plot(x, y, pen=pg.mkPen(color='d', width=2))
            p4.showGrid(x=True, y=True) # 顯示格子

            self.first_plot_flag = True # 第一次繪圖後進行標記

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
