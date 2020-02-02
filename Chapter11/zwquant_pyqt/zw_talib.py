# -*- coding: utf-8 -*- 
'''
    模組名稱：zwpd_talib.py
    預設縮寫：zwta,範例：import zwpd_talib as zwta
    【簡介】
    zw版的talib函數封裝，第一批以pandas_talib.py的29個函數為藍本。

    zw_talib函式程式庫v0.5版，所有33個函數，均已測試通過，
    運行平台：python3.5，zwPython2016m2    
     
     zw量化，py量化第一品牌
     網站:http://www.ziwang.com zw網站
     py量化QQ總群  124134140   千人大群 zwPython量化&大資料 
     
     開發：zw量化開源團隊 2016.03.28
     
    pandas_talib.py參見：
    https://www.quantopian.com/posts/technical-analysis-indicators-without-talib-code
    https://github.com/panpanpandas/ultrafinance/blob/master/ultrafinance/pyTaLib/pandasImpl.py
    預設資料格式，採用zwDat標準，全部小寫
    ohlcv:open,high,low,close,volumns

---------zwtalib 首批函數名稱
:: ACCDIST(df, n):集散指標(A/D)——Accumulation/Distribution,是由價格和成交量的變化而決定的
:: ADX(df, n, n_ADX): 	 #adx，中文全稱：平均趨向指數，ADX指數是反映趨向變動的程度，而不是方向的本身;英文全稱：Average Directional Index 或者Average Directional Movement Index
:: ATR(df, n): ATR,均幅指標（Average True Ranger）,取一定時間週期內的股價波動幅度的移動平均值，主要用於研判買賣時機
:: BBANDS(df, n):布林帶.Bollinger Bands 
:: BBANDS_UpLow(df, n): zw改進版的布林帶talib函數
:: CCI(df, n): CCI順勢指標(Commodity Channel Index),CCI指標，是由美國股市分析家唐納德::藍伯特（Donald Lambert）所創造的，是一種重點研判股價偏離度的股市分析工具。
:: COPP(df, n):估波指標（Coppock Curve）,又稱“估波曲線”，通過計算月度價格的變化速率的加權平均值來測量市場的動量，屬於長線指標。估波指標由Edwin::Sedgwick::Coppock於1962年提出，主要用於判斷牛市的到來。該指標用於研判大盤指數較為可靠，一般較少用於個股；再有，該指標只能產生買進訊號。依估波指標買進股票後，應另外尋求其他指標來輔助賣出訊號。估波指標的週期參數一般設置為11、14，加權平均參數為10，也可以結合指標的平均線進行分析
:: Chaikin(df):佳慶指標（Chaikin Oscillator）,是由馬可::蔡金（Marc Chaikin）提出的，聚散指標（A/D）的改良版本。
:: DONCH(df, n):奇安通道指標,Donchian Channel,該指標是由Richard Donchian發明的，是有3條不同顏色的曲線組成的，該指標用週期（一般都是20）內的最高價和最低價來顯示市場的波動性;當其通道窄時表示市場波動較小，反之通道寬則表示市場波動比較大。
:: EMA(df, n):指數平均數指標(Exponential Moving Average，EXPMA或EMA),指數平均數指標也叫EXPMA指標，它也是一種趨向類指標，其構造原理是仍然對價格收盤價進行算術平均，並根據計算結果來進行分析，用於判斷價格未來走勢的變動趨勢。
:: EOM(df, n):簡易波動指標(Ease of Movement Value)，又稱EMV指標;它是由RichardW．ArmJr．根據等量圖和壓縮圖的原理設計而成,目的是將價格與成交量的變化結合成一個波動指標來反映股價或指數的變動狀況。由於股價的變化和成交量的變化都可以引發該指標數值的變動,因此,EMV實際上也是一個量價合成指標。
:: FORCE(df, n):勁道指數(Force Index);勁道指數是由亞歷山大::埃爾德(Alexander Elder)博士設計的一種擺蕩指標，藉以衡量每個漲勢中的多頭勁道與每個跌勢中的空頭勁道。勁道指數結合三項主要的市場資訊：價格變動的方向、它的幅度與成交量。它是由一個嶄新而實用的角度，把成交量納入交易決策中。
:: KELCH(df, n):肯特納通道（Keltner Channel，KC）,肯特納通道（KC）是一個移動平均通道，由三條線組合而成(上通道、中通道及下通道)。通道，一般情況下是以上通道線及下通道線的分界作為買賣的最大可能性。若股價於邊界出現不沉常的波動，即表示買賣機會。
:: KST(df, r1, r2, r3, r4, n1, n2, n3, n4): 確然指標（KST）又稱為完定指標，該指標參考長、中、短期的變速率ROC，以瞭解不同時間迴圈對市場的影響。該指標將數個週期的價格變動率函數作加權以及再平滑繪製長短曲線，其特色在通過修正的價格變動組合來判斷趨勢，精准掌握轉折買賣點。
:: KST4(df, r1, r2, r3, r4, n1, n2, n3, n4): 	zw修訂版，KST確然指標,確然指標（KST）又稱為完定指標，該指標參考長、中、短期的變速率ROC，以瞭解不同時間迴圈對市場的影響。該指標將數個週期的價格變動率函數作加權以及再平滑繪製長短曲線，其特色在通過修正的價格變動組合來判斷趨勢，精准掌握轉折買賣點。
:: MA(df, n):移動平均線,Moving Average，即最常用的均線指標
:: MACD(df, n_fast, n_slow): #MACD指標信號和MACD的區別, MACD Signal and MACD difference，MACD是由一快及一慢指數移動平均（EMA）之間的差計算出來。“快”指短時期的EMA，而“慢”則指長時期的EMA，最常用的是12及26日EMA。
:: MFI(df, n): MFI,資金流量指標和比率,Money Flow Index and Ratio，資金流量指標又稱為量相對強弱指標（Volume Relative Strength Index，VRSI）；根據成交量來計測市場供需關係和買賣力道。該指標是通過反映股價變動的四個元素：上漲的天數、下跌的天數、成交量增加幅度、成交量減少幅度；來研判量能的趨勢，預測市場供求關係和買賣力道，屬於量能反趨向指標。	
:: MOM(df, n):動量線，英文全名MOmentum，簡稱MOM。“動量”這一名詞，市場上的解釋相當廣泛。以Momentum命名的指標，種類更是繁多。綜合而言，動量可以視為一段期間內，股價漲跌變動的比率。
:: MassI(df):梅斯線（Mass Index），梅斯線是Donald Dorsey累積股價波幅寬度之後，所設計的震盪曲線。本指標最主要的作用，在於尋找飆漲股或者極度弱勢股的重要趨勢反轉點。MASS指標是所有區間震盪指標中，風險係數最小的一個。		
:: OBV(df, n):能量潮指標（On Balance Volume，OBV），OBV指標是葛蘭維（Joe Granville）於本世紀60年代提出的，並被廣泛使用。股市技術分析的四大要素：價、量、時、空。OBV指標就是從“量”這個要素作為突破口，來發現熱門股票、分析股價運動趨勢的一種技術指標。它是將股市的人氣——成交量與股價的關係數位化、直觀化，以股市的成交量變化來衡量股市的推動力，從而研判股價的走勢。關於成交量方面的研究，OBV能量潮指標是一種相當重要的分析指標之一。
:: PPSR(df):支點，支撐線和阻力線.Pivot Points, Supports and Resistances；PIVOT指標的觀念很簡單，不需要計算任何東西，它純粹只是一個分析反轉點的方法而已。PIVOT意思是指“軸心”，軸心是用來確認反轉的基準，所以PIVOT指標其實就是找軸心的方法；PIVOT指標，經常與布林帶資料一起分析。
:: ROC(df, n):變動率(Rate of change,ROC)，ROC是由當天的股價與一定的天數之前的某一天股價比較，其變動速度的大小,來反映股票市場變動的快慢程度。ROC，也叫做變動速度指標、變動率指標或變化速率指標。	
:: RSI(df, n): RSI，相對強弱指標,Relative Strength Index，也稱相對強弱指數、相對力度指數；RSI，是通過比較一段時期內的平均收盤漲數和平均收盤跌數來分析市場買沽盤的意向和實力，從而作出未來市場的走勢。RSI通過特定時期內股價的變動情況計算市場買賣力量對比，來判斷股票價格內部本質強弱、推測價格未來的變動方向的技術指標。
:: RSI100(df, n):zw版RSI相對強弱指數，取0..100之間的數值
:: STDDEV(df, n):標準差,Standard Deviation
:: STOD(df, n):隨機指標D值,Stochastic oscillator %D；隨機指標，又稱KD指標，KDJ指標；隨機指標綜合了動量觀念、強弱指標及移動平均線的優點，用來度量股價脫離價格正常範圍的變異程度。隨機指標考慮的不僅是收盤價，而且有近期的最高價和最低價，這避免了僅考慮收盤價而忽視真正波動幅度的弱點。隨機指標一般是根據統計學的原理，通過一個特定的週期（常為9日、9周等）內出現過的最高價、最低價，及最後一個計算週期的收盤價及這三者之間的比例關係，來計算最後一個計算週期的未成熟隨機值RSV，然後根據平滑移動平均線的方法來計算K值、D值與J值，並繪成曲線圖來研判股票走勢。
:: STOK(df):隨機指標K值,Stochastic oscillator %K 
:: TRIX(df, n):TRIX指標又叫三重指數平滑移動平均指標，Triple Exponentially Smoothed Average
:: TSI(df, r, s): TSI，真實強度指數,True Strength Index，TSI是相對強弱指數 (RSI) 的變體。TSI 使用價格動量的雙重平滑指數移動平均線，剔除價格的震盪變化並發現趨勢的變化。r一般取25，是一般取13。
:: ULTOSC(df): UOS，終極指標（Ultimate Oscillator），終極指標，由拉瑞::威廉（Larry Williams）所創。他認為現行使用的各種振盪指標，對於週期參數的選擇相當敏感。不同的市況，不同參數設定的振盪指標，產生的結果截然不同。因此，選擇最佳的參數組含，成為使用振盪指標之前，最重要的一道手續。為了將參數週期調和至最佳狀況，拉瑞::威廉經過不斷測試的結果，先找出三個週期不同的振盪指標，再將這些週期參數，按照反比例的方式，製作成常數因數。然後，依照加權的方式，將三個週期不同的振盪指標，分別乘以不同比例的常數，加以綜合製作成UOS指標。經過一連串參數順化的過程後，UOS指標比一般單一參數的振盪指標，更能夠順應各種不同的市況。
:: Vortex(df, n):螺旋指標,Vortex Indicator，參見http://www.vortexindicator.com/VFX_VORTEX.PDF


'''

