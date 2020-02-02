# -*- coding: utf-8 -*-

"""
    【簡介】
     按鈕傳遞滑鼠按下事件例子


"""

import sys
from PyQt5.QtCore import  QSize
from PyQt5.QtWidgets import QApplication  ,QWidget  , QVBoxLayout, QMessageBox, QToolButton
from PyQt5.QtCore import Qt 

### 自訂窗口類  
class MyWindow( QWidget):
    '''自訂窗口類''' 
    def __init__(self,parent=None):
        '''構造函數'''
        # 調用父類構造函數
        super(MyWindow,self).__init__(parent)
        #設置表單標題
        self.setWindowTitle("按鈕傳遞滑鼠按下事件例子") 
        # 設置視窗固定尺寸
        self.setFixedSize( QSize(820,600))
        # 創建主控制項
        bodyWidget = QWidget(self)
        # 創建主佈局
        mainLayout = QVBoxLayout(bodyWidget)
        # 遍歷創建按鈕
        for i in range(4):
            # 創建自訂按鈕
            button = MyButton(self)
            # 設置文本內容
            button.setText("測試-%s" % i)
            # 添加控制項
            mainLayout.addWidget(button)
            # 設置按鈕點擊連接槽函數
            button.clicked.connect(self.OnClick)
			
    def OnClick(self):
        '''回應點擊'''
        QMessageBox.about(self,"測試","點擊快顯視窗成功")

    def mousePressEvent(self,event):
        '''滑鼠按下事件'''
        # 判斷是否為滑鼠左鍵按下
        if event.button() ==  Qt.LeftButton:
            # 設置視窗背景顏色
            self.setStyleSheet('''background-color:cyan;''')
        
### 自訂按鈕類 
class MyButton( QToolButton):
    '''自訂按鈕類'''
    def __init__(self,parent=None):
        '''構造函數'''
        # 調用父類構造函數
        super(MyButton,self).__init__(parent)
        # 設置按鈕尺寸
        self.setFixedSize( QSize(800,120))
        # 設置按鈕背景顏色
        self.setStyleSheet('''background-color:red;''')

    def mousePressEvent(self,event):
        '''滑鼠按下事件'''
        # 判斷是否為滑鼠左鍵按下
        if event.button() ==  Qt.LeftButton:
            # 發射點擊信號
            self.clicked.emit(True)
            # 傳遞至父視窗回應滑鼠按下事件
            self.parent().mousePressEvent(event)
        
###  主函數 ####
if __name__ == "__main__":
    '''主函數'''
    # 聲明變數
    app =QApplication(sys.argv)
    # 創建窗口
    window = MyWindow()
    # 設置視窗顯示
    window.show()
    #應用程式事件迴圈
    sys.exit(app.exec_())
    
    
