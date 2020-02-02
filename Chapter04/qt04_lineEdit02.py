# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中 QLineEdit的驗證器範例     
  
'''

from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout
from PyQt5.QtGui import QIntValidator ,QDoubleValidator  , QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys  

class lineEditDemo(QWidget):
	def __init__(self, parent=None):
		super(lineEditDemo, self).__init__(parent)
		self.setWindowTitle("QLineEdit範例")

		flo = QFormLayout()
		pIntLineEdit  = QLineEdit( )
		pDoubleLineEdit  = QLineEdit()
		pValidatorLineEdit  = QLineEdit( )

		flo.addRow("整數", pIntLineEdit)
		flo.addRow("浮點數", pDoubleLineEdit)
		flo.addRow("字母和數字", pValidatorLineEdit)
        
		pIntLineEdit.setPlaceholderText("整數");
		pDoubleLineEdit.setPlaceholderText("浮點數");
		pValidatorLineEdit.setPlaceholderText("字母和數字");

		# 整數，範圍：[1, 99]
		pIntValidator = QIntValidator(self)
		pIntValidator.setRange(1, 99)

		# 浮點數，範圍：[-360, 360]，精度：小數點後兩位
		pDoubleValidator = QDoubleValidator(self)
		pDoubleValidator.setRange(-360, 360)
		pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
		pDoubleValidator.setDecimals(2)
		
		# 字母和數字
		reg = QRegExp("[a-zA-Z0-9]+$")
		pValidator = QRegExpValidator(self)
		pValidator.setRegExp(reg)	

        # 設定驗證器
		pIntLineEdit.setValidator(pIntValidator)
		pDoubleLineEdit.setValidator(pDoubleValidator)
		pValidatorLineEdit.setValidator(pValidator)
		                    
		self.setLayout(flo)                        
   
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = lineEditDemo()	
	win.show()	
	sys.exit(app.exec_())
