# -*- coding: utf-8 -*- 
#  
#  zwQuantToolBox 2016
#  zw量化開源工具箱系列軟體 
#  http://www.ziwang.com,Python量化第一品牌 
#  
#  檔案名:zwSys.py
#  說明：import zwSys as zw
#       設定常用變數,類定義、初始化函數
#  
# =====================================  

import sys, os
import numpy as np
import pandas as pd
import tushare as ts
# import talib as ta

import datetime as dt
from dateutil.parser import parse
from dateutil import rrule

import zwTools as zwt
import zwQTBox as zwx

# ----zw.var...
__version__ = '2016.M5'

# 顏色變數
# 注意，opecv內部的顏色不是常用的RGB模式，而是採用BGR排列
_corBlack = (0, 0, 0)
_corWhite = (255, 255, 255)
_corGray = (128, 128, 128)
_corBlue = (0, 0, 255)
_corGreed = (0, 255, 0)
_corRed = (255, 0, 0)

_corRedCV = (0, 0, 255)
_corBlueCV = (255, 0, 0)

# ----init

# ----init.dir 目錄設定

_rdat0 = "\\zwDat\\"
_rdatCN = _rdat0 + "cn\\"
_rdatUS = _rdat0 + "us\\"
_rdatInx = _rdat0 + "inx\\"
_rdatMin = _rdat0 + "min\\"
_rdatTick = _rdat0 + "tick\\"
_rdatTickReal = _rdat0 + "tickreal\\"

_rdatZW = _rdat0 + "zw\\"

_rTmp = "\\zwPython\\zwQuant\\demo\\tmp\\"

# ----init.stk.var 初始化數據設定
_stkTradeTaxi = 0.002
_stkRateRF = 0.03
_stkKRateBreak = 10

# ---qx.misc.xxx
qxMinName = ['time', 'open', 'high', 'low', 'close', 'volume', 'amount', 'vol_norm', 'amo_norm', 'vol_buy', 'amo_buy',
             'vol_sell', 'amo_sell']
qxTickName = ['time', 'price', 'change', 'volume', 'amount', 'type']
qxTickNameNew = ['date', 'price', 'change', 'volume', 'amount', 'type']
#
qxKPriceName = ['open', 'high', 'low', 'close', 'adj close', 'dprice', 'kprice']
# ---qxLib.xxxx
ohlcLst = ['open', 'high', 'low', 'close']
ohlcExtLst = ['date', 'open', 'high', 'low', 'close', 'volume', 'adj close']
xtrdName = ['date', 'ID', 'mode', 'code', 'dprice', 'num', 'kprice', 'sum', 'cash']
xtrdNil = ['', '', '', '', 0, 0, 0, 0, 0]
qxLibName = ['date', 'stkVal', 'cash', 'dret', 'val', 'downLow', 'downHigh', 'downDay', 'downKMax']
qxLibNil = ['', 0, 0, 0, 0, 0, 0, 0, 0]  # xBars:DF

stkInxLib = None  # 全域變數，大盤指數，記憶體股票資料庫
stkLib = {}  # 全域變數，相關股票的交易資料，記憶體股票資料庫
stkLibCode = []  # 全域變數，相關股票的交易代碼，記憶體股票資料庫
stkCodeTbl = None  # 全域變數，相關股票的交易代碼，名稱對照表


# ----class

class zwXBar(object):
    ''' 記錄每筆交易Bar資料包
    
    Args:
        Csv資料來源。
        (datetime, open, close, high, low, volume)
        
    :ivar xtim: 交易時間
    :ivar mode: 買or賣
    :ivar code: 股票代碼
    :ivar num: 交易量
    :ivar price: 成交價
    :ivar sum： 交易總額
    '''

    def __init__(self, xtim, mode='', code='', num=0, price=0):
        self.time = xtim
        self.mode = mode  # '',buy,sell
        self.code = code
        self.num = num
        self.price = price
        self.sum = price * num

    def prXBar(self):
        print('')
        print('date,', self.time)
        print('mode,', self.mode)
        print('code,', self.code)
        print('num,', self.num)
        print('price,', self.price)
        print('sum,', self.sum)


