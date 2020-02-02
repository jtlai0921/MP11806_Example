# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QWidget,QMessageBox

class MySharedObject(QWidget):
        
	def __init__( self):
		super( MySharedObject, self).__init__()
		            
	def _getStrValue( self):
        #  
		return '100'        

	def _setStrValue( self,  str ):
        #  
		print('取得頁面參數：%s'% str ) 
		QMessageBox.information(self,"Information", '取得頁面參數：%s'% str )
        
    # 需要定義對外開放的方法
	strValue = pyqtProperty(str, fget=_getStrValue, fset=_setStrValue)     
    
   
    