import sys,os
import numpy as np
import pandas as pd



#----

def ACCDIST(df, n,ksgn='close'): 
    '''
    def ACCDIST(df, n,ksgn='close'): 
    #集散指標(A/D)——Accumulation/Distribution
        是由價格和成交量的變化而決定的
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：ad_{n}，輸出資料
    '''
    xnam='ad_{d}'.format(d=n)
    ad = (2 * df[ksgn] - df['high'] - df['low']) / (df['high'] - df['low']) * df['volume']  
    M = ad.diff(n - 1)  
    N = ad.shift(n - 1)  
    ROC = M / N  
    AD = pd.Series(ROC, name = xnam)  #'Acc/Dist_ROC_' + str(n)
    df = df.join(AD)  
    return df


def ADX(df, n, n_ADX,ksgn='close'):
    '''
    def ADX(df, n, n_ADX):
    adx，中文全稱：平均趨向指數，ADX指數是反映趨向變動的程度，而不是方向的本身
    英文全稱：Average Directional Index 或者Average Directional Movement Index
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        n_ADX,adx週期
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：adx_{n}_{n2}，輸出資料
    '''
    i = 0
    UpI = []
    DoI = []
    xnam='adx_{n}_{n2}'.format(n=n,n2=n_ADX)
    while i + 1 <= len(df) - 1:  # df.index[-1]:
        #UpMove = df.get_value(i + 1, 'high') - df.get_value(i, 'high')
        #DoMove = df.get_value(i, 'low') - df.get_value(i + 1, 'low')
        #..UpMove=df['high'].iloc[i+1]-df['high'].iloc[i]
        UpMove = df['high'].iloc[i+1] - df['high'].iloc[i]
        DoMove = df['low'].iloc[i] - df['low'].iloc[i+1]
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    i = 0
    TR_l = [0]
    while i < len(df) - 1:  # df.index[-1]:
        #TR = max(df.get_value(i + 1, 'high'), df.get_value(i, 'close')) - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))
        TR = max(df['high'].iloc[i+1], df[ksgn].iloc[i]) - min(df['low'].iloc[i+1], df[ksgn].iloc[i])
        TR_l.append(TR)
        i = i + 1
    TR_s = pd.Series(TR_l)
    ATR = pd.Series(pd.ewma(TR_s, span=n, min_periods=n))
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(pd.ewma(UpI, span=n, min_periods=n - 1) / ATR)
    NegDI = pd.Series(pd.ewma(DoI, span=n, min_periods=n - 1) / ATR)
    ds = pd.Series(pd.ewma(abs(PosDI - NegDI) / (PosDI + NegDI), span=n_ADX, min_periods=n_ADX - 1), name=xnam)
    ds.index=df.index;df[xnam]=ds
    #df = df.join(ds)  
    return df


