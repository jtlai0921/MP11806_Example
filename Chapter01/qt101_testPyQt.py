import sys 	
from PyQt5 import QtWidgets 

'''
    【簡介】
	第一個PyQt例子
   
    
'''

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("hello, pyqt5")
widget.show()
sys.exit(app.exec_())
