# -*- coding: utf-8 -*-

# 匯入模組
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtCore import Qt 

### 自訂視窗類別 
class MyWindow( QMainWindow):
    '''自訂視窗類別'''
    ###  建構函數 
    def __init__(self,parent=None):
        '''構造函數'''
        # 呼叫父類別建構函數
        super(MyWindow,self).__init__(parent)

        # 設定視窗標誌（無邊框）
        self.setWindowFlags(Qt.FramelessWindowHint)
  
        # 便於顯示，設定視窗背景顏色(採用QSS)
        self.setStyleSheet('''background-color:blue; ''')

	###  覆寫函數
    def showMaximized(self):
        '''最大化'''
        # 取得桌面控制項
        desktop = QApplication.desktop()
        # 取得螢幕可顯示尺寸
        rect = desktop.availableGeometry()
        # 設定視窗尺寸
        self.setGeometry(rect)
        # 顯示視窗
        self.show()

###  主函數
if __name__ == "__main__":
    '''主函數'''
    # 宣告變數
    app =  QApplication(sys.argv)
    # 建立視窗
    window = MyWindow()
    # 最大化顯示
    window.showMaximized()
    # 進入程式事件迴圈
    sys.exit(app.exec_())
