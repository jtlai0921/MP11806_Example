# -*- coding: utf-8 -*- 
'''
    【簡介】
	儲存PyQt5類別的說明文字到硬碟
   
    
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage 
from PyQt5.QtWidgets import QWidget

out = sys.stdout
sys.stdout = open(r'C:\QWidget.txt' , 'w')
help( QWidget  )
sys.stdout.close()
sys.stdout = out