def ATR(df, n,ksgn='close'):  
    '''
    def ATR(df, n,ksgn='close'):  
    #ATR,均幅指標（Average True Ranger）,取一定時間週期內的股價波動幅度的移動平均值，主要用於研判買賣時機
    
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：atr_{n}，輸出資料
    '''    
    xnam='atr_{n}'.format(n=n)
    i = 0
    TR_l = [0]
    while i < len(df) - 1:  # df.index[-1]:
    # for i, idx in enumerate(df.index)
        # TR=max(df.get_value(i + 1, 'High'), df.get_value(i, 'Close')) - min(df.get_value(i + 1, 'Low'), df.get_value(i, 'Close'))
        #TR = max(df['High'].iloc[i + 1], df['Close'].iloc[i] - min(df['Low'].iloc[i + 1], df['Close'].iloc[i]))
        TR = max(df['high'].iloc[i + 1], df[ksgn].iloc[i] - min(df['low'].iloc[i + 1], df[ksgn].iloc[i]))
        TR_l.append(TR)
        i = i + 1;#print('#',i,TR)
    TR_s = pd.Series(TR_l)
    ds = pd.Series(pd.ewma(TR_s, span=n, min_periods=n), name=xnam)
    #df = df.join(ds)  
    ds.index=df.index;df[xnam]=ds
    #print('ds',ds.head())
    return df
    


def BBANDS(df, n,ksgn='close'):  
    '''
    def BBANDS(df, n,ksgn='close'):  
    布林帶.Bollinger Bands  
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了2欄：_{n}，_{n}b，輸出資料
    '''    
    xnam='boll_{n}'.format(n=n)
    MA = pd.Series(pd.rolling_mean(df[ksgn], n))  
    MSD = pd.Series(pd.rolling_std(df[ksgn], n))  
    b1 = 4 * MSD / MA  
    B1 = pd.Series(b1, name = xnam+'b')  
    df = df.join(B1)  
    b2 = (df[ksgn] - MA + 2 * MSD) / (4 * MSD)  
    B2 = pd.Series(b2, name = xnam)  
    df = df.join(B2)  
    return df    


def BBANDS_UpLow(df, n,ksgn='close'):  
    '''
    BBANDS_UpLow(df, n,ksgn='close'):  
    zw改進版的布林帶talib函數.Bollinger Bands  
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了4欄：
            boll_ma，布林帶均線數據
            boll_std，布林帶方差據
            boll_up，布林帶上軌帶差據
            boll_low，布林帶下軌帶差據
    '''        
    df['boll_ma']=pd.Series(pd.rolling_mean(df[ksgn], n))  
    df['boll_std']= pd.Series(pd.rolling_std(df[ksgn], n))  
    #df[#MSD = pd.Series(pd.rolling_std(df[ksgn], n))  
    MA=df['boll_ma']
    MSD=df['boll_std']
    #
    knum=2
    df['boll_up']= MA + MSD * knum    #knum=numStdDev
    df['boll_low']= MA - MSD * knum

    return df 


def CCI(df, n,ksgn='close'):  
    '''
    def CCI(df, n,ksgn='close'):  
    CCI順勢指標(Commodity Channel Index)
    CCI指標，是由美國股市分析家唐納德•藍伯特（Donald Lambert）所創造的，是一種重點研判股價偏離度的股市分析工具。

    
    MA是簡單平均線，也就是平常說的均線
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：cci_{n}，輸出資料
    '''
    xnam='cci_{d}'.format(d=n)
    PP = (df['high'] + df['low'] + df[ksgn]) / 3  
    CCI = pd.Series((PP - pd.rolling_mean(PP, n)) / pd.rolling_std(PP, n), name = xnam)  
    df = df.join(CCI)  
    
    return df
    

#Coppock Curve  
def COPP(df, n,ksgn='close'):  
    '''
    def COPP(df, n):  				
　　估波指標（Coppock Curve）又稱“估波曲線”，通過計算月度價格的變化速率的加權平均值來測量市場的動量，屬於長線指標。
　　估波指標由Edwin•Sedgwick•Coppock於1962年提出，主要用於判斷牛市的到來。
    該指標用於研判大盤指數較為可靠，一般較少用於個股；再有，該指標只能產生買進訊號。
    依估波指標買進股票後，應另外尋求其他指標來輔助賣出訊號。
    估波指標的週期參數一般設置為11、14，加權平均參數為10，也可以結合指標的平均線進行分析

    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：copp_{n}，輸出資料
    '''
    xnam='copp_{d}'.format(d=n)
    M = df[ksgn].diff(int(n * 11 / 10) - 1)  
    N = df[ksgn].shift(int(n * 11 / 10) - 1)  
    ROC1 = M / N  
    M = df[ksgn].diff(int(n * 14 / 10) - 1)  
    N = df[ksgn].shift(int(n * 14 / 10) - 1)  
    ROC2 = M / N  
    Copp = pd.Series(pd.ewma(ROC1 + ROC2, span = n, min_periods = n), name = xnam)  
    df = df.join(Copp)  
    return df
    
