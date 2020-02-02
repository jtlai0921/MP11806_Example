# -*- coding: utf-8 -*- 
'''
  
  zwQuantToolBox 2016
  zw量化開源工具箱系列軟體 
  http://www.ziwang.com,Python量化第一品牌 
  
  檔案名稱:zwQTBox.py
  說明：import zwQTBox as zwx
  常用zwQuant量化工具函數集
  

'''

import sys, os
import numpy as np
import tushare as ts
import pandas as pd
#import pandas_datareader.data as web

from numba import *

import csv
import pickle
from datetime import *
from dateutil.parser import parse
from dateutil import rrule
import datetime as dt

import zwSys as zw  #::zwQT
import zwTools as zwt


# -------------

# -------------xtick tick分筆數據下載



def xtick_down_init(qx, finx):
    '''
    根據finx股票代碼檔案名，讀取資料到qx.stkCodeLib
    並根據預設的日期，初始化相關的時間參數
    [輸入]
        qx.xdayNum,下載時間週期為0，採用指定下載起始、結束日期模式
            qx.xday0k，資料下載起始日期，為空使用預設起始日期：2005-01-01
            qx.xday9k，資料下載結束日期，為空使用當前日期
            日期為字串格式，'yyyy-mm-dd'
        qx.xdayNum,下載時間週期大於0時，採用指定時間週期模式，一般用於資料追加
            #資料追加模式，無需設定起始、結束日期，
            例如，qx.xdayNum=2  #下載今天以前2天的資料，注意這個是日曆間隔，不是工作日間隔
    '''
    # ---finx
    qx.fn_stkCode = finx
    print(finx)
    qx.stkCodeLib = pd.read_csv(finx, encoding='gbk')
    qx.codeNum = len(qx.stkCodeLib['code'])
    # ---xtim0 qx.xday0k,qx.xday9k='2010-01-01','' qx.xday0k,qx.xday9k='',''
    if qx.xdayNum > 0:
        qx.DTxtim9 = dt.datetime.now()
        qx.DTxtim0 = qx.DTxtim9 - dt.timedelta(days=qx.xdayNum)
    else:
        if qx.xday9k == '':
            qx.DTxtim9 = dt.datetime.now()
        else:
            qx.DTxtim9 = parse(qx.xday9k)
        if qx.xday0k == '':
            qx.DTxtim0 = dt.datetime.now()
        else:
            qx.DTxtim0 = parse(qx.xday0k)
        #
        # qx.DTxtim9=zwt.iff2(qx.xday9k=='',dt.datetime.now(),parse(qx.xday9k))
        # qx.DTxtim0=zwt.iff2(qx.xday0k=='',qx.DTxtim9+dt.timedelta(days=-2) ,parse(qx.xday0k))
        #
        qx.xdayNum = rrule.rrule(rrule.DAILY, dtstart=qx.DTxtim0, until=qx.DTxtim9).count()
    #

    qx.xtim0Sgn, qx.xtim9Sgn = qx.DTxtim0.strftime('%Y-%m-%d'), qx.DTxtim9.strftime('%Y-%m-%d')
    print('\n@nday', qx.xdayNum, qx.xtim0Sgn, '@', qx.xtim9Sgn)  # nday=13


def xtick_down100(qx, ftg):
    '''
    根據指定的日期，股票代碼，資料檔案名：ftg
    下載指定股票指定日期的ticks資料，並保存到ftg
    [輸入]
        qx.code，股票代碼
        qx.xtimSgn，當前日期的字串
        ftg，保存tick資料的檔案名
    '''
    df, dn = [], 0
    try:
        df = ts.get_tick_data(qx.code, date=qx.xtimSgn)  # print(df.head())
    except IOError:
        pass  # skip,error
    datFlag, dn = False, len(df)
    print('     n', dn, ftg)  # 跳過無數據 日期
    # if zwt.xin(dn,0,9):print('n2',dn,ftg)
    if dn > 10:
        df['type'] = df['type'].str.replace(u'中性盤', 'norm')
        df['type'] = df['type'].str.replace(u'買盤', 'buy')
        df['type'] = df['type'].str.replace(u'賣盤', 'sell')
        df.to_csv(ftg, index=False, encoding='utf')
        datFlag = True
    #
    return datFlag, dn


def xtick_down8tim_codes(qx):
    '''
    下載指定日期，stkCodeLib包含的所有代碼的tick歷史分筆資料
    並轉換成對應的分時資料：5/15/30/60 分鐘
    資料檔案保存在：對應的資料目錄 \zwdat\tick\yyyy-mm\
        目錄下，yyyy，是年份；mm，是月份
    運行時，會根據日期，股票代碼，生成資料檔案名：ftg
    [輸入]
      qx.xtimSgn，當前日期的字串
      qx.stkCodeLib，包含所有股票代碼的pd資料表格
          '''
    # qx.xday0ChkFlag=False self.codeInx0k=-1
    # inx0,qx.codeNum=qx.codeInx,len(dinx['code'])
    numNil = 0
    for i, xc in enumerate(qx.stkCodeLib['code']):
        code = "%06d" % xc  # print("\n",i,"/",qx.codeNum,"code,",code)
        qx.code, qx.codeCnt = code, i
        # ---
        ftg = '%s%s_%s.csv' % (qx.rtickTimMon, code, qx.xtimSgn)
        xfg = os.path.exists(ftg)
        if xfg:
            numNil = 0
        else:
            if numNil < 90:
                datFlag, dfNum = xtick_down100(qx, ftg)
                numNil = zwt.iff2(datFlag, 0, numNil + 1)
                if dfNum == 3: numNil += 10
            #
            print(xfg, datFlag, qx.codeCnt, "/", qx.codeNum, ftg, numNil)
        #
        if numNil > 90: break
        # if i>3:break


def xtick_down8tim_all(qx, finx):
    '''
    下載所有股票代碼的所有tick歷史分筆資料，按時間日期迴圈下載
    資料檔案保存在：對應的資料目錄 \zwdat\tick\yyyy-mm\
        目錄下，yyyy，是年份；mm，是月份
    [輸入]
      finx，股票代碼檔
          '''

    xtick_down_init(qx, finx)
    # qx.xday0ChkFlag=False
    print('r', qx.rdat, qx.rtickTim)
    #    self.rtickTimMon=self.rtickTim+'2010-01\\'  #   \zwDat\ticktim\  2012-01\
    for tc in range(qx.xdayNum):
        qx.DTxtim = qx.DTxtim0 + dt.timedelta(days=tc)
        qx.xdayInx, qx.xtimSgn = tc, qx.DTxtim.strftime('%Y-%m-%d')
        #
        rmon0 = qx.DTxtim.strftime('%Y-%m')
        qx.rtickTimMon = '%s%s\\' % (qx.rtickTim, rmon0)
        xfg = os.path.exists(qx.rtickTimMon)
        if not xfg:
            os.mkdir(qx.rtickTimMon)
        #
        print('\n', xfg, qx.xdayInx, '/', qx.xdayNum, qx.xtimSgn)
        #
        xtick_down8tim_codes(qx)


# ----xtimck2tim.xxx 分筆tick資料，轉換為分時資料




