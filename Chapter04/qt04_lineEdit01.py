# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中 QLineEdit.EchoMode效果範例     
  
'''

from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout
import sys  

class lineEditDemo(QWidget):
	def __init__(self, parent=None):
		super(lineEditDemo, self).__init__(parent)
		self.setWindowTitle("QLineEdit範例")

		flo = QFormLayout()
		pNormalLineEdit = QLineEdit( )
		pNoEchoLineEdit = QLineEdit()
		pPasswordLineEdit = QLineEdit( )
		pPasswordEchoOnEditLineEdit = QLineEdit( )

		flo.addRow("Normal", pNormalLineEdit)
		flo.addRow("NoEcho", pNoEchoLineEdit)
		flo.addRow("Password", pPasswordLineEdit)
		flo.addRow("PasswordEchoOnEdit", pPasswordEchoOnEditLineEdit)
        
		pNormalLineEdit.setPlaceholderText("Normal")
		pNoEchoLineEdit.setPlaceholderText("NoEcho")
		pPasswordLineEdit.setPlaceholderText("Password")
		pPasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

		# 設定顯示效果
		pNormalLineEdit.setEchoMode(QLineEdit.Normal)
		pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
		pPasswordLineEdit.setEchoMode(QLineEdit.Password)
		pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
		                    
		self.setLayout(flo)
                    
   
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = lineEditDemo()	
	win.show()	
	sys.exit(app.exec_())