#Chaikin Oscillator  
def CHAIKIN(df,ksgn='close'):   
    '''
    def CHAIKIN(df):					
    #佳慶指標（Chaikin Oscillator）
　　佳慶指標（CHAIKIN）是由馬可•蔡金（Marc Chaikin）提出的，聚散指標（A/D）的改良版本。
    【輸入】
        df, pd.dataframe格式資料來源
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：_{n}，輸出資料
    '''
    xnam='ck'
    ad = (2 * df[ksgn] - df['high'] - df['low']) / (df['high'] - df['low']) * df['volume']  
    Chaikin = pd.Series(pd.ewma(ad, span = 3, min_periods = 2) - pd.ewma(ad, span = 10, min_periods = 9), name = xnam)  
    df = df.join(Chaikin)  
    return df
    

#Donchian Channel  
def DONCH(df, n):  
    '''
    def DONCH(df, n):      
      #奇安通道指標,Donchian Channel  
	該指標是由Richard Donchian發明的，是有3條不同顏色的曲線組成的，該指標用週期（一般都是20）內的最高價和最低價來顯示市場的波動性
	當其通道窄時表示市場波動較小，反之通道寬則表示市場波動比較大。
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了2欄：donch__{n}sr，中間輸出資料
            donch__{n}，輸出資料
    '''
    xnam='donch_{d}'.format(d=n)
    i = 0  
    DC_l = []  
    while i < n - 1:  
        DC_l.append(0)  
        i = i + 1  
    i = 0  
    while (i + n - 1) <=(len(df) - 1):  #df.index[-1]:  
        #DC = max(df['high'].ix[i:i + n - 1]) - min(df['low'].ix[i:i + n - 1])  
        DC = max(df['high'].iloc[i:i + n - 1]) - min(df['low'].iloc[i:i + n - 1])  
        DC_l.append(DC)  
        i = i + 1  
    #
    #DC_l.append(DC)  
    #
    DonCh = pd.Series(DC_l, name = xnam)   #'Donchian_' + str(n)
    
    #df = df.join(DonCh)  
    DonCh.index=df.index;
    df[xnam+'_sr']=DonCh
    df[xnam]=df[xnam+'_sr'].shift(n - 1)  
    #DonCh = DonCh.shift(n - 1)  
    return df
    


def EMA(df, n,ksgn='close'):  
    '''
    EMA(df, n,ksgn='close'):  
    #Exponential Moving Average  
    EMA是指數平滑移動平均線，也叫EXPMA指標，也稱為：SMMA 
    是平均線的一個變種，EMA均線較MA更加專業一些。
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：ema_{n}，輸出資料
    '''
    xnam='ema_{n}'.format(n=n)
    EMA = pd.Series(pd.ewma(df[ksgn], span = n, min_periods = n - 1), name = xnam)  
    df = df.join(EMA)  
    return df    
   
    

#Ease of Movement  
def EOM(df, n):   
    '''
    def EOM(df, n):  					
    簡易波動指標(Ease of Movement Value)，又稱EMV指標
   它是由RichardW．ArmJr．根據等量圖和壓縮圖的原理設計而成,目的是將價格與成交量的變化結合成一個波動指標來反映股價或指數的變動狀況。
   由於股價的變化和成交量的變化都可以引發該指標數值的變動,因此,EMV實際上也是一個量價合成指標。


    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了2欄：eom_{n}，輸出資料
            eom_x，10e10倍的輸出資料
    '''
    xnam='eom_{d}'.format(d=n)
    EoM = (df['high'].diff(1) + df['low'].diff(1)) * (df['high'] - df['low']) / (2 * df['volume'])  
    Eom_ma = pd.Series(pd.rolling_mean(EoM, n), name = xnam)  
    df = df.join(Eom_ma)  
    df['eom_x']=df[xnam]*10e10
    return df



def FORCE(df, n,ksgn='close'):   
    '''
    def FORCE(df, n):					
    #勁道指數(Force Index)
　　勁道指數是由亞歷山大•埃爾德(Alexander Elder)博士設計的一種擺蕩指標，藉以衡量每個漲勢中的多頭勁道與每個跌勢中的空頭勁道。
　　勁道指數結合三項主要的市場資訊：價格變動的方向、它的幅度與成交量。它是由一個嶄新而實用的角度，把成交量納入交易決策中。

    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了2欄：force__{n}，輸出資料
          force_x，縮小10e7倍的輸出資料
    '''
    xnam='force_{d}'.format(d=n)
    F = pd.Series(df[ksgn].diff(n) * df['volume'].diff(n), name = xnam)  
    df = df.join(F)  
    df['force_x']=df[xnam]/10e7
    return df

def KELCH(df, n,ksgn='close'):
    '''
    def KELCH(df, n):  				#肯特納通道（Keltner Channel，KC）
　　肯特納通道（KC）是一個移動平均通道，由三條線組合而成(上通道、中通道及下通道)。
	KC通道，一般情況下是以上通道線及下通道線的分界作為買賣的最大可能性。
  	若股價於邊界出現不沉常的波動，即表示買賣機會。    
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了3欄：kc_m，中間數據
            kc_u，up上軌道數據
            kc_d，down下軌道資料
    '''
    xnam='kc_m'
    xnam2='kc_u'
    xnam3='kc_d'
    KelChM = pd.Series(pd.rolling_mean((df['high'] + df['low'] + df[ksgn]) / 3, n), name = xnam)  #'KelChM_' + str(n)
    KelChU = pd.Series(pd.rolling_mean((4 * df['high'] - 2 * df['low'] + df[ksgn]) / 3, n), name = xnam2)   #'KelChU_' + str(n)
    KelChD = pd.Series(pd.rolling_mean((-2 * df['high'] + 4 * df['low'] + df[ksgn]) / 3, n), name =xnam3)    #'KelChD_' + str(n)
    df = df.join(KelChM)  
    df = df.join(KelChU)  
    df = df.join(KelChD)  
    
    return df




