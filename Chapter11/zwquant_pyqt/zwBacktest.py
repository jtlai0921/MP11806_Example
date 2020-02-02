# -*- coding: utf-8 -*- 
'''
    模組名稱：zwBacktest.py
    預設縮寫：zwbt,範例：import zwBacktest as zwbt
   【簡介】
    zwQT量化軟體，回溯測試模組
     
    zw量化，py量化第一品牌
    網站:http://www.ziwang.com zw網站
    py量化QQ總群  124134140   千人大群 zwPython量化&大數據
     
    開發：zw量化開源團隊 2016.04.01 首發
  
'''

import numpy as np
import math
import pandas as pd
import matplotlib as mpl
import matplotlib.gridspec as gridspec
# from pinyin import PinYin

from dateutil.parser import parse
from dateutil import rrule
import datetime as dt

# zwQuant
import zwSys as zw
import zwTools as zwt
import zwQTBox as zwx
import zwQTDraw as zwdr
import zw_talib as zwta

from numba import *


# -------------

# -------------    zw.Quant.BackTest

def bt_init(xlst, rdat, prjNam, money0=1000000):
    '''
    qt_init(qx,xlst,rdat):
        初始化zw量化參數，stk股票記憶體中資料庫等
    【輸入】：
        xlst (list): 股票代碼列表，例如：xlst=['aeti','egan','glng','simo']，xlst=['002739','300239']   
        rdat (str): 股票資料目錄,可直接使用 zwDat的中美股票資料:\\zwdat\\cn\\Day\\，\\zwdat\\us\\Day\\，
        prjNam (str): 項目名稱
        money0 (int): 啟動資金，預設是：1000000(100w)
        
    【輸出】：
        qx (zwQuantx): 程式化全域變數qx
        '''
    # qx=zw.zwQuantX('tur',1000000) #100w
    qx = zw.zwQuantX(prjNam, money0)  # 100w

    # ------設定各種價格模式：
    #    priceWrk，策略分析時，使用的股票價格，一般是：dprice，複權收盤價
    #    priceBuy，買入/賣出的股票價格，一般是：kprice，一般採用次日的複權開盤價
    #    priceCalc，最後結算使用的股票價格，一般是：adj close，複權收盤價
    qx.priceCalc = 'close'  # qx.priceCalc='adj close'
    qx.priceWrk = 'dprice'
    qx.priceBuy = 'kprice'
    # ----------設定繪圖&資料輸出格式
    mpl.style.use('seaborn-whitegrid')
    pd.set_option('display.width', 450)
    # -----設定資料原始目錄等場所，讀取股票資料，stkLib
    qx.rdat = rdat
    zwx.stkLibRd(xlst, rdat)
    #
    # 大盤指數.設定
    # zw.stkInxLib=None  #全域變數，大盤指數，記憶體股票資料庫
    qx.stkInxRDat = '\\zwdat\\cn\\xday\\'  # 大盤指數資料來源路徑
    qx.stkInxPriceName = 'close'  # 大盤指數資料列名稱，預設是:close
    # 大盤指數代碼,名稱拼音,中文名稱
    # qx.stkInxCode,qx.stkInxName,qx.stkInxCName='000001','sh001','上證指數'

    #  讀取股票資料，
    xtim0 = parse('9999-01-01')
    xtim9 = parse('1000-01-01')
    zw.stkLibTim = {}  # 記錄每檔股票的交易起點時間和終點時間，終點作為清倉判斷標誌。
    for xcod in zw.stkLibCode:
        xt0, xt9 = zwx.stkLibGetTimX(xcod)
        xcod_tim0 = xt0.strftime('%Y-%m-%d')
        xcod_tim9 = xt9.strftime('%Y-%m-%d')
        zw.stkLibTim[xcod] = [xcod_tim0, xcod_tim9]
        if xtim0 > xt0: xtim0 = xt0
        if xtim9 < xt9: xtim9 = xt9

    xtim0 = xtim0.strftime('%Y-%m-%d')
    xtim9 = xtim9.strftime('%Y-%m-%d')
    qx.qxTimSet(xtim0, xtim9)

    if qx.debugMod > 0:
        print(xtim0, xtim9, '\nstkCode', zw.stkLibCode)  # zwx.stkLibPr()

    return qx


