# -*- coding: utf-8 -*-
'''
    【簡介】
	PyQT5的第一個簡單範例
   
  
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.move(300, 300)
window.setWindowTitle('hello PyQt5')
window.show()
sys.exit(app.exec_())   
