# -*- coding: utf-8 -*-
 
class MyCounter:
    __secretCount = 0  # 私有變數
    publicCount = 0    # 公共變數

    def __privateCountFun(self):
        print('這是私有方法')
        self.__secretCount += 1
        self.publicCount += 1
        #print (self.__secretCount)
        
    def publicCountFun(self):
        print('這是公共方法')
        self.__privateCountFun()

if __name__ == "__main__":
    counter = MyCounter()
    counter.publicCountFun()
    counter.publicCountFun()
    print ('instance publicCount=%d' % counter.publicCount)
    print ('Class publicCount=%d' % MyCounter.publicCount)
    
    # 出錯，實例不能存取私有變數
    # print (counter.__secretCount)  
    # 出錯，實例不能存取私有方法
    # counter.__privateCountFun()