def xtick2tim_code010(qx):
    '''
    根據指定的股票代碼，
    把所有tick歷史分筆資料
    轉換成對應的分時資料：5/15/30/60 分鐘
    資料檔案保存在：對應的資料目錄 \zwdat\min\
    [輸入]
      qx.code，股票代碼
      qx.min_ksgns,分時資料時間模式清單，一般是[5，15，30，60]，也可以自行設定
      self.xtickAppendFlag=False
    '''
    # xtick_setTimeDat(qx)

    for kss in qx.min_ksgns:
        rx.min_knum, rx.min_ksgnWrk = int(kss), 'M' + kss
        qx.datMin[kss] = pd.DataFrame(columns=zw.qxMinName)
        # 預設=False，tick資料追加模式標誌,如果=True,強行將所有tick檔轉換為分時資料
        if qx.xtickAppFlag:

            fss = zw._rdatTick + qx.code + '\\' + qx.xtim + '.csv'
            xfg = os.path.exists(fss)
            if xfg: qx.datMin[ksgn] = pd.read_csv(fss, index_col=False)
    #
    flst = os.listdir(zw._rdatTick + qx.code + '\\')
    qx.codeCnt, qx.codeNum = 0, len(flst)
    for fs0 in flst:
        qx.codeCnt += 1
        nday = qx.codeNum - qx.codeCnt
        if (not qx.xtickAppFlag) or (nday < qx.xtickAppNDay):
            qx.xtim = fs0.split('.')[0]
            xtick2tim100(qx)
            print(qx.codeCnt, "/", qx.codeNum, qx.xtim, nday, qx.xtickAppNDay, qx.xtickAppFlag, '@', qx.code)
            #

    # ---------wr.code分時數據
    xtick2minWr(qx, zw._rdatTick)


# ---------

def xtick2minWr(qx, rsk):
    '''
    把所有分時資料，保存到檔
    會自動去重
    對應的資料目錄 \zwdat\min\
        輸出資料在min目錄對應的分時目錄當中，已經自動轉換為5,15,30,60分鐘分時資料
    
    '''
    print(qx.min_ksgns)
    for ksgn0 in qx.min_ksgns:
        sgnMin = 'M' + ksgn0
        xdf = qx.datMin[sgnMin]
        xdf.drop_duplicates(subset='time', keep='last', inplace=True)
        xdf = np.round(xdf, 2)
        xdf = xdf.sort_values(by=['time'], ascending=False)
        # fss=zw._rdatMin+sgnMin+'\\'+qx.code+'.csv' # print(fss)
        fss = rsk + sgnMin + '\\' + qx.code + '.csv'
        print(fss)
        if len(xdf) > 3:
            xdf.to_csv(fss, columns=zw.qxMinName, index=False, encoding='utf')
        qx.datMin[sgnMin] = xdf


def xtick2minsub(df):
    '''
    tick 資料 轉換值程式，
    對根據qx.minType切割的資料，進行匯總，
    tick 資料 轉換為分時資料：5/15/30/60 分鐘
    輸入
        df，根據qx.minType切割的數據
    輸出
        ds，匯總後的資料，注意，格式是：pd.Series
    '''
    ds = pd.Series(index=zw.qxMinName)
    x9 = df.iloc[-1]
    ds['open'] = x9['price']
    x0 = df.iloc[0]
    ds['close'] = x0['price']
    #
    ds['high'], ds['low'] = np.max(df['price']), np.min(df['price'])
    ds['volume'], ds['amount'] = np.sum(df['volume']), np.sum(df['amount'])
    #
    xlst = ['norm', 'buy', 'sell']
    for xsgn in xlst:
        df2 = df[df['type'] == xsgn]
        if len(df2) > 0:
            ds['vol_' + xsgn], ds['amo_' + xsgn] = np.sum(df2['volume']), np.sum(df2['amount'])
        else:
            ds['vol_' + xsgn], ds['amo_' + xsgn] = 0, 0
    #
    return ds


def xtick2min010(qx):
    '''
       將下載的tick分筆資料，轉換為分時資料：5/15/30/60 分鐘
       並且追加到對應的分時資料清單當中
       注意qx.xtimTick0,qx.xtimTick9是預設時間資料，在zwDatX類定義並初始化
       輸入
           qx.min_ksgnWrk
           qx.min_knum
           
    '''

    wrkDTim0, dt9 = parse(qx.xtimTick0), parse(qx.xtimTick9)
    xt = dt9 - wrkDTim0
    numMin = xt.total_seconds() / 60
    xn9 = int(numMin / qx.min_knum) + 1  # print(wrkDTim0,xn9) #xn9=7
    for tc in range(xn9):
        wrkDTim9 = wrkDTim0 + dt.timedelta(minutes=qx.min_knum)
        strTim0, strTim9 = wrkDTim0.strftime('%H:%M:%S'), wrkDTim9.strftime('%H:%M:%S')
        # ---cut tick.dat by tim
        df = qx.datTick  # print(df.head())
        df2 = df[df['time'] < strTim9]
        df3 = df2[df2['time'] >= strTim0]
        if len(df3) > 0:
            # -----tick 資料 轉換為分時資料：5/15/30/60 分鐘
            ds = xtick2minsub(df3)
            ds['time'] = qx.xtimSgn + ' ' + strTim0
            qx.datMin[qx.min_ksgnWrk] = qx.datMin[qx.min_ksgnWrk].append(ds.T, ignore_index=True)
        # ----ok,#tc
        wrkDTim0 = wrkDTim9


def xtick2tim100(qx, fdat):
    '''
    根據輸入的fdat檔案名，讀取tick分筆資料，並轉換為對應的分時資料：5/15/30/60 分鐘
    【輸入】
    fdat，rick資料檔案名
    
    '''
    xfg = os.path.exists(fdat)  # print('x100',xfg,fdat)
    if xfg:
        qx.datTick = pd.read_csv(fdat, index_col=False)
        if len(qx.datTick) > 10:
            for kss in qx.min_ksgns:  # qx.min_ksgns=['M05','M15','M30','M60']
                qx.min_knum, qx.min_ksgnWrk, ksgn = int(kss), 'M' + kss, 'M' + kss
                xtick2min010(qx)


def xtick2tim_nday(qx):
    '''
    將指定時間週期的tick資料，轉換為分時資料
          '''
    for tc in range(qx.xdayNum):
        qx.DTxtim = qx.DTxtim0 + dt.timedelta(days=tc)
        qx.xdayInx, qx.xtimSgn = tc, qx.DTxtim.strftime('%Y-%m-%d')
        #
        rmon0 = qx.DTxtim.strftime('%Y-%m')
        qx.rtickTimMon = '%s%s\\' % (qx.rtickTim, rmon0)
        fdat = '%s%s_%s.csv' % (qx.rtickTimMon, qx.code, qx.xtimSgn)
        #
        print(qx.xdayInx, '/', qx.xdayNum, qx.xtimSgn, fdat)
        xtick2tim100(qx, fdat)