def KST(df, r1, r2, r3, r4, n1, n2, n3, n4,ksgn='close'): 
    '''
    def KST(df, r1, r2, r3, r4, n1, n2, n3, n4,ksgn='close'): 
    #KST Oscillator  
    確然指標（KST）又稱為完定指標，該指標參考長、中、短期的變速率ROC，以瞭解不同時間迴圈對市場的影響。
    該指標將數個週期的價格變動率函數作加權以及再平滑繪製長短曲線，其特色在通過修正的價格變動組合來判斷趨勢，精准掌握轉折買賣點。
    
    tst:
       (r1, r2, r3, r4, n1, n2, n3, n4) = (1, 2, 3, 4, 6, 7, 9, 9)
    '''
    '''
    
    【輸入】
        df, pd.dataframe格式資料來源
        r1..r4,n1..n4，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：ksf，輸出資料
    '''
    xnam='kst';
    M = df[ksgn].diff(r1 - 1)  
    N = df[ksgn].shift(r1 - 1)  
    ROC1 = M / N  
    M = df[ksgn].diff(r2 - 1)  
    N = df[ksgn].shift(r2 - 1)  
    ROC2 = M / N  
    M = df[ksgn].diff(r3 - 1)  
    N = df[ksgn].shift(r3 - 1)  
    ROC3 = M / N  
    M = df[ksgn].diff(r4 - 1)  
    N = df[ksgn].shift(r4 - 1)  
    ROC4 = M / N  
    #'KST_' + str(r1) + '_' + str(r2) + '_' + str(r3) + '_' + str(r4) + '_' + str(n1) + '_' + str(n2) + '_' + str(n3) + '_' + str(n4)
    KST = pd.Series(pd.rolling_sum(ROC1, n1) + pd.rolling_sum(ROC2, n2) * 2 + pd.rolling_sum(ROC3, n3) * 3 + pd.rolling_sum(ROC4, n4) * 4, name = xnam)  
    df = df.join(KST)  
    return df

def KST4(df, r1, r2, r3, r4,ksgn='close'): 
    '''
    def KST4(df, r1, r2, r3, r4, n1, n2, n3, n4,ksgn='close'): 
    zw修訂版，KST確然指標
    確然指標（KST）又稱為完定指標，該指標參考長、中、短期的變速率ROC，以瞭解不同時間迴圈對市場的影響。
    該指標將數個週期的價格變動率函數作加權以及再平滑繪製長短曲線，其特色在通過修正的價格變動組合來判斷趨勢，精准掌握轉折買賣點。
    
    tst:
       (r1, r2, r3, r4) = (9,13,18,24);(12,20,30,40)
    
    【輸入】
        df, pd.dataframe格式資料來源
        r1,r2,r3,r4，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：ksf，輸出資料
    
    '''
    df=KST(df,r1, r2, r3, r4,r1, r2, r3, r4,ksgn)
    
    return df

 
def MA(df, n,ksgn='close'):  
    '''
    def MA(df, n,ksgn='close'):  
    #Moving Average  
    MA是簡單平均線，也就是平常說的均線
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：ma_{n}，均線數據
    '''
    xnam='ma_{n}'.format(n=n)
    #ds5 = pd.Series(pd.rolling_mean(df[ksgn], n), name =xnam)  
    ds2=pd.Series(df[ksgn], name =xnam);
    ds5 = ds2.rolling(center=False,window=n).mean() 
    #print(ds5.head()); print(df.head())
    df = df.join(ds5)  
    
    return df
   
   


#MACD, MACD Signal and MACD difference  
def MACD(df, n_fast, n_slow,ksgn='close'): 
    '''
    def MACD(df, n_fast, n_slow):           
      #MACD指標信號和MACD的區別, MACD Signal and MACD difference   
	MACD是查拉爾•阿佩爾(Geral Appel)於1979年提出的，由一快及一慢指數移動平均（EMA）之間的差計算出來。
	“快”指短時期的EMA，而“慢”則指長時期的EMA，最常用的是12及26日EMA：

    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了3欄：macd,sign,mdiff
    '''
    xnam='macd'.format(n=n_fast,n2=n_slow)
    xnam2='msign'.format(n=n_fast,n2=n_slow)
    xnam3='mdiff'.format(n=n_fast,n2=n_slow)
    EMAfast = pd.Series(pd.ewma(df[ksgn], span = n_fast, min_periods = n_slow - 1))  
    EMAslow = pd.Series(pd.ewma(df[ksgn], span = n_slow, min_periods = n_slow - 1))  
    MACD = pd.Series(EMAfast - EMAslow, name = xnam)  
    MACDsign = pd.Series(pd.ewma(MACD, span = 9, min_periods = 8), name =xnam2)  
    MACDdiff = pd.Series(MACD - MACDsign, name =xnam3)  
    df = df.join(MACD)  
    df = df.join(MACDsign)  
    df = df.join(MACDdiff)  
    return df
    



def MFI(df, n,ksgn='close'):   
    '''
    def MFI(df, n):					
    MFI,資金流量指標和比率,Money Flow Index and Ratio
　　資金流量指標又稱為量相對強弱指標（Volume Relative Strength Index，VRSI），
	英文全名Money Flow Index，縮寫為MFI，根據成交量來計測市場供需關係和買賣力道。
	該指標是通過反映股價變動的四個元素：上漲的天數、下跌的天數、成交量增加幅度、成交量減少幅度
	來研判量能的趨勢，預測市場供求關係和買賣力道，屬於量能反趨向指標。	    
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：mfi_{n}，輸出資料
    '''
    xnam='mfi_{d}'.format(d=n)
    PP = (df['high'] + df['low'] + df[ksgn]) / 3  
    i = 0  
    PosMF = [0]  
    while i <(len(df) - 1): #df.index[-1]:  
        if PP.iloc[i + 1] > PP.iloc[i]:  
            #PosMF.append(PP[i + 1] * df.get_value(i + 1, 'volume'))  
            PosMF.append(PP.iloc[i + 1] * df['volume'].iloc[i + 1])  
        else:  
            PosMF.append(0)  
        i = i + 1  
    #    
    PosMF = pd.Series(PosMF)  
    TotMF = PP * df['volume']  
    #MFR = pd.Series(PosMF / TotMF)  
    PosMF.index=TotMF.index
    MFR =PosMF / TotMF
    MFI = pd.Series(pd.rolling_mean(MFR, n), name = xnam)  
    #df = df.join(MFI)  
    #MFI.index=df.index;
    df[xnam]=MFI
    return df
    
