import sys
import random
import matplotlib


import matplotlib as mpl
mpl_agg = 'Qt5Agg'
try:
    import PyQt5
except:
    mpl_agg = 'Qt4Agg'
mpl.use('Qt5Agg')

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

class MyMplCanvas(FigureCanvas):
    '''FigureCanvas的最終的父類別其實是QWidget。'''

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        # 設定中文顯示
        plt.rcParams['font.family'] = ['SimHei']  # 正常顯示中文標籤
        # plt.rcParams['font.family'] = ['SimSun']  # 正常顯示中文標籤
        plt.rcParams['axes.unicode_minus'] = False  # 正常顯示負號

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一個figure
        self.fig.set_tight_layout(True)


        self.axes = self.fig.add_subplot(111)  # 建立一個子圖，如果要建立複合圖，可在這裡修改

        self.axes.hold(False)  # 每次繪圖時不保留上一次繪圖的結果

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定義FigureCanvas的尺寸策略，意思是設定FigureCanvas，使其盡可能地向外填充空間。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    '''繪製靜態圖，可在這裡定義自己的繪圖邏輯'''

    def start_static_plot(self,qx=None):
        if qx != None: # 與zwquant結合，qx是zwquant的一個實例物件
            df = qx.qxLib.copy()
            df.set_index('date',inplace=True)
            df.rename_axis(lambda x: pd.to_datetime(x),inplace=True)
            ax1 = self.axes
            ax1.plot(df['dret'], color='green', label='dret', linewidth=0.5)
            ax1.legend(loc='upper left')
            ax2 = ax1.twinx()
            ax2.plot(df['val'], color='red', label='val', linewidth=2)
            ax2.legend(loc='upper right')
        else:# 用於測試，不需要zwquant也能執行，方面快速開發自己的GUI介面
            t = arange(0.0, 3.0, 0.01)
            s = sin(2 * pi * t)
            self.axes.plot(t, s)
            self.axes.set_ylabel('靜態圖：Y軸')
            self.axes.set_xlabel('靜態圖：X軸')
            self.axes.grid(True)

    '''繪製動態圖'''
    def start_dynamic_plot(self, *args, **kwargs):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)  # 每隔一段時間就會觸發一次update_figure函數
        timer.start(1000)  # 觸發的時間間隔為1秒

    '''動態圖的繪圖邏輯可以在這裡修改'''
    def update_figure(self):
        self.fig.suptitle('測試動態圖')
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.axes.set_ylabel('動態圖：Y軸')
        self.axes.set_xlabel('動態圖：X軸')
        self.axes.grid(True)
        self.draw()


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        # self.mpl.start_static_plot() # 如果在初始化時就呈現靜態圖，請去掉這行註解
        # self.mpl.start_dynamic_plot() # 如果在初始化時就呈現靜態圖，請去掉這行註解
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.mpl.start_static_plot()  # 測試靜態圖效果
    # ui.mpl.start_dynamic_plot() # 測試動態圖效果
    ui.show()
    app.exec_()