def xtick2tim_code100(qx):
    '''
    根據qx.min_ksgns預設的分時參數，
    以及指定的股票代碼、時間週期參數，
    將對應的tick資料，轉換為分時資料，並保存到檔
    【輸入】
        qx.code，股票代碼
        qx.min_ksgns,分時資料時間模式清單，一般是[5，15，30，60]，也可以自行設定
    【輸出】
       分時資料保存在目錄：
           \zwdat\min\Mxx\
    '''
    for kss in qx.min_ksgns:
        qx.min_knum, qx.min_ksgnWrk, ksgn = int(kss), 'M' + kss, 'M' + kss
        qx.rminWrk = '%s\\%s\\' % (qx.rmin0k, qx.min_ksgnWrk)
        if not os.path.exists(qx.rminWrk): os.mkdir(qx.rminWrk)
        #
        qx.datMin[ksgn] = pd.DataFrame(columns=zw.qxMinName)
        fss = '%s%s.csv' % (qx.rminWrk, qx.code)  # print('@fss',fss,len(qx.datMin[ksgn]))
        xfg = os.path.exists(fss)  # print(xfg,'@f100',fss,len(qx.datMin[ksgn]))
        if xfg:
            qx.datMin[ksgn] = pd.read_csv(fss, index_col=False)
            print('\n@fss', fss, len(qx.datMin[ksgn]))
    #
    xtick2tim_nday(qx)
    xtick2minWr(qx, qx.rmin0k)


def xtick2tim_allcode(qx):
    '''
    將所有股票代碼的tick資料轉換為分時資料
    輸入：
        qx.stkCodeLib:，股票代碼列表檔，
        qx.min_ksgns,分時資料時間模式清單，一般是[5，15，30，60]，也可以自行設定
    輸出
        \zwdat\min\
        輸出資料在tick目錄對應的分時目錄當中，已經自動轉換為5,15,30,60分鐘分時資料
        為當天最新即時分筆資料，會自動覆蓋以前的就資料
    '''
    for i, xc in enumerate(qx.stkCodeLib['code']):
        code = "%06d" % xc  # print("\n",i,"/",qx.codeNum,"code,",code)
        qx.code, qx.codeCnt = code, i
        print(qx.codeCnt, "/", qx.codeNum, qx.rtickTimMon, code, qx.xtimSgn)
        #
        xtick2tim_code100(qx)


# ---------------xtick.real.xxx

def xtick_real_downsub(xcod):
    ''' 中國A股,tick 歷史或real即時 tick 分筆資料下載副程式
        會自動將中文type，替換成 英文：中性盤：norm；買盤：buy 賣盤：sell
        
    【輸入】
        xcod,股票代碼
        xtim，日期字串，當xtim為空時，下載的是當天 即時 tick資料
    【輸出】
        df,股票 tick  資料
            資料列格式：
            time,price,change,volume,amount,type
    '''
    xd = ts.get_today_ticks(xcod)
    dn = len(xd)  # print('n',dn) # 跳過無數據 日期
    if dn > 10:
        xd['type'] = xd['type'].str.replace(u'中性盤', 'norm')
        xd['type'] = xd['type'].str.replace(u'買盤', 'buy')
        xd['type'] = xd['type'].str.replace(u'賣盤', 'sell')
        # xd.to_csv('tmp\\'+xcod+'_'+xtim+'.csv',index=False,encoding='utf')
    else:
        xd = []
    #
    return xd


def xtick_real_down_all(qx, finx):
    '''
    下載當天的即時tick分筆資料，並自動轉換為分時資料
    輸入：
        finx，股票目錄索引檔，一般每個股票，下載需要2-3分鐘，
            如果做高頻。單機股票代碼不要太多，可以分組在多台電腦運行
        qx.min_ksgns，股票分時參數，例如：['20','60']
    輸出
        \zwdat\tickreal\ 輸出目錄
        \zwdat\tickreal\tick\ 分筆tick數據
        \zwdat\tickreal\Mxx\ 分筆tick資料，轉換後的分時資料
        
        輸出資料在對應的tick目錄當中，已經自動轉換為分時資料
        當天最新即時tikc、分筆資料，會自動覆蓋以前的舊資料
        
        
    '''
    # qx.min_ksgns=['05','15','30','60']
    rdat = zw._rdatTickReal
    dinx = pd.read_csv(finx, encoding='gbk')
    print('finx', finx)
    i, xn9 = 0, len(dinx['code'])
    for xc in dinx['code']:
        i += 1
        code = "%06d" % xc
        qx.codeCnt, qx.code = i, code
        print("\n", i, "/", xn9, "code,", code)
        # ---
        df = xtick_real_downsub(code)
        if len(df) > 10:
            fss = rdat + 'tick\\' + qx.code + '.csv'
            print('\n', fss)
            df.to_csv(fss, index=False, encoding='utf')
            qx.datTick = df
            # ---------- tick 分筆資料，轉換為分時資料：05,15,30,60
            for kss in qx.min_ksgns:  # qx.min_ksgns=['M05','M15','M30','M60']
                qx.min_knum, qx.min_ksgnWrk, ksgn = int(kss), 'M' + kss, 'M' + kss
                qx.rminWrk = '%s\\%s\\' % (qx.rmin0k, qx.min_ksgnWrk)
                if not os.path.exists(qx.rminWrk): os.mkdir(qx.rminWrk)
                #
                # sgnMin='M'+ksgn0 # qx.minType=int(ksgn0)       # print('@mt',qx.minType)
                qx.datMin[ksgn] = pd.DataFrame(columns=zw.qxMinName)
                xtick2min010(qx)
                #
            xtick2minWr(qx, rdat)


# ----------------down.stk

def down_stk_cn020inx(qx, xtim0):
    ''' 下載大盤指數資料,簡版股票資料，可下載到1994年股市開市起
    【輸入】
        qx.xcod:指數代碼

    '''
    xcod = qx.code
    tim0 = xtim0  # tim0='1994-01-01'
    xd = []
    rss = qx.rXDay
    fss = rss + xcod + '.csv'
    # if ((xtyp!='D')and(xtyp!='9') ):    tim0=tim0+" 00:00:00"

    # -------------------
    xfg = os.path.exists(fss)
    xd0 = []
    if xfg:
        xd0 = pd.read_csv(fss, index_col=0, parse_dates=[0], encoding='gbk')
        # print(xd0.head())
        xd0 = xd0.sort_index(ascending=False)
        # tim0=xd0.index[0]
        _xt = xd0.index[0]  # xt=xd0.index[-1]###
        s2 = str(_xt)
        tim0 = s2.split(" ")[0]

    #
    print('\n', xfg, fss, ",", tim0)
    # -----------
    try:
        xd = ts.get_h_data(xcod, start=tim0, index=True, end=None, retry_count=5, pause=1)  # Day9
        # -------------
        if xd is not None:
            if (len(xd0) > 0):
                xd2 = xd0.append(xd)
                #  flt.dup 
                xd2["index"] = xd2.index
                xd2.drop_duplicates(subset='index', keep='last', inplace=True)
                del (xd2["index"])
                # xd2.index=pd.to_datetime(xd2.index)
                xd = xd2

            xd = xd.sort_index(ascending=False)
            xd = np.round(xd, 3)
            xd.to_csv(fss, encoding='gbk')
    except IOError:
        pass  # skip,error

    return xd