def MOM(df, n,ksgn='close'):  
    '''
    
    def MOM(df, n,ksgn='close'):  
　　動量線，英文全名MOmentum，簡稱MOM。“動量”這一名詞，市場上的解釋相當廣泛。以Momentum命名的指標，種類更是繁多。
		綜合而言，動量可以視為一段期間內，股價漲跌變動的比率。
    
    動量指標.Momentum  
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：mom_{n}，輸出資料
    '''
    xnam='mom_{n}'.format(n=n)
    #M = pd.Series(df['close'].diff(n), name = 'Momentum_' + str(n))  
    M = pd.Series(df[ksgn].diff(n), name = xnam)  
    df = df.join(M)  
    return df
    



def MASS(df):  
    '''
    def MassI(df):					
    梅斯線（Mass Index）
　　梅斯線是Donald Dorsey累積股價波幅寬度之後，所設計的震盪曲線。
		本指標最主要的作用，在於尋找飆漲股或者極度弱勢股的重要趨勢反轉點。
　　MASS指標是所有區間震盪指標中，風險係數最小的一個。		
    
    【輸入】
        df, pd.dataframe格式資料來源
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：mass，輸出資料
    '''
    xnam='mass'
    Range = df['high'] - df['low']  
    EX1 = pd.ewma(Range, span = 9, min_periods = 8)  
    EX2 = pd.ewma(EX1, span = 9, min_periods = 8)  
    Mass = EX1 / EX2  
    MassI = pd.Series(pd.rolling_sum(Mass, 25), name = xnam)  #'Mass Index'
    df = df.join(MassI)  
    return df    
    



def OBV(df, n,ksgn='close'):   
    '''
    def OBV(df, n,ksgn='close'):   
    #能量潮指標（On Balance Volume，OBV）
    OBV指標是葛蘭維（Joe Granville）於本世紀60年代提出的，並被廣泛使用。
    股市技術分析的四大要素：價、量、時、空。OBV指標就是從“量”這個要素作為突破口，來發現熱門股票、分析股價運動趨勢的一種技術指標。
    它是將股市的人氣——成交量與股價的關係數位化、直觀化，以股市的成交量變化來衡量股市的推動力，從而研判股價的走勢。
    關於成交量方面的研究，OBV能量潮指標是一種相當重要的分析指標之一。    
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了2欄：obv_{n}，輸出資料
        obv_x，放大10e6倍的輸出資料
    '''
    xnam='obv_{d}'.format(d=n)
    i = 0  
    OBV = [0]  
    while i <  len(df) - 1:  #df.index[-1]
        #if df.get_value(i + 1, ksgn) - df.get_value(i, ksgn) > 0:  
        if df[ksgn].iloc[i+1]-df[ksgn].iloc[i] > 0:  
            #OBV.append(df.get_value(i + 1, 'Volume'))  
            OBV.append(df['volume'].iloc[i + 1])  
        if (df[ksgn].iloc[i+1]-df[ksgn].iloc[i]) == 0:  
            OBV.append(0)  
        if (df[ksgn].iloc[i+1]-df[ksgn].iloc[i]) < 0:  
            OBV.append(-df['volume'].iloc[i + 1])  
        i = i + 1  
    OBV = pd.Series(OBV)  
    OBV_ma = pd.Series(pd.rolling_mean(OBV, n), name = xnam)  
    #df = df.join(OBV_ma)  
    OBV_ma.index=df.index;
    df[xnam]=OBV_ma
    df['obv_x']=df[xnam]/10e6
    return df
    
    



def PPSR(df):  
    '''
    def PPSR(df):  					
     支點，支撐線和阻力線.Pivot Points, Supports and Resistances  
	PIVOT指標的觀念很簡單，不需要計算任何東西，它純粹只是一個分析反轉點的方法而已。
	PIVOT意思是指“軸心”，軸心是用來確認反轉的基準，所以PIVOT指標其實就是找軸心的方法
     PIVOT指標，經常與布林帶資料一起分析。

    【輸入】
        df, pd.dataframe格式資料來源
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了7欄：pp,s1,s2,s3,r1,r2,r3，輸出資料
    '''
    PP = pd.Series((df['high'] + df['low'] + df['close']) / 3)  
    R1 = pd.Series(2 * PP - df['low'])  
    S1 = pd.Series(2 * PP - df['high'])  
    R2 = pd.Series(PP + df['high'] - df['low'])  
    S2 = pd.Series(PP - df['high'] + df['low'])  
    R3 = pd.Series(df['high'] + 2 * (PP - df['low']))  
    S3 = pd.Series(df['low'] - 2 * (df['high'] - PP))  
    psr = {'pp':PP, 'r1':R1, 's1':S1, 'r2':R2, 's2':S2, 'r3':R3, 's3':S3}  
    PSR = pd.DataFrame(psr)  
    df = df.join(PSR)  
    
    return df
    


def ROC(df, n,ksgn='close'):  

    '''
    def ROC(df, n,ksgn='close'):  
    變動率(Rate of change,ROC)
　　ROC是由當天的股價與一定的天數之前的某一天股價比較，其變動速度的大小,來反映股票市場變動的快慢程度。
		ROC，也叫做變動速度指標、變動率指標或變化速率指標。
    
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：_{n}，輸出資料
    '''
    xnam='roc_{n}'.format(n=n)
    M = df[ksgn].diff(n - 1)  
    N = df[ksgn].shift(n - 1)  
    ROC = pd.Series(M / N, name = xnam)  
    df = df.join(ROC)  
    return df




