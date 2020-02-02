# -*- coding: utf-8 -*- 
'''
    模組名稱：zwQTDraw.py
    預設縮寫：zwdr,範例：import wQTDraw as zwdr
   【簡介】
    zwQT量化軟體，繪圖模組
     
    zw量化，py量化第一品牌
    網站:http://www.ziwang.com zw網站
    py量化QQ總群  124134140   千人大群 zwPython量化&大數據
     
    開發：zw量化開源團隊 2016.04.01 首發
  
'''

import sys, os
import numpy as np
import pandas as pd

import matplotlib as mpl
mpl_agg = 'Qt5Agg'
try:
    import PyQt5
except:
    mpl_agg = 'Qt4Agg'
mpl.use('Qt5Agg')

import matplotlib.pyplot as plt

# from PIL import Image,ImageDraw,ImageFont

import zwSys as zw  # zwQuant
import zwTools as zwt
import zwQTBox as zwx


def my_pyqt_show(qx):
    from my_back_test_show import MainWindow
    from PyQt5.QtWidgets import QMainWindow, QApplication
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow(qx)
    ui.showMaximized()
    # ui.show()
    sys.exit(app.exec_())

# ----
def my_qunt_plot(qx):
    fig = plt.figure(figsize=(10, 6))

    mpl_agg = plt.get_backend().lower()

    if 'tk' in mpl_agg:
        # Option 2
        # TkAgg backend
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
    elif 'qt' in mpl_agg:
        # Option 1
        # QT backend
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()
    elif 'wx' in mpl_agg:
        # Option 3
        # WX backend
        manager = plt.get_current_fig_manager()
        manager.frame.Maximize(True)

    df = pd.read_csv(qx.fn_qxLib, index_col=0, parse_dates=[0])
    # ---top.plt
    # fig = plt.figure(figsize=(20, 15))
    ax1 = fig.add_subplot(111)
    ax1.plot(df['dret'],color='green',label='dret',linewidth=0.5)
    ax1.legend(loc='upper left')
    ax2 = ax1.twinx()
    ax2.plot(df['val'], color='red', label='val', linewidth=2)
    ax2.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

def dr_quant3x_init(qx, w=11, h=6.5, show_max=False):
    ''' zwQT預設繪圖模版quant3x，
    初始化繪圖環境，w、h 是圖形大小尺寸
    
    Args:
        qx (zwDatX): 需要顯示的資料
        w (int): 圖像寬度
        h (int): 圖像高度
        show_max: 全屏繪圖。
            
    :ivar xcod (int): 股票代碼
    '''

    # -----------plt.env.init
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定預設字體 ???
    # myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttf')
    # mpl.rcParams['axes.unicode_minus'] = False #解決保存圖像是負號'-'顯示為方塊的問題
    # Accent,brg, coolwarm, Dark2,rainrow,gnuplot,hot,hsv,jet,prism,raibow, Set1
    # -----------plt.init


    # w = 5;h=5;show_max=True

    fig = plt.figure(figsize=(w, h))
    if show_max == True:

        mpl_agg = plt.get_backend().lower()

        if 'tk' in mpl_agg:
            # Option 2
            # TkAgg backend
            manager = plt.get_current_fig_manager()
            manager.resize(*manager.window.maxsize())
        elif 'qt' in mpl_agg:
            # Option 1
            # QT backend
            manager = plt.get_current_fig_manager()
            manager.window.showMaximized()
        elif 'wx' in mpl_agg:
            # Option 3
            # WX backend
            manager = plt.get_current_fig_manager()
            manager.frame.Maximize(True)


    left, width = 0, 1.0
    p1box = [left, 0.7, width, 0.3]  # [左, 下, 寬, 高] 規定的矩形區域 （全部是0~1之間的數，表示比例）
    # p2box = [left, 0.2, width, 0.5]
    p3box = [left, 0.05, width, 0.50]
    # --set qx.size&pos
    qx.pltTop = fig.add_axes(p1box);
    qx.pltTop2 = qx.pltTop.twinx()
    # qx.pltMid = fig.add_axes(p2box);
    # qx.pltMid2 = qx.pltMid.twinx()
    qx.pltBot = fig.add_axes(p3box);
    qx.pltBot2 = qx.pltBot.twinx()
    # --set label,tick,...
    # qx.pltTop.set_xticks([]);qx.pltTop.set_yticks([])
    qx.pltTop2.set_xticks([]);
    qx.pltTop2.set_yticks([])
    # qx.pltMid2.set_xticks([]);
    # qx.pltMid2.set_yticks([])
    qx.pltBot2.set_xticks([]);
    qx.pltBot2.set_yticks([])