class zwQuantX(object):
    ''' 定義了zwQuant量化交易所需的各種變數參數、相關的類函數
    
    Args:
        csv資料來源。
        (datetime, open, close, high, low, volume)
        '''

    def __init__(self, prjNam, dbase0=10000):
        ''' 預設初始化函數
        Args:
            prjNam (list): 項目名稱
            dbase0 (int): 啟動資金
        '''

        # taxi,傭金，扣稅
        self.prjName = prjNam
        self.fn_qxLib = 'tmp\\' + prjNam + '_qxLib.csv'
        self.fn_xtrdLib = 'tmp\\' + prjNam + '_xtrdLib.csv'
        # ---
        self.mbase = dbase0
        self.money = dbase0
        #
        xtim0 = ''
        xtim9 = ''
        self.xtim0 = xtim0
        self.xtim9 = xtim9
        self.xtim = xtim0
        self.DTxtim0 = None
        self.DTxtim9 = None
        if self.xtim0 != '': self.DTxtim0 = parse(self.xtim0)
        if self.xtim9 != '': self.DTxtim9 = parse(self.xtim9)

        #
        self.stkKCash = 0.9  # 預設，每次買入90%的資金
        self.stkNum0 = 100  # 每手交易，預設最少10股
        self.stkNum9 = 200000  # 每手交易，預設最多20000股
        self.rfRate = 0  # 無風險利率，例如計算夏普指數sharp radio
        self.dvix_k0 = 80  # dvix波動率下限
        self.dvix_k9 = 120  # dvix波動率上限
        # stkInx,大盤指數
        self.stkInxCode = ''  # 大盤指數代碼
        self.stkInxName = ''  # 大盤指數名稱，拼音
        self.stkInxCName = ''  # 大盤指數中文名稱，拼音
        self.stkInxPriceName = 'close'  # 大盤指數資料列名稱，預設是:close
        self.stkInxRDat = ''  # 大盤指數資料來源路徑
        # ---wrk.stk.var

        self.stkCName = ''
        self.stkName = ''
        self.stkCode = ''
        self.stkNum = 0
        self.stkPrice = 0
        # self.dcash=0
        self.trdNilFlag = False  # 空頭交易標誌
        self.trdCnt = 0
        self.qxID = 0  # ID=date+'_'+trdCnt(0000)
        self.rdat = ''  # 股票資料檔案目錄
        # self.rxdat=''    #指數檔目錄

        #
        self.periodMode = 'day'  # day,hour,min
        self.periodCount = 0
        self.periodNWork = 0  # 工作日(時)長
        # self.periodNDay=rrule.rrule(rrule.DAILY,dtstart=self.DTxtim0,until=self.DTxtim9).count()
        self.periodNDay = None
        self.wrkNDay = 0
        # -----ret
        self.mvalSum = 0
        self.mvalGet = 0
        self.mvalCash = 0
        self.mvalOther = 0  # 其他資產價值，例如股票價值stkVal
        self.kretYear = 0
        self.kretDay = 0
        self.kretDayStd = 0
        # ---
        self.pltTop = None
        self.pltTop2 = None
        self.pltMid = None
        self.pltMid2 = None
        self.pltBot = None
        self.pltBot2 = None
        # ---
        self.staFun = ''
        self.staVars = [0, '', '']  # 策略變數輸入資料清單
        self.staName = ''

        # ---drawdown.var
        self.downHigh = 0
        self.downLow = 0
        self.downHighTime = None
        self.downMaxDay = 0
        self.downKMax = 0

        # ---qxLib.xxx.init
        # xBarName=['date','ID','mode','code','num','price','sum']
        # qxLibName=['date','ID','stkVal','cash','dret','val']
        self.qxLib = pd.DataFrame(columns=qxLibName, index=['date'])  # 所有交易記錄清單清單
        self.qxLib.dropna(inplace=True)
        self.xtrdLib = pd.DataFrame(columns=xtrdName, index=['date'])  # 所有xBars股票交易記錄清單清單
        self.xtrdLib.dropna(inplace=True)
        self.xtrdNilLib = pd.DataFrame(columns=xtrdName, index=['date'])  # 所有Nil空頭交易記錄清單清單
        self.xtrdNilLib.dropna(inplace=True)
        self.qxUsr = pd.Series(index=qxLibName)  # 使用者資產資料
        self.qxUsrStk = {}  # 使用者持有的股票資產資料
        self.xbarWrk = None
        self.xdatWrk = None
        self.xtrdChk = None

        self.result_info = [] # 記錄輸出結果資訊，用來pyqt輸出
        self.path_dataPre = [] # 記錄資料預處理存儲的path
        self.pyqt_mode_flag = False # 預設非pyqt窗口輸出結果

        # ----misc
        # debug
        # ',__name__,',@fun:',sys._getframe().f_code.co_name)
        # 上級主叫函數 sys._getframe().f_back.f_code.co_name
        self.debugMod = 0  # 調試Mod，0：不調試；1：主模組，',__name__=__main__；3：子模組 5；

        # ------設定各種環境的價格模式：
        #    priceWrk，策略分析時，使用的股票價格，一般是：dprice，複權開盤價
        #    priceBuy，買入/賣出的股票價格，一般是：kprice，一般採用次日的複權開盤價
        #    priceCalc，最後結算使用的股票價格，一般是：adj close，複權收盤價
        #    qxKPriceName=['open','high','low','close','adj close','dprice','kprice']
        self.priceWrk = 'dprice'
        self.priceBuy = 'kdprice'
        self.priceCalc = 'adj close'
        #
        # -----init.set

    def qxTimSet(self, xtim0, xtim9):
        ''' 設定時間參數
           
        Args:
            xtim0 (str): 起始時間
            xtim9 (str): 截止時間
        '''

        self.xtim0 = xtim0
        self.xtim9 = xtim9
        self.xtim = xtim0
        self.DTxtim0 = parse(self.xtim0)
        self.DTxtim9 = parse(self.xtim9)
        date_range = pd.date_range(self.xtim0, self.xtim9, freq='D')
        self.periodNDay = date_range.shape[0]
        # self.periodNDay=rrule.rrule(rrule.DAILY,dtstart=self.DTxtim0,until=self.DTxtim9).count()

    def qxTim0SetVar(self, xtim):
        ''' 回溯測試時間點開始，初始化相關參數
            
        '''

        self.xtim = xtim
        self.qxUsr['date'] = xtim
        # self.trdCnt=0
        self.qxID = 0

    def qxTim9SetVar(self, xtim):
        ''' 回溯測試時間點結束，整理相關資料
          
        '''

        self.xtim = xtim
        # self.qxUsr['date'] = xtim
        zwx.xusrUpdate(self)
        # self.qxLib.append(self.qxUsr.T,ignore_index=True)
        self.qxLib = self.qxLib.append(self.qxUsr, ignore_index=True)
        # self.qxLib.dropna(inplace=True)

    def update_usr_qxLib(self,qx,qxLib):
        '''輸入qx,qxLib
        修改qxLib的dret,downLow,downHigh,downKMax，並進行更新（downDay暫時沒有修改）。
        輸出變更後的qxLib'''
        df = qxLib
        df['dret'] = df.val.pct_change()
        df['downLow'] = df.val.cummin()
        df['downHigh'] = df.val.cummax()

        '''計算最大回撤'''
        _temp = df['val'] / df['downHigh']
        df['downKMax'] = _temp -1
        self.downKMax = df['downKMax'].iloc[-1]

        '''計算最長回撤的天數'''
        group = df.groupby(df.downHigh)
        qx.downMaxDay = group['downDay'].count().max()

        '''計算回撤的最高點位'''
        print('idxmax before = ')
        idxmax = df.val.idxmax()
        print('idxmax after = ', idxmax)
        qx.downHigh = df.iloc[idxmax, :]['val']

        '''計算回撤的最高點位時間'''
        qx.downHighTime = df.iloc[idxmax,:]['date']

        '''計算回撤的最低點位'''
        qx.downLow = df.downLow.min()

        '''更新qxLib'''
        qx.qxLib = df
        return df


    def qxIDSet(self):
        ''' 生成訂單流水號編碼ID
           #ID=prjName+'_'+trdCnt(000000)
        '''

        self.trdCnt += 1
        nss = '{:06d}'.format(self.trdCnt)
        # tim=parse(self.xtim)
        # timStr=tim.strftime('%Y%m%d')
        self.qxID = self.prjName + '_' + nss
        # print(s2,',',qx.trdCnt)
        # print('trdID',qx.trdID)

        return self.qxID


        # def xobj2str(xobj,xnamLst):

    def prQxUsr(self):
        ''' 輸出使用者變數保存的資料
            #qxLibName=['date','ID','stkVal','cash','dret','val']
        '''

        print('\n::qxUsr')
        dss = zwt.xobj2str(self.qxUsr, qxLibName)
        print(dss, '\n')

    def prQLib(self):
        ''' 輸出各種回溯交易測試資料，一般用於結束時
            #qxLibName=['date','ID','stkVal','cash','dret','val']
        '''

        print('')
        self.prQxUsr()
        print('::qxUsr.stk', self.prjName)
        print(self.qxUsrStk)
        print('::xtrdLib', self.fn_xtrdLib)
        # print(self.xtrdLib.tail())
        print(self.xtrdLib)
        print('')
        print('::qxLib.head', self.fn_qxLib)
        # print(self.qxUsr)
        print(self.qxLib.head())
        print('')
        print('::qxLib.tail')
        print(self.qxLib.tail())
        print('')

    def prTrdLib(self):
        ''' 輸出xtrdLib、xtrdNilLib 各種實盤、空頭交易資料，一般用於結束時
            
        '''
        print('\n::xtrdNilLib 空頭交易')
        print(self.xtrdNilLib)
        print('\n::xtrdLib 實盤交易', self.fn_xtrdLib)
        print(self.xtrdLib)