def RSI(df, n):
    '''
    def RSI(df, n):  					
      #RSI，相對強弱指標,Relative Strength Index
	也稱相對強弱指數、相對力度指數
	RSI，是通過比較一段時期內的平均收盤漲數和平均收盤跌數來分析市場買沽盤的意向和實力，從而作出未來市場的走勢。
	RSI通過特定時期內股價的變動情況計算市場買賣力量對比，來判斷股票價格內部本質強弱、推測價格未來的變動方向的技術指標。

    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度,一般為14
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：rsi_{n}，輸出資料
    '''
    xnam='rsi_{n}'.format(n=n)
    print( xnam)
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= len(df) - 1:  # df.index[-1]
        #UpMove = df.get_value(i + 1, 'high') - df.get_value(i, 'high')
        #DoMove = df.get_value(i, 'low') - df.get_value(i + 1, 'low')
        UpMove=df['high'].iloc[i+1]-df['high'].iloc[i]
        DoMove=df['low'].iloc[i]-df['low'].iloc[i+1]

        #Range=abs(df['high'].iloc[i+1]-df['low'].iloc[i])-abs(df['low'].iloc[i+1]-df['high'].iloc[i])
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(pd.ewma(UpI, span=n, min_periods=n - 1))
    NegDI = pd.Series(pd.ewma(DoI, span=n, min_periods=n - 1))
    ds = pd.Series(PosDI / (PosDI + NegDI), name=xnam)
    #df = df.join(ds)
    #print('rsi')
    #print(len(ds),len(df))
    ds.index=df.index
    df[xnam]=ds*100
    return df



def RSI100(df, n):

    '''
    def RSI100(df, n):
        zw版RSI相對強弱指數，取0..100之間的數值
    
    
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了2欄：rsi_{n}，輸出資料
          rsi_k，中間輸出資料
    '''    
    xnam='rsi_{n}'.format(n=n)
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= len(df) - 1:  # df.index[-1]
        #UpMove = df.get_value(i + 1, 'high') - df.get_value(i, 'high')
        #DoMove = df.get_value(i, 'low') - df.get_value(i + 1, 'low')
        UpMove=df['high'].iloc[i+1]-df['high'].iloc[i];
        DoMove=df['low'].iloc[i]-df['low'].iloc[i+1];
        
        #Range=abs(df['high'].iloc[i+1]-df['low'].iloc[i])-abs(df['low'].iloc[i+1]-df['high'].iloc[i])
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(pd.ewma(UpI, span=n, min_periods=n - 1))
    NegDI = pd.Series(pd.ewma(DoI, span=n, min_periods=n - 1))
    #ds = pd.Series(PosDI / (PosDI + NegDI))
    ds = pd.Series(PosDI / (PosDI + NegDI))
    ds.index=df.index
    #print(ds.tail())
    #df = df.join(ds)  
    #df[xnam]=ds;
    df['rsi_k']=ds;
    df[xnam]=100-100/(1+df['rsi_k']);
    
    return df
    


def STDDEV(df, n,ksgn='close'):
    '''
    def STDDEV(df, n,ksgn='close'):
    #標準差,#Standard Deviation
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：std_{n}，輸出資料
    '''
    xnam='std_{d}'.format(d=n)
    df = df.join(pd.Series(pd.rolling_std(df[ksgn], n), name =xnam))  
    return df      
    
    

def STOD(df, n,ksgn='close'):    
    '''
    def STO(df, n,ksgn='close'):     
       隨機指標D值,Stochastic oscillator %D  
	隨機指標，又稱KD指標，KDJ指標
　   隨機指標綜合了動量觀念、強弱指標及移動平均線的優點，用來度量股價脫離價格正常範圍的變異程度。
　   KD指標考慮的不僅是收盤價，而且有近期的最高價和最低價，這避免了僅考慮收盤價而忽視真正波動幅度的弱點。
　  隨機指標一般是根據統計學的原理，通過一個特定的週期（常為9日、9周等）內出現過的最高價、最低價
  及最後一個計算週期的收盤價及這三者之間的比例關係，來計算最後一個計算週期的未成熟隨機值RSV，
  然後根據平滑移動平均線的方法來計算K值、D值與J值，並繪成曲線圖來研判股票走勢。
       
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：_{n}，輸出資料
    '''
    #xnam='stod'
    xnam='stod'
    SOk = pd.Series((df[ksgn] - df['low']) / (df['high'] - df['low']), name = 'stok')
    SOd = pd.Series(pd.ewma(SOk, span = n, min_periods = n - 1), name = xnam)
    df = df.join(SOk) 
    df = df.join(SOd) 
    df['stod']=df['stod']*100
    df['stok']=df['stok']*100
    #print('n df',len(df))
    return df


def STOK(df,ksgn='close'):  
    '''
    def STOK(df,ksgn='close'):  
    隨機指標K值,Stochastic oscillator %K
	隨機指標，又稱KD指標，KDJ指標
　   隨機指標綜合了動量觀念、強弱指標及移動平均線的優點，用來度量股價脫離價格正常範圍的變異程度。
　   KD指標考慮的不僅是收盤價，而且有近期的最高價和最低價，這避免了僅考慮收盤價而忽視真正波動幅度的弱點。
　  隨機指標一般是根據統計學的原理，通過一個特定的週期（常為9日、9周等）內出現過的最高價、最低價
  及最後一個計算週期的收盤價及這三者之間的比例關係，來計算最後一個計算週期的未成熟隨機值RSV，
  然後根據平滑移動平均線的方法來計算K值、D值與J值，並繪成曲線圖來研判股票走勢。
    【輸入】
        df, pd.dataframe格式資料來源
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：_{n}，輸出資料
    '''
    xnam='stok'
    SOk = pd.Series((df[ksgn] - df['low']) / (df['high'] - df['low']), name =xnam)  
    df = df.join(SOk)  
    return df



