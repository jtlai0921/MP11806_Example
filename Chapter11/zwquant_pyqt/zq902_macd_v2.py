# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

#zwQuant
import zwSys as zw
import zwTools as zwt
import zwQTBox as zwx
import zwQTDraw as zwdr
import zwBacktest as zwbt
import zwStrategy as zwsta
import zw_talib as zwta

#=======================    

    
def bt_endRets(qx):
    #---ok ，測試完畢
    # 儲存測試資料，qxlib：每日收益等資料；xtrdLib：交易清單資料
    #qx.qxLib=qx.qxLib.round(4)
    qx.qxLib.to_csv(qx.fn_qxLib,index=False,encoding='utf-8')
    qx.xtrdLib.to_csv(qx.fn_xtrdLib,index=False,encoding='utf-8')
    qx.prQLib()
    #
    #-------計算交易回報資料
    zwx.zwRetTradeCalc(qx)
    zwx.zwRetPr(qx)

    print('')
    print('每日交易推薦')
    print('::xtrdLib',qx.fn_xtrdLib)
    print(qx.xtrdLib.tail())
    #print(qx.xtrdLib)


    # 使用自訂輸出結果
    if qx.pyqt_mode_flag == True:
        zwdr.my_pyqt_show(qx)
    else:
        zwdr.my_qunt_plot(qx)


#==================main
#--------init，設定參數
rss='dat\\'  #rss='\\zwdat\\cn\\day\\'
xlst=['600401']   #600401,*ST海潤
qx=zwbt.bt_init(xlst,rss,'macd20',10000)

#---設定策略參數
qx.staVars=[12,26,'2015-01-01','']    
qx.debugMod=1
qx.pyqt_mode_flag = True
qx.staFun=zwsta.macd20 #---繫結策略函數&執行回溯主函數

#---根據目前策略，對資料進行預先處理
zwsta.macd10_dataPre(qx,'macd20','close')

#----執行回溯主程式
zwbt.zwBackTest(qx)

#----輸出回溯結果
bt_endRets(qx) #

