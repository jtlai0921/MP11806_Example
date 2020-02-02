# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中 QLineEdit的輸入遮罩範例     
  
'''

from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout
import sys  

class lineEditDemo(QWidget):
	def __init__(self, parent=None):
		super(lineEditDemo, self).__init__(parent)
		self.setWindowTitle("QLineEdit的輸入遮罩範例")

		flo = QFormLayout()          		
		pIPLineEdit = QLineEdit()
		pMACLineEdit = QLineEdit()
		pDateLineEdit = QLineEdit()
		pLicenseLineEdit = QLineEdit()		

		pIPLineEdit.setInputMask("000.000.000.000;_")
		pMACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
		pDateLineEdit.setInputMask("0000-00-00")
		pLicenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

		flo.addRow("數字遮罩", pIPLineEdit)
		flo.addRow("Mac遮罩", pMACLineEdit)
		flo.addRow("日期遮罩", pDateLineEdit)
		flo.addRow("許可證遮罩", pLicenseLineEdit)
        
		#pIPLineEdit.setPlaceholderText("111")
		#pMACLineEdit.setPlaceholderText("222")
		#pLicenseLineEdit.setPlaceholderText("333")
		#pLicenseLineEdit.setPlaceholderText("444")
		      		                    
		self.setLayout(flo)                        
   
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = lineEditDemo()	
	win.show()	
	sys.exit(app.exec_())