def TRIX(df, n,ksgn='close'): 
    '''
    def TRIX(df, n,ksgn='close'): 
    
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：trix_{n}，輸出資料
    '''
    xnam='trix_{n}'.format(n=n)
    EX1 = pd.ewma(df[ksgn], span=n, min_periods=n - 1)
    EX2 = pd.ewma(EX1, span=n, min_periods=n - 1)
    EX3 = pd.ewma(EX2, span=n, min_periods=n - 1)
    i = 0
    ROC_l = [0]
    while i + 1 <= len(df) - 1:  # df.index[-1]:
        ROC = (EX3[i + 1] - EX3[i]) / EX3[i]
        ROC_l.append(ROC)
        i = i + 1
    trix  = pd.Series(ROC_l, name=xnam)
    #df = df.join(trix)     
    trix.index=df.index;
    df[xnam]=trix
     
    #print(trix.tail())
    #print('n',len(df))
    return df
    


def TSI(df, r, s,ksgn='close'):   
    
    '''
    def TSI(df, r, s,ksgn='close'):   
    TSI，真實強度指數,True Strength Index
  TSI是相對強弱指數 (RSI) 的變體。
  TSI 使用價格動量的雙重平滑指數移動平均線，剔除價格的震盪變化並發現趨勢的變化。
  r一般取25，是一般取13
    【輸入】
        df, pd.dataframe格式資料來源
        r,s，時間長度;  r一般取25，是一般取13
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：tsi，輸出資料
    '''
    xnam='tsi'.format(d=r,d2=s)
    M = pd.Series(df[ksgn].diff(1))  
    aM = abs(M)  
    EMA1 = pd.Series(pd.ewma(M, span = r, min_periods = r - 1))  
    aEMA1 = pd.Series(pd.ewma(aM, span = r, min_periods = r - 1))  
    EMA2 = pd.Series(pd.ewma(EMA1, span = s, min_periods = s - 1))  
    aEMA2 = pd.Series(pd.ewma(aEMA1, span = s, min_periods = s - 1))  
    TSI = pd.Series(EMA2 / aEMA2, name = xnam)  
    df = df.join(TSI)  
    
    return df





#Ultimate Oscillator  
def ULTOSC(df,ksgn='close'):
    '''
    def ULTOSC(df,ksgn='close'):
    UOS，終極指標（Ultimate Oscillator，UOS）
　　終極指標，由拉瑞•威廉（Larry Williams）所創。他認為現行使用的各種振盪指標，對於週期參數的選擇相當敏感。
   不同的市況，不同參數設定的振盪指標，產生的結果截然不同。因此，選擇最佳的參數組含，成為使用振盪指標之前，最重要的一道手續。
　　為了將參數週期調和至最佳狀況，拉瑞•威廉經過不斷測試的結果，先找出三個週期不同的振盪指標，再將這些週期參數，按照反比例的方式，製作成常數因數。
   然後，依照加權的方式，將三個週期不同的振盪指標，分別乘以不同比例的常數，加以綜合製作成UOS指標。
　　經過一連串參數順化的過程後，UOS指標比一般單一參數的振盪指標，更能夠順應各種不同的市況。
    【輸入】
        df, pd.dataframe格式資料來源
        ksgn，列名，一般是：close收盤價
    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：uos，輸出資料
    '''
    i = 0  
    TR_l = [0]  
    BP_l = [0]  
    xnam='uos'
    while i <  len(df) - 1:   #df.index[-1]:  
        #TR = max(df.get_value(i + 1, 'high'), df.get_value(i, 'close')) - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))  
        TR = max(df['high'].iloc[i+1],df[ksgn].iloc[i])-min(df['low'].iloc[i+1],df[ksgn].iloc[i])  
        TR_l.append(TR)  
        #BP = df.get_value(i + 1, 'close') - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))  
        BP =df[ksgn].iloc[i+1]-min(df['low'].iloc[i+1], df[ksgn].iloc[i])  
        BP_l.append(BP)  
        i = i + 1  
    UltO = pd.Series((4 * pd.rolling_sum(pd.Series(BP_l), 7) / pd.rolling_sum(pd.Series(TR_l), 7)) + (2 * pd.rolling_sum(pd.Series(BP_l), 14) / pd.rolling_sum(pd.Series(TR_l), 14)) + (pd.rolling_sum(pd.Series(BP_l), 28) / pd.rolling_sum(pd.Series(TR_l), 28)), name =xnam)  # 'Ultimate_Osc'
    #df = df.join(UltO)      
    UltO.index=df.index;
    df[xnam]=UltO
    return df


def VORTEX(df, n):
    '''
    def VORTEX(df, n):
    螺旋指標,#Vortex Indicator  
    參見 http://www.vortexindicator.com/VFX_VORTEX.PDF


    
    【輸入】
        df, pd.dataframe格式資料來源
        n，時間長度

    【輸出】    
        df, pd.dataframe格式資料來源,
        增加了一欄：vortex__{n}，輸出資料
    '''
    xnam='vortex_{n}'.format(n=n)
    i = 0
    TR = [0]
    while i < len(df) - 1:  # df.index[-1]:
        #Range = max(df.get_value(i + 1, 'high'), df.get_value(i, 'close')) - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))
        Range=max(df['high'].iloc[i+1],df['close'].iloc[i])-min(df['low'].iloc[i+1],df['close'].iloc[i])
        #TR = max(df['High'].iloc[i + 1], df['Close'].iloc[i] - min(df['Low'].iloc[i + 1], df['Close'].iloc[i]))
        TR.append(Range)
        i = i + 1
    i = 0
    VM = [0]
    while i < len(df) - 1:  # df.index[-1]:
        #Range = abs(df.get_value(i + 1, 'high') - df.get_value(i, 'low')) - abs(df.get_value(i + 1, 'low') - df.get_value(i, 'high'))
        Range=abs(df['high'].iloc[i+1]-df['low'].iloc[i])-abs(df['low'].iloc[i+1]-df['high'].iloc[i])
        VM.append(Range)
        i = i + 1
    ds = pd.Series(pd.rolling_sum(pd.Series(VM), n) / pd.rolling_sum(pd.Series(TR), n), name=xnam)
    #df = df.join(ds)  
    ds.index=df.index;
    df[xnam]=ds
    
    return df




    
#=========================================