def dr_quant3x00(qx, ktop2, kbot, kmidlst, midSgn0=''):
    '''
    zwQT預設繪圖模版quant3x，
    dr_quant3x(qx,ktop2,kbot,kmidlst,midSgn0=''):
    zw版3x三合一，回溯測試繪圖函數
    【輸入】
        qx (zwQuantx): zwQuantx資料包-全域量化參數變數
        ktop2 (str): Top頂部成交量股票代碼
        kbot (str): Bot底部繪圖列名稱，一般是'val'，資產總價值；資料來源為：qx.qxLib
        kmidlst (list): Mid中部繪圖列名稱清單，為複合表格
          子清單元素1，為股票代碼xcod，其他列名稱，為格式為：
          [[xcod1,nam1,nam2,...],[xcod2,nam1,nam2,...],[xcod3,nam1,nam2,...]]
          注意，kmidlst資料來源為：stkLib[xcod]，包含預處理擴充的資料列
          
        midSgn0(str)，中部繪圖區圖示首碼
           其中，“<xcod>”為特殊符號，表示對應的股票代碼
    【輸出】
        無
    
    '''
    df = pd.read_csv(qx.fn_qxLib, index_col=0, parse_dates=[0]);
    # ---top.plt
    qx.pltTop.plot(df['dret']);
    qx.pltTop.axhline(0, color='black');
    qx.pltTop.legend(['dret'], loc=2)
    if ktop2 != '':
        df2 = zw.stkLib[ktop2];
        df2['kvol'] = df2['dprice'] * df2['volume'] / 1e6
        qx.pltTop2.fill_between(df2.index, df2['kvol'], color='peru')
        qx.pltTop2.legend([ktop2], loc=1, ncol=2)

    # ---bot,plot
    if kbot != '':
        qx.pltBot.plot(df[kbot], color='red');
        qx.pltBot.legend([kbot], loc=2, ncol=2)
    # ---mid,plot
    x10 = [];
    for x5 in kmidlst:
        xcod = x5[0];
        xn9 = len(x5);  # x10.append(xcod);#print('@x',xcod)
        d20 = zw.stkLib[xcod]
        for xc in range(xn9 - 1):
            ksgn = x5[xc + 1];
            css = ksgn;
            if midSgn0 != '':
                if midSgn0 == '<xcod>':
                    css = xcod + '_' + css;
                else:
                    css = midSgn0 + '_' + css;
            x10.append(css);
            qx.pltMid.plot(d20[ksgn])
    # x10=x10.sort;
    qx.pltMid.legend(x10, loc='best', ncol=5)
    plt.show()


def dr_quant3x(qx, ktop2, kbot, kmidlst, midSgn0='', inxSgn0=''):
    '''
    zwQT預設繪圖模版quant3x，
    dr_quant3x(qx,ktop2,kbot,kmidlst,midSgn0=''):
    zw版3x三合一，回溯測試繪圖函數
    【輸入】
        qx (zwQuantx): zwQuantx資料包-全域量化參數變數
        ktop2 (str): Top頂部成交量股票代碼
        kbot (str): Bot底部繪圖列名稱，一般是'val'，資產總價值；資料來源為：qx.qxLib
        kmidlst (list): Mid中部繪圖列名稱清單，為複合表格
          子清單元素1，為股票代碼xcod，其他列名稱，為格式為：
          [[xcod1,nam1,nam2,...],[xcod2,nam1,nam2,...],[xcod3,nam1,nam2,...]]
          注意，kmidlst資料來源為：stkLib[xcod]，包含預處理擴充的資料列
          
        midSgn0(str)，中部繪圖區圖示首碼
           其中，“<xcod>”為特殊符號，表示對應的股票代碼
       inxSgn0,大盤指數名稱，為空，不顯示大盤指數圖形    
    【輸出】
        無
    
    '''
    df = pd.read_csv(qx.fn_qxLib, index_col=0, parse_dates=[0])
    # ---top.plt
    qx.pltTop.plot(df['dret']);
    qx.pltTop.axhline(0, color='black');
    qx.pltTop.legend(['dret'], loc=2)
    if ktop2 != '':
        df2 = zw.stkLib[ktop2];
        if 'volume' not in df2.columns:
            df2['kvol'] = df2['dprice']
        else:
            df2['kvol'] = df2['dprice'] * df2['volume'] / 1e6
        # qx.pltTop2.fill_between(df2.index, df2['kvol'], color='peru')
        qx.pltTop2.plot(df2.index, df2['kvol'], color='peru')

        qx.pltTop2.legend([ktop2], loc=1, ncol=2)

    # ---bot,plot
    if kbot != '':
        qx.pltBot.plot(df.index,df[kbot], color='red');
        qx.pltBot.legend([kbot], loc=2, ncol=2)
    # ---stkInx，大盤指數資料
    if (qx.stkInxCode != '') and (inxSgn0 != ''):
        ksgn = qx.stkInxPriceName;  # 大盤指數資料列名稱，預設是:close
        qx.pltBot2.plot(zw.stkInxLib[ksgn], color='blue');
        qx.pltBot2.legend([inxSgn0], loc=4, ncol=2)

        # ---mid,plot
    # x10 = [];
    # for x5 in kmidlst:
    #     xcod = x5[0];
    #     xn9 = len(x5);  # x10.append(xcod);#print('@x',xcod)
    #     d20 = zw.stkLib[xcod]
    #     for xc in range(xn9 - 1):
    #         ksgn = x5[xc + 1];
    #         css = ksgn;
    #         if midSgn0 != '':
    #             if midSgn0 == '<xcod>':
    #                 css = xcod + '_' + css;
    #             else:
    #                 css = midSgn0 + '_' + css;
    #         x10.append(css);
    #         qx.pltMid.plot(d20[ksgn])
    # # x10=x10.sort;
    # qx.pltMid.legend(x10, loc='best', ncol=5)
    plt.show()
