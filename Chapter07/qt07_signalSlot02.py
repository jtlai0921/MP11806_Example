# -*- coding: utf-8 -*-

'''
    【簡介】
    內建訊號/槽訊例

'''

from PyQt5.QtCore import QObject , pyqtSignal

class CustSignal(QObject):
      
    # 宣告一個無參數的訊號
    signal1 = pyqtSignal()
      
    # 宣告帶一個int類型參數的訊號
    signal2 = pyqtSignal(int)
      
    # 宣告帶一個int和str類型參數的訊號
    signal3 = pyqtSignal(int,str)
  
    # 宣告帶一個列表類型參數的訊號
    signal4 = pyqtSignal(list)
  
    # 宣告帶一個字典類型參數的訊號
    signal5 = pyqtSignal(dict)
  
    # 宣告一個多重載版本的訊號，包括一個帶(int, str)類型參數的訊號，或著帶str參數的訊號
    signal6 = pyqtSignal([int,str], [str])
      
    def __init__(self,parent=None):
        super(CustSignal,self).__init__(parent)
  
        # 將訊號連接到指定槽函數
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int,str].connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6OverLoad)
  
        # 發射訊號
        self.signal1.emit()
        self.signal2.emit(1)
        self.signal3.emit(1,"text")
        self.signal4.emit([1,2,3,4])
        self.signal5.emit({"name":"wangwu","age":"25"})
        self.signal6[int,str].emit(1,"text")
        self.signal6[str].emit("text")
          
    def signalCall1(self):
        print("signal1 emit")
  
    def signalCall2(self,val):
        print("signal2 emit,value:",val)
  
    def signalCall3(self,val,text):
        print("signal3 emit,value:",val,text)
  
    def signalCall4(self,val):
        print("signal4 emit,value:",val)
          
    def signalCall5(self,val):
        print("signal5 emit,value:",val)
  
    def signalCall6(self,val,text):
        print("signal6 emit,value:",val,text)
  
    def signalCall6OverLoad(self,val):
        print("signal6 overload emit,value:",val)
  
if __name__ == '__main__':  
    custSignal = CustSignal()