def down_stk_cn010(qx):
    ''' 中國A股資料下載副程式
    【輸入】
        qx (zwDatX): 
        xtyp (str)：資料類型，9,Day9,簡版股票資料，可下載到2001年，其他的全部是擴充版資料，只可下載近3年數據
            D=日k線 W=周 M=月 預設為D
    :ivar xcod (int): 股票代碼
    :ivar fss (str): 保存資料檔案名
    '''

    xcod, rss, = qx.code, qx.rDay
    tim0 = '1994-01-01'  # tim0='2012-01-01'
    #
    fss = rss + xcod + '.csv'
    # -------------------
    xfg = os.path.exists(fss)
    xd0 = []
    xd = []
    if xfg:
        xd0 = pd.read_csv(fss, index_col=0, parse_dates=[0], encoding='gbk')
        # print(xd0.head())
        xd0 = xd0.sort_index(ascending=False)
        # tim0=xd0.index[0]
        _xt = xd0.index[0]  # xt=xd0.index[-1]###
        s2 = str(_xt)
        tim0 = s2.split(" ")[0]

    print('\n', xfg, fss, ",", tim0)
    # -----------
    try:
        xd = ts.get_h_data(xcod, start=tim0, end=None, retry_count=5, pause=1)  # Day9
        # xd=ts.get_hist_data(xcod,start=tim0,end=None,retry_count=5,pause=1,ktype=xtyp)
        # -------------
        if xd is not None:
            if (len(xd0) > 0):
                xd2 = xd0.append(xd)
                #  flt.dup 
                xd2["index"] = xd2.index
                xd2.drop_duplicates(subset='index', keep='last', inplace=True)
                del (xd2["index"])
                # xd2.index=pd.to_datetime(xd2.index)
                xd = xd2

            xd = xd.sort_index(ascending=False)
            xd = np.round(xd, 3)
            xd.to_csv(fss, encoding='gbk')
    except IOError:
        pass  # skip,error

    return xd


def down_stk_all(qx, finx):
    '''
    根據finx股票清單檔，下載所有，或追加日線資料
    自動去重，排序
    
    '''
    dinx = pd.read_csv(finx, encoding='gbk')
    print(finx)
    xn9 = len(dinx['code'])
    for i, xc in enumerate(dinx['code']):
        code = "%06d" % xc
        print("\n", i, "/", xn9, "code,", code)
        # ---
        qx.code = code
        down_stk_cn010(qx)


def down_stk_inx(qx, finx):
    dinx = pd.read_csv(finx, encoding='gbk')
    print(finx)

    xn9 = len(dinx['code'])
    for i in range(xn9):
        # for xc,xtim0 in dinx['code'],dinx['tim0']:
        d5 = dinx.iloc[i]
        xc = d5['code']
        xtim0 = d5['tim0']
        i += 1
        code = "%06d" % xc
        print("\n", i, "/", xn9, "code,", code, xtim0)
        # ---
        qx.code = code
        down_stk_cn020inx(qx, xtim0)

'''

def down_stk_yahoo010(qx, ftg):
   
		美股資料下載副程式
		Args:
        qx (zwDatX): 
        ftg,資料檔案名
        
    :ivar xcod (int): 股票代碼
    :ivar xdat (pd.DataFrame): yahoo xcod股票資料
   
    try:
        xcod = qx.code
        xdat = web.DataReader(xcod, "yahoo", start="1/1/1900")
        xdat.to_csv(ftg)
        print(ftg)
    except IOError:
        pass  # skip,error

'''

# --------stk.InxLib.xxx

def stkInxLibRd(qx):
    '''
		讀取指定的大盤數據到zw.stkInxLib
		
		Args:
            
    :
    qx.stkInxRDat='\\zwdat\\cn\\xday\\''    #大盤指數資料來源路徑
    qx.stkInxCode='000001'    #大盤指數代碼
    qx.stkInxName='sz001'    #大盤指數名稱，拼音
    qx.stkInxCName='上證指數'    #大盤指數中文名稱，拼音
    #
    zw.stkInxLib=None  #全域變數，大盤指數，記憶體股票資料庫
    
    '''
    if qx.stkInxCode != '':
        fss = qx.stkInxRDat + qx.stkInxCode + ".csv"
        xfg = os.path.exists(fss)
        if xfg:
            df10 = pd.read_csv(fss, index_col=0, parse_dates=[0])
            df10 = df2zwAdj(df10)
            zw.stkInxLib = df10.sort_index()


def stkInxLibSet8XTim(qx, dtim0, dtim9):
    ''' 根據時間段，切割大盤指數資料 zw.stkInxLib
    
    Args:
        dtim0（str）：起始時間
        dtim9（str）:結束時間
            
    :ivar
    zw.stkInxLib，大盤指數資料
    '''
    df10 = zw.stkInxLib
    # print(df10.head())
    if dtim0 == '':
        df20 = df10
    else:
        df20 = df10[(df10.index >= dtim0) & (df10.index <= dtim9)]
        # df20=df10[(df10['date']>=dtim0)&(df10['date']<=dtim9)]

    zw.stkInxLib = df20.sort_index()


# --------stk.Lib.xxx



def stkLibRd(xlst, rdir):
    '''
		讀取指定的股票資料到stkLib，可多檔股票，以及股票代碼檔案名
		
		Args:
        xlst (list): 指定股票代碼列表,
          如果xlst參數首字母是'@'，表示是股票代碼檔案名，而不是代碼本身
          用於批量導入股票代碼 
        rdir (str)：資料類存放目錄 
            
    :ivar xcod (int): 股票代碼
    
    '''
    zw.stkLib = {}  # 全域變數，相關股票的交易資料
    zw.stkLibCode = []  # 全域變數，相關股票的交易代碼

    #
    x0 = xlst[0]
    if x0.find('@') == 0:
        fss = x0[1:]  # print('fss',fss)  #fss=_rdatInx+fs0
        flst = pd.read_csv(fss, dtype=str, encoding='gbk')
        xlst = list(flst['code'])
        # print(xlst)
    for xcod in xlst:
        fss = rdir + xcod + ".csv"
        xfg = os.path.exists(fss)
        if xfg:
            try:
                df10 = pd.read_csv(fss, index_col=0, parse_dates=[0])
                df10 = df2zwAdj(df10)
            except:
                print('讀取檔失敗：', fss)
            zw.stkLib[xcod] = df10.sort_index()
            zw.stkLibCode.append(xcod)


def stkLibPr():
    ''' 輸出股票資料 
            
    :ivar xcod (int): 股票代碼
    '''

    for xcod in zw.stkLibCode:
        df10 = zw.stkLib[xcod]
        print('\n::code,', xcod)
        print(df10.head())
    print('\n stk code num', len(zw.stkLibCode))


def stkLibSet8XTim(dtim0, dtim9):
    ''' 根據時間段，切割股票資料
    
    Args:
        dtim0（str）：起始時間
        dtim9（str）:結束時間
            
    :ivar xcod (int): 股票代碼
    '''
    for xcod in zw.stkLibCode:
        df10 = zw.stkLib[xcod]
        if dtim0 == '':
            df20 = df10
        else:
            df20 = df10[(df10.index >= dtim0) & (df10.index <= dtim9)]
        #
        # zw.stkLibCode.append(xcod)
        zw.stkLib[xcod] = df20.sort_index()
        # print(zw.stkLib[xcod])
        # print(df20)


def stkLibSetDVix():
    ''' 根據時間段，切割股票資料
    
    Args:
        dtim0（str）：起始時間
        dtim9（str）:結束時間
            
    :ivar xcod (int): 股票代碼
    '''
    for xcod in zw.stkLibCode:
        df10 = zw.stkLib[xcod]
        df10['dvix'] = df10['dprice'] / df10['dprice'].shift(1) * 100
        #
        zw.stkLib[xcod] = np.round(df10, 2)


