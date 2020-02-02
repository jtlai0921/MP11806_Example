# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中處理database範例
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase , QSqlQuery

def createDB():
	db = QSqlDatabase.addDatabase('QSQLITE')
	db.setDatabaseName('./db/database.db')
    
	if not db.open():
		QMessageBox.critical(None,  ("無法開啟資料庫"),
		( "無法建立資料庫的連線，本例需要SQLite支援，請檢查資料庫設定。\n\n"
          "點擊取消鈕退出程式。"),
			QMessageBox.Cancel )
		return False
	
	query = QSqlQuery()
	query.exec_("create table people(id int primary key, "
	"name varchar(20), address varchar(30))")
	query.exec_("insert into people values(1, 'zhangsan1', 'BeiJing')")
	query.exec_("insert into people values(2, 'lisi1', 'TianJing')")
	query.exec_("insert into people values(3, 'wangwu1', 'HenNan')")
	query.exec_("insert into people values(4, 'lisi2', 'HeBei')")
	query.exec_("insert into people values(5, 'wangwu2', 'shanghai')")
	return True

if __name__ == '__main__':
	app =  QApplication(sys.argv)
	createDB() 
	sys.exit(app.exec_())
		