class zwDatX(object):
    ''' 設定各個資料目錄，用於zwDat專案
        Args:
            Csv資料來源。
            (datetime, open, close, high, low, volume)
    '''

    def __init__(self, rs0=_rdat0):
        # ----tick5.rss
        self.rdat = rs0  # \zwDat\
        self.rtickTim = rs0 + 'tick\\'  # \zwDat\ticktim\  2012-01\
        self.rtickTimMon = self.rtickTim + '2010-01\\'  # \zwDat\ticktim\  2012-01\
        # xxx.lib
        self.stkCodeLib = []
        # fn_xxx
        self.fn_stkCode = ''
        # --xtim.xxx
        self.xtimTick0 = "09:00"
        self.xtimTick9 = "15:00"
        #
        self.xtimSgn = ""
        self.xtim0Sgn = ""
        self.xtim9Sgn = ""
        self.xday0k = "2005-01-01"
        self.xday9k = ""
        self.xdayNum = 0
        self.xdayInx = 0
        self.DTxtim9 = None
        self.DTxtim0 = None
        self.DTxtim = None
        # self.xtim9=""
        # self.xtim0=""
        #  code.xxx
        self.code = ""
        self.codeSgn = ""
        self.codeCnt = 0
        self.codeNum = 0
        self.codeInx0k = -1
        #
        self.rmin0k = _rdatMin
        self.rminWrk = self.rmin0k + 'M05\\'

        # self.fn_min=[]
        self.min_ksgns = ['05', '15', '30', '60']  # 分時資料時間模式清單，一般是[5，15，30，60]，也可以自行設定
        self.min_ksgnWrk = 'M05'
        self.min_knum = 5
        # self.min_kdat=[5,15,30,60]
        ###
        self.datTick = []
        self.datMin = {}  # pd.DataFrame(columns=qxMinName)

        # self.xday0=''
        # self.xtickAppNDay=3      #tick裝換時，追加模式下，預設追加的日期檔數
        # self.xtickAppFlag=False  #預設=False，tick資料追加模式標誌,如果=True,強行將所有tick檔轉換為分時資料
        # self.xday0ChkFlag=True   #  預設=True，如果qx.xday0ChkFlag=Flase，強制從xday0k日開始抓取資料，主要用於用於補漏



        # ---------
        self.rTmp = _rTmp
        self.rdat = rs0

        self.rdatCN = _rdatCN
        self.rdatUS = _rdatUS
        self.rdatInx = _rdatInx

        self.rdatZW = _rdatZW
        self.rZWcnXDay = _rdatZW + "cnXDay\\"
        self.rZWcnDay = _rdatZW + "cnDay\\"
        self.rZWusDay = _rdatZW + "usDay\\"
        #
        self.rDay = rs0 + "day\\"
        self.rXDay = rs0 + "xday\\"

        # self.rDay9=rs0+"day9\\" #?????

        #  min.dat
        # self.rTick=_rdatMin+"tick\\"

        #

        #
        # self.datTick=pd.DataFrame(columns=qxTickNameNew,index=['date'])
        # self.datTick.dropna(inplace=True)

        # self.datM05.dropna(inplace=True)
        # self.datM15=pd.DataFrame(columns=qxMinName)
        # self.datM30=pd.DataFrame(columns=qxMinName)
        # self.datM60=pd.DataFrame(columns=qxMinName)
        #
        #

    def prDat(self):
        ''' 輸出相關資料目錄
        '''

        print('')
        print('rTmp,', self.rTmp)

        print('rdat,', self.rdat)
        print('rdatCN,', self.rdatCN)
        print('rdatUS,', self.rdatUS)
        print('rdatInx,', self.rdatInx)

        print('')
        print('rdatZW,', self.rdatZW)
        print('rZWcnXDay,', self.rZWcnXDay)
        print('rZWcnDay,', self.rZWcnDay)
        print('rZWusDay,', self.rZWusDay)

        print('')
        print('XDay,', self.rXDay)
        # print('Day9,',self.rDay9)
        print('Day,', self.rDay)

        # print('')
        # print('rdatMin,',self.rdatMin)

        print('')
        print('code,', self.code)
        print('name,', self.codeSgn)