# --------stk.Lib.get.xxx
def stkGetVars(qx, ksgn):
    '''
      獲取股票代碼，指定欄位的資料
    
    Args:
        qx (zwQuantX): zwQuantX交易資料包
        ksgn (str): qx.stkCode,qx.xtim,qx.stkSgnPrice 
        '''
    d10 = zw.stkLib[qx.stkCode]
    d01 = d10[qx.xtim:qx.xtim]
    #
    dval = 0
    if len(d01) > 0:
        d02 = d01[ksgn]
        dval = d02[0]

    return dval


def stkGetPrice(qx, ksgn):
    '''
      獲取當前價格
    
    Args:
        qx (zwQuantX): zwQuantX交易資料包
        ksgn (str): 價格模式代碼
        '''
    d10 = zw.stkLib[qx.stkCode]
    d01 = d10[qx.xtim:qx.xtim]
    #
    price = 0
    if len(d01) > 0:
        d02 = d01[ksgn]
        price = d02[0]
        if pd.isnull(price):
            d02 = d01['dprice']
            price = d02[0]

    return price


def stkGetPrice9x(qx, ksgn):
    '''
      獲取首個、末個交易日資料
    
    Args:
        qx (zwQuantX): zwQuantX交易資料包
        ksgn (str): 價格模式代碼
        '''
    d10 = zw.stkLib[qx.stkCode]
    # d05=d10[qx.stkSgnPrice]
    d05 = d10[ksgn]
    price0 = d05[0]
    price9 = d05[-1]

    return price0, price9


def stkLibGetTimX(xcod):
    '''
    返回指定股票代碼首個、末個交易日時間資料
    
    Args:
        xcod (int): 股票代碼
        '''
    d10 = zw.stkLib[xcod]
    d01 = d10.index
    xtim0 = d01[0]
    xtim9 = d01[-1]
    # xtim0s=xtim0.strftime()

    return xtim0, xtim9


def stkLibName8Code(xcod):
    ''' 根據股票代碼，返回股票中文、英文/拼音縮寫名稱
    
    Args:
        xcod (int): 股票代碼
        '''
    d10 = zw.stkCodeTbl[zw.stkCodeTbl['code'] == xcod]
    # print(d10)
    enam = ''
    cnam = ''
    if len(d10) > 0:
        xc = d10.index[0]
        enam = d10.at[xc, 'ename']
        cnam = d10.at[xc, 'cname']
        # print('c',xc,cnam,enam)

    return enam, cnam


# --------stk.xxx
def stkValCalc(qx, xdicts):
    ''' 計算 xdicts 內所有的股票總價值
    
    Args:
        qx (zwQuantX): zwQuantX數據包
        xdicts (list)：所選股票代碼列表 
            
    :ivar xcod (int): 股票代碼
    '''
    dsum9 = 0
    for xcod, xnum in xdicts.items():
        qx.stkCode = xcod
        # price=stkGetPrice(qx,'dprice')
        price = stkGetPrice(qx, qx.priceCalc)
        dsum = price * xnum
        dsum9 = dsum9 + dsum
        # print('@c',qx.xtim,price,dsum,dsum9)

    return dsum9


# --------xbars.xxx
def xbarPr(bars):
    ''' 輸出資料包資料
    '''
    for xd in bars:
        xd.prXBar()
        print('')


def xbarGet8Tim(xcod, xtim):
    ''' 根據指定股票代碼。時間，獲取資料包
    
    Args:
        xcod (int): 股票代碼
        xtim (str): 交易時間
        '''

    d10 = zw.stkLib[xcod]
    d02 = d10[xtim:xtim]

    return d02


def xbarGet8TimExt(xcod, xtim):
    '''  根據指定股票代碼。時間，獲取資料包及股票資料
    
    Args:
        xcod (int): 股票代碼
        xtim (str): 交易時間
        '''

    d10 = zw.stkLib[xcod]
    d02 = d10[xtim:xtim]

    return d02, d10


# --------xtrd.xxx

def xtrdObjSet(qx):
    ''' 設定交易節點資料
    
    Args:
        qx (zwDatX): zwQuant數據包   
    #xtrdName=['date','ID','mode','code','dprice','num','kprice','sum','cash']
        '''
    b2 = pd.Series(zw.xtrdNil, index=zw.xtrdName)
    b2['date'] = qx.xtim
    b2['code'] = qx.stkCode
    b2['num'] = qx.stkNum
    if qx.stkNum != 0:
        b2['mode'] = zwt.iff3(qx.stkNum, 0, 'sell', '', 'buy')
        b2['dprice'] = stkGetVars(qx, qx.priceWrk)
        # kprice=stkGetVars(qx,qx.priceBuy)
        kprice = stkGetPrice(qx, qx.priceBuy)
        b2['kprice'] = kprice
        b2['sum'] = kprice * qx.stkNum
        dcash9 = qx.qxUsr['cash']
        b2['cash'] = dcash9 - kprice * b2['num']

    # print('\nb2\n',b2)
    return b2


def xtrdChkFlag(qx):
    ''' 檢查是不是有效交易
    
    Args:
        qx (zwQuantX): zwQuantX數據包
        #qx.stkNum，>0，買入股票；<0，賣出股票；-1；賣出全部股票
        #預設參數：qx.qxUsr 
    
    Return：
        xfg,True,有效交易；False，無效交易
        b2：有效交易的資料包 Bar
        
    :ivar xnum (int): 用戶持有資產總數
    '''

    kfg = False
    b2 = None
    qx.trdNilFlag = False
    dcash9 = qx.qxUsr['cash']
    dnum = qx.stkNum
    dnum5 = abs(dnum)
    numFg = zwt.xinEQ(dnum5, qx.stkNum0, qx.stkNum9)
    # --------
    # b2=xtrdObjSet(qx) #print('::b2\n',b2)
    if dnum > 0:
        # dsum=b2['sum']
        kprice = stkGetVars(qx, qx.priceBuy)
        dsum = kprice * dnum
        # 股票買入股票總數，必須在限額內：100-2w手，總值不能超過現金數，買空需修改此處
        if numFg:
            if dsum < dcash9:
                kfg = True
            else:
                qx.trdNilFlag = True
    else:
        if qx.stkCode in qx.qxUsrStk:
            # print('@',qx.stkCode,dnum)
            xnum = qx.qxUsrStk[qx.stkCode]
            if dnum == -1:
                qx.stkNum = -xnum
                kfg = True
            else:
                kfg = zwt.iff2(dnum5 <= xnum, True, False)
            #
            qx.trdNilFlag = not kfg
        elif dnum != -1:
            qx.trdNilFlag = True

            #
    if kfg or qx.trdNilFlag:
        b2 = xtrdObjSet(qx)  # 設定交易節點
    else:
        qx.stkNum = 0

    return kfg, b2


def xtrdChkFlag00(qx):
    ''' 檢查是不是有效交易
    
    Args:
        qx (zwQuantX): zwQuantX數據包
        #qx.stkNum，>0，買入股票；<0，賣出股票；-1；賣出全部股票
        #預設參數：qx.qxUsr 
    
    Return：
        xfg,True,有效交易；False，無效交易
        b2：有效交易的資料包 Bar
        
    :ivar xnum (int): 用戶持有資產總數
    '''

    kfg = False
    b2 = None
    dcash9 = qx.qxUsr['cash']
    # --------
    # b2=xtrdObjSet(qx) #print('::b2\n',b2)
    if qx.stkNum > 0:
        # dsum=b2['sum']
        kprice = stkGetVars(qx, qx.priceBuy)
        dsum = kprice * qx.stkNum
        # 股票買入股票總數，必須在限額內：100-2w手，總值不能超過現金數，買空需修改此處
        kfg = (zwt.xinEQ(qx.stkNum, qx.stkNum0, qx.stkNum9) and (dsum < dcash9))
    else:
        if qx.stkCode in qx.qxUsrStk:
            xnum = qx.qxUsrStk[qx.stkCode]
            if (qx.stkNum == -1) or (abs(qx.stkNum) >= xnum):
                qx.stkNum = -xnum
                kfg = True
            elif abs(qx.stkNum) < xnum:
                kfg = True

    #
    if kfg:
        b2 = xtrdObjSet(qx)  # 設定交易節點
    else:
        qx.stkNum = 0

    return kfg, b2


