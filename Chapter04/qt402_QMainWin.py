# -*- coding: utf-8 -*- 

'''
    【簡介】
	PyQT5中主視窗範例
  
  
'''

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon 
# MainWidget
class MainWindow(QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
        # 設定主視窗標題
		self.setWindowTitle("PyQt QMainWindow範例")
		self.resize(400, 200)
		self.status = self.statusBar()
		self.status.showMessage("這是狀態列提示",10000)


if __name__ == "__main__": 
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("./images/cartoon1.ico"))
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())
