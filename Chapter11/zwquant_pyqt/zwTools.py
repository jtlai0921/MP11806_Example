# -*- coding: utf-8 -*- 
'''
    模組名稱：zwTools.py
    預設縮寫：zwt,範例：zwTools.py as zwt
   【簡介】
    zwQT量化軟體，常用工具（非量化）函數模組
     
    zw量化，py量化第一品牌
    網站:http://www.ziwang.com zw網站
    py量化QQ總群  124134140   千人大群 zwPython量化&大數據
     
    開發：zw量化開源團隊 2016.04.01 首發
  
'''
#
# zwTools.py as zwt.

import sys,os
import time

import numpy as np
import pandas as pd
import tushare as ts
#import talib as ta

import matplotlib as mpl

import datetime as dt
from dateutil.rrule import *
from dateutil.parser import *

import csv
import pickle
import numexpr as ne  

import zwSys as zw  #zwQuant
import zwQTBox as zwx



    
#----hot.funs
def xinEQ(d,k0,k9):
    ''' 如果d位於(k0, k9)間，包含等於，返回True
 		    d可以是數值，字串
       '''
    #return (d>=k0)&(d<=k9)
    return ne.evaluate('(d>=k0)&(d<=k9)')

def xin(xk,k0sgn,k9sgn):
    ''' 如果xk位於(x0sgn, x9sgn)間，不含等於，返回True
       xk可以是數值，字串
       '''

    #return (xk>k0sgn)&(xk<k9sgn)    
    return ne.evaluate('(xk>k0sgn)&(xk<k9sgn)')


def iff2(kflag,x1,x0):
    ''' 二選一函數，如果kflag為True，返回值是x1；否則，返回值是x0；
        Args:
        kflag (bool): true or fall
        '''

    if kflag:
        return x1
    else:
        return x0;
def iff3(v,k,xn1,x0,x1):
    ''' 三選一函數，如果v<k，返回值是xn1；v=k，返回值是x0；v>k，返回值是x1；
    '''

    if v<k:
        return xn1
    elif v==k:
        return x0
    else:
        return x1;
        
        
def wait(n,mstr=''):
    ''' 等待n秒，mstr為提示資訊
    '''

    if mstr !='':
        print(mstr);
        
    time.sleep(n)
    
def lastDay(y,m):
    return rrule(MONTHLY, count=1, bymonthday=(-1),dtstart=dt.datetime(y,m,1))[0].day
    
#----cov.x2str
def xobj2str(xobj,xnamLst):
    ''' 物件屬性字串，根據屬性清單，生成字串
        
        #qxLibName=['time','ID','stkVal','cash','dret','val'];
        '''

    #print('\n::QxUsr');
    dss='';
    for cnam in xnamLst:
        ess=str(xobj[cnam]);
        dss=dss+cnam+','+ess+'; ';

    return dss

#----debug
def xdebug(xmod,mnam,fnam):
    ''' 輸出調試資訊
    
    Args:
        xmod (int): #調試Mod，0：不調試；1：主模組，',__name__=__main__；2：子模組
        mnam (str): __name__
        fnam (str): sys._getframe().f_code.co_name
            
    i.e zwt.xdebug(qx.debugMod,__name__,sys._getframe().f_code.co_name)
    ''' 

    if xmod==0:
        pass;
    elif xmod==1:
        if mnam=='__main__':print('\n@mod:',mnam,',@fun:',fnam);
    elif xmod==2:
        print('\n@mod:',mnam,',@fun:',fnam);

    
#----lst.xxx
def lst4dir(rss):
    ''' 目錄檔生成清單資料
    '''

    flst=[] 
    for root,dirs,files in os.walk(rss):
        for fss in files:
            #print(fss)
            flst.append(fss)
    return flst   
    
    
def listRd(fnam):
    ''' 讀取清單數據
    '''

    f=open(fnam,'rb') 
    lst=pickle.load(f);
    f.close() 
    return lst    
    
    
def listWr(fnam,lst):
    ''' 儲存清單資料
    '''

    fhnd=open(fnam,'wb') 
    #testList = [ 123, { 'Calories' : 190 }, 'Mr. Anderson', [ 1, 2, 7 ] ] 
    pickle.dump (lst,fhnd) #,True
    fhnd.close() 


def listPr(lst):
    ''' 輸出清單資訊
    '''

    for x in lst:
        print(x);