def xusrStkNum(qx, xcod):
    ''' 返回使用者持有的 xcod 股票數目
    
    Args:
        qx (zwQuantX): zwQuantX數據包
        xcod (int): 股票代碼
        '''

    dnum = 0
    if xcod in qx.qxUsrStk:
        dnum = qx.qxUsrStk[xcod]
    return dnum


def xusrUpdate(qx):
    ''' 更新使用者資料
    
    Args:
        qx (zwQuantX): zwQuantX數據包 
        
        '''

    qx.qxUsr['date'] = qx.xtim
    # dcash=qx.qxUsr['cash']
    # qx.qxUsr['cash']=dcash-b2['sum']
    stkVal = stkValCalc(qx, qx.qxUsrStk)
    qx.qxUsr['stkVal'] = stkVal
    dval0 = qx.qxUsr['val']
    dval = qx.qxUsr['cash'] + stkVal
    qx.qxUsr['val'] = dval
    # qx.qxUsr['dret'] = (qx.qxUsr['val'] - dval0) / dval0
    # # print('\n::xbarUsr\n',qx.qxUsrStk)
    # # print('stkVal',stkVal)
    #
    # # ---------drawdown.xxx
    # if dval > qx.downHigh:
    #     qx.downHigh = dval
    #     qx.downLow = dval
    #     # qx.downHighTime=date.today()
    #     qx.downHighTime = qx.xtim
    #     # qx.downHighTime=datetime.dateTime
    # else:
    #     qx.downLow = min(dval, qx.downLow)
    # # ----------
    # qx.qxUsr['downHigh'] = qx.downHigh
    # qx.qxUsr['downLow'] = qx.downLow
    # kmax = downKMax(qx.downLow, qx.downHigh)
    # qx.downKMax = min(qx.downKMax, kmax)
    # qx.qxUsr['downKMax'] = qx.downKMax
    # # xday=parse(qx.xtim)-parse(qx.downHighTime)
    # nday = rrule.rrule(rrule.DAILY, dtstart=parse(qx.downHighTime), until=parse(qx.xtim)).count()
    #
    # dmax = max(qx.downMaxDay, nday - 1)
    # qx.downMaxDay = dmax
    # qx.qxUsr['downDay'] = qx.downMaxDay


def xusr4xtrd(qx, b2):
    ''' 根據交易資料，更新使用者資料 qxUsr
    
    Args:
        qx (zwQuantX): zwQuantX數據包
        b2 (pd.Series): 有效交易的資料包 Bar
            
    :ivar xcod (int): 股票代碼
    '''

    xcod = b2['code']
    if xcod != '':
        xfg = xcod in qx.qxUsrStk
        # s2=zwBox.xobj2str(b2,zw.xbarName) #print(xfg,'::b2,',s2)

        if xfg:
            xnum = qx.qxUsrStk[xcod]
            xnum2 = xnum + b2['num']
            qx.qxUsrStk[xcod] = xnum2
            if xnum2 == 0: del (qx.qxUsrStk[xcod])
        else:
            qx.qxUsrStk[xcod] = b2['num']

        qx.qxUsr['cash'] = qx.qxUsr['cash'] - b2['sum']


def xtrdLibAdd(qx):
    ''' 添加交易到 xtrdLib
    
    Args:
        qx (zwQuantX): zwQuantX數據包

    '''

    qx.qxIDSet()
    # print('qx.qxID',qx.qxID)
    qx.xtrdChk['ID'] = qx.qxID
    # xbarUsrUpdate(qx,qx.xtrdChk)
    xusr4xtrd(qx, qx.xtrdChk)  # qx.qxUsr['cash']=qx.qxUsr['cash']-b2['sum']
    qx.xtrdLib = qx.xtrdLib.append(qx.xtrdChk.T, ignore_index=True)


def xtrdLibNilAdd(qx):
    ''' 添加交易到空頭記錄 xtrdNilLib
    
    Args:
        qx (zwQuantX): zwQuantX數據包

    '''
    qx.xtrdChk['ID'] = 'nil'
    qx.xtrdNilLib = qx.xtrdNilLib.append(qx.xtrdChk.T, ignore_index=True)


# --zw.ret.xxx

def zwRetTradeCalc(qx, pyqt_mode=False):
    ''' 輸出、計算交易資料
    
    Args:
        qx (zwQuantX): zwQuantX數據包
        
        '''

    df = qx.xtrdLib
    xbar = qx.qxLib.iloc[-1]
    xtim9 = xbar['date']

    sum9 = -1 * df['sum'].sum()
    print('交易總次數：%d' % len(df))
    print('交易總盈利：%.2f' % sum9)
    qx.result_info.append(['交易總次數', '%d' % len(df)])
    # len(df)
    qx.result_info.append(['交易總盈利' , '%.2f' % sum9])

    # print('交易總支出：%.2f' %sumPut)
    # print('交易總收入：%.2f' %sumGet)
    # print('交易收益差：%.2f' %sumx)
    print('')
    # print('盈利交易數：%d' % numAdd)
    # print('盈利交易金額：%.2f' % sumAdd)
    # print('虧損交易數：%d' % numDec)
    # print('虧損交易金額：%.2f' % sumDec)
    # print('@t',qx.xtim)
    qx.xtim = xtim9


