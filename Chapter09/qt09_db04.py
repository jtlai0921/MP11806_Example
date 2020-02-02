# -*- coding: utf-8 -*-

'''
    【簡介】
	PyQt5中 處理database範例
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase , QSqlQuery

def createDB():
    # 增加資料庫
	db =  QSqlDatabase.addDatabase('QSQLITE')
	# 設定資料庫名稱
	db.setDatabaseName('./db/database.db')
	# 判斷是否開啟
	if not db.open():
		QMessageBox.critical(None,  ("Cannot open database"),
		("Unable to establish a database connection. \n"
		"This example needs SQLite support. Please read "
		"the Qt SQL driver documentation for information "
		"how to build it.\n\n"
		"Click Cancel to exit."),
		QMessageBox.Cancel)
		return False
		
	# 宣告資料庫查詢物件
	query = QSqlQuery()
	# 建立資料表
	query.exec("create table student(id int primary key, name vchar, sex vchar, age int, deparment vchar)")
	
	#增加記錄
	query.exec("insert into student values(1,'張三1','男',20,'電腦')")
	query.exec("insert into student values(2,'李四1','男',19,'經管')")
	query.exec("insert into student values(3,'王五1','男',22,'機械')")
	query.exec("insert into student values(4,'趙六1','男',21,'法律')")
	query.exec("insert into student values(5,'小明1','男',20,'英語')")
	query.exec("insert into student values(6,'小李1','女',19,'電腦')")
	query.exec("insert into student values(7,'小張1','男',20,'機械')")
	query.exec("insert into student values(8,'小剛1','男',19,'經管')")
	query.exec("insert into student values(9,'張三2','男',21,'電腦')")
	query.exec("insert into student values(10,'張三3','女',20,'法律')")
	query.exec("insert into student values(11,'王五2','男',19,'經管')")
	query.exec("insert into student values(12,'張三4','男',20,'電腦')")
	query.exec("insert into student values(13,'小李2','男',20,'機械')")
	query.exec("insert into student values(14,'李四2','女',19,'經管')")
	query.exec("insert into student values(15,'趙六3','男',21,'英語')")
	query.exec("insert into student values(16,'李四2','男',19,'法律')")
	query.exec("insert into student values(17,'小張2','女',22,'經管')")
	query.exec("insert into student values(18,'李四3','男',21,'英語')")
	query.exec("insert into student values(19,'小李3','女',19,'法律')")
	query.exec("insert into student values(20,'王五3','女',20,'機械')")
	query.exec("insert into student values(21,'張三4','男',22,'電腦')")
	query.exec("insert into student values(22,'小李2','男',20,'法律')")
	query.exec("insert into student values(23,'張三5','男',19,'經管')")
	query.exec("insert into student values(24,'小張3','女',20,'電腦')")
	query.exec("insert into student values(25,'李四4','男',22,'英語')")
	query.exec("insert into student values(26,'趙六2','男',20,'機械')")
	query.exec("insert into student values(27,'小李3','女',19,'英語')")
	query.exec("insert into student values(28,'王五4','男',21,'經管')")
	# 關閉資料庫
	db.close()

	return True

if __name__ == '__main__':
	app =  QApplication(sys.argv)
	createDB() 
	sys.exit(app.exec_())
