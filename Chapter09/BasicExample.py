# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import pandas
import numpy
import sys
from qtpandas.excepthook import excepthook

# Use QtGui from the compat module to take care if correct sip version, etc.
from qtpandas.compat import QtGui
from qtpandas.models.DataFrameModel import DataFrameModel
from qtpandas.views.DataTableView import DataTableWidget
# from qtpandas.views._ui import icons_rc

sys.excepthook = excepthook # 設定PyQt的異常鉤子，基本上在本例沒什麼作用

# 建立一個空的模型，該模型用來儲存與處理資料
model = DataFrameModel()

# 建立一個應用程式顯示表格
app = QtGui.QApplication([])
widget = DataTableWidget() # 建立一個空的表格，用來呈現資料
widget.resize(500, 300) # 調整Widget的大小
widget.show()
# 讓表格繫結模型，也就是呈現模型的內容
widget.setViewModel(model)

# 建立測試資料
data = {
    'A': [10, 11, 12],
    'B': [20, 21, 22],
    'C': ['Peter Pan', 'Cpt. Hook', 'Tinkerbell']
}
df = pandas.DataFrame(data)

# 下面兩列用來測試委託是否成立
df['A'] = df['A'].astype(numpy.int8) # A欄資料格式變成整數
df['B'] = df['B'].astype(numpy.float16) # B欄資料格式變成浮點數

# 在模型中填入資料df
model.setDataFrame(df)

# 啟動程式
app.exec_()