def zwRetPr(qx):
    ''' 輸出、計算回報率
    
    Args:
        qx (zwQuantX): zwQuantX數據包

    '''
    # ---回報測試

    retAvg = qx.qxLib['dret'].mean()
    retStd = qx.qxLib['dret'].std()
    dsharp = sharpe_rate(qx.qxLib['dret'], qx.rfRate)
    dsharp0 = sharpe_rate(qx.qxLib['dret'], 0)
    dcash = qx.qxUsr['cash']
    dstk = stkValCalc(qx, qx.qxUsrStk)  # 因為個人添加了到期清倉的機制，所以dstk應該為0
    dval = dstk + dcash
    dret9 = (dval - qx.mbase) / qx.mbase

    print('')
    print("最終資產價值 Final portfolio value: $%.2f" % dval)
    print("最終現金資產價值 Final cash portfolio value: $%.2f" % dcash)
    print("最終證券資產價值 Final stock portfolio value: $%.2f" % dstk)
    print("累計回報率 Cumulative returns: %.2f %%" % (dret9 * 100))
    print("平均日收益率 Average daily return: %.3f %%" % (retAvg * 100))
    print("日收益率方差 Std. dev. daily return:%.4f " % (retStd))
    print('')
    print("夏普比率 Sharpe ratio: %.3f,（%.2f利率）" % (dsharp, qx.rfRate))
    print("無風險利率 Risk Free Rate: %.2f" % (qx.rfRate))
    print("夏普比率 Sharpe ratio: %.3f,（0利率）" % (dsharp0))
    print('')
    print("最大回撤率 Max. drawdown: %.4f %%" % (abs(qx.downKMax)))
    print("最長回撤時間 Longest drawdown duration:% d" % qx.downMaxDay)
    print("回撤時間(最高點位) Time High. drawdown: ", qx.downHighTime)
    print("回撤最高點位 High. drawdown: %.3f" % qx.downHigh)
    print("回撤最低點位 Low. drawdown: %.3f" % qx.downLow)
    print('')
    print("時間週期 Date lenght: %d (Day)" % qx.periodNDay)
    print("時間週期（交易日） Date lenght(weekday): %d (Day)" % qx.wrkNDay)

    print("開始時間 Date begin: %s" % qx.xtim0)
    print("結束時間 Date lenght: %s" % qx.xtim9)
    print('')
    print("項目名稱 Project name: %s" % qx.prjName)
    print("策略名稱 Strategy name: %s" % qx.staName)
    print("股票代碼列表 Stock list: ", zw.stkLibCode)
    print("策略參數變數 staVars[]: ", qx.staVars)
    print('')

    if qx.pyqt_mode_flag == True:
        qx.result_info.append(['最終資產價值' , '$%.2f' % dval])
        qx.result_info.append(['最終現金資產價值' , '$%.2f' % dcash])
        qx.result_info.append(['最終證券資產價值' , '$%.2f' % dstk])
        qx.result_info.append(['累計回報率' , '%.2f' % (dret9 * 100)])
        qx.result_info.append(['平均日收益率' , '%.3f' % (retAvg * 100)])
        qx.result_info.append(['日收益率方差' , '%.4f' % retStd])
        qx.result_info.append(['夏普比率' , '%.3f,（%.2f利率）' % (dsharp, qx.rfRate)])
        qx.result_info.append(['無風險利率' , '%.2f' % qx.rfRate])
        qx.result_info.append(['夏普比率（無風險）' , '%.3f' % dsharp0])
        qx.result_info.append(['最大回撤率' , '%.4f' % abs(qx.downKMax)])
        qx.result_info.append(['最長回撤時間' , '%d' % qx.downMaxDay])
        qx.result_info.append(['回撤時間(最高點位)' , qx.downHighTime])
        qx.result_info.append(['回撤最高點位' , '%.3f' % qx.downHigh])
        qx.result_info.append(['回撤最低點位' , '%.3f' % qx.downLow])
        qx.result_info.append(['時間週期' , '%d (Day)' % qx.periodNDay])
        qx.result_info.append(['時間週期（交易日）' , '%d (Day)' % qx.wrkNDay])
        qx.result_info.append(['開始時間' , qx.xtim0])
        qx.result_info.append(['結束時間' , qx.xtim9])
        qx.result_info.append(['項目名稱' , '%s' % qx.prjName])
        qx.result_info.append(['策略名稱' , '%s' % qx.staName])
        # qx.result_info.append(['股票代碼列表' , '  '.join(zw.stkLibCode)])
        qx.result_info.append(['策略參數變數 staVars[]' , '  '.join([str(i) for i in qx.staVars])])
        # qx.result_info.append(['最大回撤率' , '%.4f' % downKMax])


# -------------qx.xxxx
def qxObjSet(xtim, stkVal, dcash, dret):
    ''' 設定 xtrdLib 單次交易節點資料
    
    Args:
        xtim (str): 交易時間
        stkVal (int): 股票總價值
        dcash (int): 資金
        dret (float): 回報率

    '''
    qx10 = pd.Series(zw.qxLibNil, index=zw.qxLibName)
    qx10['date'] = xtim
    qx10['cash'] = dcash
    # stkVal=xbarStkSum(qx10['xBars'],xtim)
    # stkVal=0
    qx10['stkVal'] = stkVal
    qx10['val'] = stkVal + dcash

    return qx10


# -------------



def xedit_zwXDat(df):
    ''' 編輯使用者資料格式
    
    Args:
        df (pd.DataFrame): 股票資料
            
            '''
    df = df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})
    df.sort_index(ascending=True, inplace=True)

    dx = df['open']
    df['xdiff'] = df['high'] - df['low']
    df['z-xdiff'] = df['xdiff'] * 1000 / dx
    df['z-xdiff'] = df['z-xdiff'].round(0)
    df['z-open'] = df['open'] * 1000 / dx.shift(1)
    df['z-open'] = df['z-open'].round(0)
    df['z-high'] = df['high'] * 1000 / dx
    df['z-high'] = df['z-high'].round(0)
    df['z-low'] = df['low'] * 1000 / dx
    df['z-low'] = df['z-low'].round(0)
    df['z-close'] = df['close'] * 1000 / dx
    df['z-close'] = df['z-close'].round(0)

    df['ma5'] = pd.rolling_mean(df['close'], window=5)
    df['ma10'] = pd.rolling_mean(df['close'], window=10)
    df['ma20'] = pd.rolling_mean(df['close'], window=20)
    df['ma30'] = pd.rolling_mean(df['close'], window=30)

    df['v-ma5'] = pd.rolling_mean(df['volume'], window=5)
    df['v-ma10'] = pd.rolling_mean(df['volume'], window=10)
    df['v-ma20'] = pd.rolling_mean(df['volume'], window=20)
    df['v-ma30'] = pd.rolling_mean(df['volume'], window=30)

    c20 = df.columns  # print(c20)
    if ('amount' in c20): del (df['amount'])
    if ('Adj Close' in c20): del (df['Adj Close'])

    df = df.round(decimals=2)

    clst = ["open", "high", "low", "close", "volume", "xdiff", "z-open", "z-high", "z-low", "z-close", "z-xdiff", "ma5",
            "ma10", "ma20", "ma30", "v-ma5", "v-ma10", "v-ma20", "v-ma30"]
    d30 = pd.DataFrame(df, columns=clst)

    return d30


# ------------
def df2yhaoo(df0):
    ''' 股票資料格式轉換，轉換為 Yahoo 格式
    
    Args:
        df0 (pd.DataFrame): 股票資料
        
    #Date,Open,High,Low,Close,Volume,Adj Close        
        '''

    clst = ["Open", "High", "Low", "Close", "Volume", "Adj Close"]
    df2 = pd.DataFrame(columns=clst)
    df0 = df0.rename(
        columns={'date': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'})
    # df0=df0.round(decimals=2)


    df2['Date'] = df0['Date']
    df2['Open'] = df0['Open']
    df2['High'] = df0['High']
    df2['Low'] = df0['Low']
    df2['Close'] = df0['Close']
    df2['Adj Close'] = df0['Close']
    df2['Volume'] = df0['Volume']
    df2 = df2.set_index(['Date'])

    return df2


def df2cnstk(df0):
    ''' 股票資料格式轉換，轉換為中國 A 股格式
    
    Args:
        df0 (pd.DataFrame): 股票資料
        
    #date,open,high,close,low,volume,amount    
        '''

    clst = ["open", "high", "low", "close", "volume", "amount"]
    df2 = pd.DataFrame(columns=clst)
    df0 = df0.rename(
        columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})
    # df0=df0.round(decimals=2)

    df2['date'] = df0['date']
    df2['open'] = df0['open']
    df2['high'] = df0['high']
    df2['low'] = df0['low']
    df2['close'] = df0['close']
    df2['volume'] = df0['volume']

    df2 = df2.set_index(['date'])

    return df2


def df2zw(df0):
    ''' 股票資料格式轉換，轉換為 zw 格式
    
    Args:
        df0 (pd.DataFrame): 股票資料

    '''

    clst = ["open", "high", "low", "close", "volume"]
    df2 = pd.DataFrame(columns=clst)
    df0 = df0.rename(
        columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})
    # df0=df0.round(decimals=2)

    df2['date'] = df0['date']
    df2['open'] = df0['open']
    df2['high'] = df0['high']
    df2['low'] = df0['low']
    df2['close'] = df0['close']
    df2['volume'] = df0['volume']

    df2 = df2.set_index(['date'])

    return df2