def zwBackTest100(qx):
    '''
    zwBackTest100(qx):
    zwQT回溯測試子函數，測試一檔股票xcod，在指定時間xtim的回溯表現資料
    會調用qx.staFun指定的策略分析函數，獲取當前的股票交易數目 qx.stkNum
    並且根據股票交易數目 qx.stkNum，判定是不是有效的交易策略
    【輸入】
        qx (zwQuantx): zwQuantx數據包
        #qx.stkCode，當前交易的股票代碼
        #qx.xtim，當前交易的時間
    【輸出】
         無
         '''

    # ----運行策略函數，進行策略分析
    qx.stkNum = qx.staFun(qx)
    # ----
    if qx.stkNum != 0:
        # ----檢查，是不是有效交易
        xfg, qx.xtrdChk = zwx.xtrdChkFlag(qx)
        if xfg:
            # ----如果是有效交易，加入交易清單
            zwx.xtrdLibAdd(qx)
            # qx.prQCap()
        elif qx.trdNilFlag:
            zwx.xtrdLibNilAdd(qx)


def zwBackTest(qx):
    '''
    zwQuant，回溯測試主程式
    【輸入】
    	qx (zwQuantx): zwQuantx封包
    	
    【輸出】
         無
    '''
    # 增加資料來源波動率參數  # 就是增加一列dvix資料
    zwx.stkLibSetDVix()
    # 計算回溯時間週期，也可以在此，根據nday調整回溯週期長度
    # 或者在 qt_init資料初始化時，通過qx.qxTimSet(xtim0,xtim9)，設定回溯週期長度
    nday = qx.periodNDay
    if qx.debugMod > 0:
        xcod = zw.stkLibCode[0]
        print(zw.stkLib[xcod].tail())
        print('nday', nday)
        fss = 'tmp\\' + qx.prjName + '_' + xcod + '.csv'
        zw.stkLib[xcod].to_csv(fss)
        # --------------
    # 按時間迴圈，進行回溯測試
    for tc in range(nday):
        tim5 = qx.DTxtim0 + dt.timedelta(days=tc)
        if hasattr(qx,'timFun'):
            qx.timFun(qx,tim5)  # 運行綁定的關於某個時間點的主函數

        xtim = tim5.strftime('%Y-%m-%d')  # print('tc',tc,xtim)
        # 每個測試時間點，開始時，清除qx相關參數
        qx.qxTim0SetVar(xtim)  # qx.prQxUsr() #qx.xtim=xtim
        xpriceFlag = False  # 有效交易標誌Flag
        # 按設定的股票代碼列表，迴圈進行回溯測試
        for xcod in zw.stkLibCode:
            qx.stkCode = xcod  # print('xcod',xcod)
            # xdatWrk是當前xcod，=stkLib[xcod]
            # xbarWrk是當前時間點的stkLib[xcod]
            # 注意,已經包括了，qt_init裡面的擴充資料列
            qx.xbarWrk, qx.xdatWrk = zwx.xbarGet8TimExt(xcod, qx.xtim)
            # print(xcod,'xbar\n',qx.xbarWrk)
            if not qx.xbarWrk[qx.priceWrk].empty:
                # -----dvix 波動率檢查
                dvix = zwx.stkGetVars(qx, 'dvix')  # dvixFlag=False
                dvixFlag = zwt.xinEQ(dvix, qx.dvix_k0, qx.dvix_k9) or (dvix == 0) or (np.isnan(dvix))
                if dvixFlag:
                    xpriceFlag = True
                    # 調用回溯副程式，如果是有效交易，設定成功交易標誌xtrdFlag
                    zwBackTest100(qx)
                else:
                    print('@dvix', xcod, xtim, dvix)
                    pass

        # 如果所有股票代碼清單迴圈完畢，成功交易標誌為真
        # 在當前測試時間點終止，設定有關交易參數
        if xpriceFlag:
            qx.wrkNDay += 1
            qx.qxTim9SetVar(qx.xtim)
    # print('')
    qx.update_usr_qxLib(qx,qx.qxLib)
    # print('')
    # print('')
    # print('')
    # print('')



if __name__ == '__main__':
    import line_profiler
    import sys

    prof = line_profiler.LineProfiler(bt_init)
    prof.enable()  # 開始性能分析
    xlst = ['orcl-2000']
    bt_init(xlst, 'dat\\', 'sma', 10000)
    prof.disable()  # 停止性能分析
    prof.print_stats(sys.stdout)


    # if 'builtins' not in dir() or not hasattr(builtins, 'profile'):
    #     import builtins
    #     def profile(func):
    #         def inner(*args, **kwargs):
    #             return func(*args, **kwargs)
    #         return inner
    #     builtins.__dict__['profile'] = profile