def df2zwAdj(df0):
    ''' 股票資料格式轉換，轉換為 zw 增強版格式，帶 adj close

    Args:
        df0 (pd.DataFrame): 股票資料
        '''

    df0 = df0.rename(
        columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume',
                 "Adj Close": "adj close"})
    ksgn = 'adj close'
    if ksgn not in df0.columns:
        df0[ksgn] = df0['close']
    return df0


# def df2zwAdj(df0):
#     ''' 股票資料格式轉換，轉換為 zw 增強版格式，帶 adj close
#
#     Args:
#         df0 (pd.DataFrame): 股票資料
#         '''
#
#     clst = ["open", "high", "low", "close", "volume", "adj close"]
#     df2 = pd.DataFrame(columns=clst)
#     df0 = df0.rename(
#         columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume',
#                  "Adj Close": "adj close"})
#     # df0=df0.round(decimals=2)
#
#     df0['date'] = df0.index
#     df2['date'] = df0['date']
#     for col_name in clst:
#         if col_name in df0.columns:
#             df2[col_name] = df0[col_name]
#
#     # df2['open'] = df0['open']
#     # df2['high'] = df0['high']
#     # df2['low'] = df0['low']
#     # df2['close'] = df0['close']
#     # df2['volume'] = df0['volume']
#     # 'adj close'
#     ksgn = 'adj close'
#     if ksgn in df0.columns:
#         df2[ksgn] = df0[ksgn]
#     else:
#         df2[ksgn] = df0['close']
#
#     # ----index
#     df2 = df2.set_index(['date'])
#
#     return df2


# -----OHLC
def stk_col_renLow(dat):
    ''' 股票資料格式轉換，轉換小寫列名稱
    
    Args:
        dat (pd.DataFrame): 股票資料
        '''

    dat = dat.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume',
                              "Adj Close": "adj close"})

    return dat


def stk_copy_OHLC(dat0):
    ''' 複製股票 OHLC 資料
    
    Args:
        dat0 (pd.DataFrame): 股票資料
        '''

    df0 = dat0
    df0 = stk_col_renLow(df0)
    df2 = pd.DataFrame(columns=['open', 'close', 'high', 'low'])
    df2['open'] = df0['open']
    df2['close'] = df0['close']
    df2['high'] = df0['high']
    df2['low'] = df0['low']
    df2.index = df0.index

    return df2


# ---------------- qt.misc.xxx
def downKMax(dlow, dhigh):
    '''
    downKMax(dlow,dhigh):
        回縮率計算函數
        低位元，高位，指的是投資組合的市場總值
    【輸入】：
    dlow，當前的低位，低水位，也稱，lowerWatermark
    dhigh，當前的高位，高水位，也稱，highWatermark
    【輸出】
    回縮率,百分比數值
    '''

    if dhigh > 0:
        kmax = (dlow - dhigh) / float(dhigh) * 100
    else:
        kmax = 0

    return kmax


def sharpe_rate(ser_return, rfRate, ntim=252, log_flag=False):
    '''
    sharpe_rate(ser_return,rfRate,ntim=252):
        計算夏普指數
    【輸入】
    	ser_return (Series): 收益率Series（根據ntim，按日、小時、保存）
      rfRate (float): 無風險收益率
      ntim (int): 每年交易次數（按天、小時、等計數）
         採用小時(60分鐘)線資料，ntim= 252* 6.5 = 1638.
    【輸出】
        夏普指數數值
        '''

    '''如果不是對數收益率，則轉化成對數收益率'''
    if log_flag == False:
        ser_return = np.log(ser_return + 1)
    ser_return.dropna(inplace=True)
    rstd = ser_return.std()
    '''如果波動率為0，說明ser_return是一個單一值，沒有夏普比'''
    if rstd != 0:
        rmean = ser_return.mean()
        avgExRet = rmean - rfRate / ntim
        dsharp = avgExRet / rstd
        rsharp = dsharp * np.sqrt(ntim)
    else:
        rsharp = None
    return rsharp


# ----------sta.misc



# ----


def sta_dataPre0xtim(qx, xnam0):
    ''' 策略參數設定子函數，根據預設時間，裁剪資料來源stkLib
    
    Args:
        qx (zwQuantX): zwQuantX數據包 
        xnam0 (str)： 函數標籤

    '''

    # 設定當前策略的變數參數
    qx.staName = xnam0
    qx.rfRate = 0.05  # 無風險年收益，一般為0.05(5%)，計算夏普指數等需要
    # qx.stkNum9=20000   #每手交易，預設最多20000股
    #
    # 按指定的時間週期，裁剪資料來源
    xt0k = qx.staVars[-2]
    xt9k = qx.staVars[-1]
    if (xt0k != '') or (xt9k != ''):
        # xtim0=parse('9999-01-01')
        # xtim9=parse('1000-01-01')
        # xtim0=xtim0.strftime('%Y-%m-%d')
        # xtim9=xtim9.strftime('%Y-%m-%d')
        if xt0k != '':
            if qx.xtim0 < xt0k:
                qx.xtim0 = xt0k
        if xt9k != '':
            if qx.xtim9 > xt9k:
                qx.xtim9 = xt9k
        qx.qxTimSet(qx.xtim0, qx.xtim9)
        stkLibSet8XTim(qx.xtim0, qx.xtim9)  # print('zw.stkLibCode',zw.stkLibCode)

    # ---stkInx 讀取大盤指數資料，並裁剪資料來源
    # print('finx',qx.stkInxCode)
    if qx.stkInxCode != '':
        stkInxLibRd(qx)
        stkInxLibSet8XTim(qx, qx.xtim0, qx.xtim9)

    # ============
    # ---設定qxUsr使用者變數，起始資料
    qx.qxUsr = qxObjSet(qx.xtim0, 0, qx.money, 0)


def cross_Mod(qx):
    ''' 均線交叉策略，判斷均線向上、向下趨勢
    
    Args:
        qx (zwQuantX): zwQuantX數據包
        ksma (str)：均線數據列名稱
    Return:
        1:above
        0:=
        -1:below
        '''

    kma = 'ma_%d' % qx.staVars[0]
    xbar = qx.xbarWrk
    dma, ma2n = xbar[kma][0], xbar['ma2n'][0]
    dp, dp2n = xbar['dprice'][0], xbar['dp2n'][0]
    #
    kmod = -9
    if (dp > dma) and (dp2n < ma2n) and (dp > dp2n):
        kmod = 1
        # print('   crs',kmod,'xbar\n',xbar)
    elif (dp < dma) and (dp2n > ma2n) and (dp < dp2n):
        kmod = -1
        # print('   crs',kmod,'xbar\n',xbar)

    return kmod
