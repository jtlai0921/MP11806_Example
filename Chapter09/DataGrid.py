# -*- coding: utf-8 -*- 

import sys
import re
from PyQt5.QtWidgets import (QWidget , QHBoxLayout , QVBoxLayout , QApplication, QPushButton, QLineEdit ,QLabel , QSplitter ,  QTableView , QHeaderView , QMessageBox )
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase  , QSqlQueryModel , QSqlQuery

def createTableAndInit():
	# 新建資料庫
	db =  QSqlDatabase.addDatabase('QSQLITE')
	# 設定資料庫名稱
	db.setDatabaseName('./db/database.db')
	# 判斷是否開啟
	if not db.open():			
		return False

	# 宣告資料庫查詢物件
	query = QSqlQuery()

	# 建立資料表
	query.exec("create table student(id int primary key, name vchar, sex vchar, age int, deparment vchar)")
	
	# 插入記錄
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
	
	db.close()
	return True		
           		
class DataGrid(QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("分頁查詢範例")
		self.resize(750,300)
		
		# 查詢模型		
		self.queryModel = None
		# 資料表
		self.tableView = None		
		# 總頁數標籤
		self.totalPageLabel = None
		# 目前頁標籤
		self.currentPageLabel = None
		# 轉到頁輸入框		
		self.switchPageLineEdit = None
		# 前一頁按鈕
		self.prevButton = None		
		# 後一頁按鈕
		self.nextButton = None
		# 轉到頁按鈕
		self.switchPageButton = None	
		# 目前頁	
		self.currentPage = 0
		# 總頁數
		self.totalPage = 0		
		# 總記錄數
		self.totalRecrodCount = 0
		# 每頁顯示記錄數
		self.PageRecordCount  = 5			

		self.db = None
		self.initUI()

	def initUI(self):
		# 建立視窗
		self.createWindow()
		# 設定表格
		self.setTableView()
		
		# 訊號/槽連接
		self.prevButton.clicked.connect(self.onPrevButtonClick )		
		self.nextButton.clicked.connect(self.onNextButtonClick )	
		self.switchPageButton.clicked.connect(self.onSwitchPageButtonClick )	

	def closeEvent(self, event):
		# 關閉資料庫
		self.db.close()

	
    # 建立視窗	
	def createWindow(self):
		# 操作佈局
		operatorLayout = QHBoxLayout()
		self.prevButton = QPushButton("前一頁")
		self.nextButton = QPushButton("後一頁")
		self.switchPageButton = QPushButton("Go")
		self.switchPageLineEdit = QLineEdit()
		self.switchPageLineEdit.setFixedWidth(40)	
		
		switchPage =  QLabel("轉到第")
		page = QLabel("頁")
		operatorLayout.addWidget(self.prevButton)
		operatorLayout.addWidget(self.nextButton)
		operatorLayout.addWidget(switchPage)
		operatorLayout.addWidget(self.switchPageLineEdit)
		operatorLayout.addWidget(page)
		operatorLayout.addWidget(self.switchPageButton)
		operatorLayout.addWidget( QSplitter())
	
	    # 狀態佈局
		statusLayout =  QHBoxLayout()
		self.totalPageLabel =  QLabel()
		self.totalPageLabel.setFixedWidth(70)
		self.currentPageLabel =  QLabel()
		self.currentPageLabel.setFixedWidth(70)
		
		self.totalRecordLabel =  QLabel()
		self.totalRecordLabel.setFixedWidth(70)
		
		statusLayout.addWidget(self.totalPageLabel)
		statusLayout.addWidget(self.currentPageLabel)
		statusLayout.addWidget( QSplitter() )	
		statusLayout.addWidget(self.totalRecordLabel)
		
		# 設定表格屬性
		self.tableView = QTableView()
		# 表格寬度的自我調整
		self.tableView.horizontalHeader().setStretchLastSection(True)
		self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		
		# 建立介面
		mainLayout =  QVBoxLayout(self);
		mainLayout.addLayout(operatorLayout);
		mainLayout.addWidget(self.tableView);
		mainLayout.addLayout(statusLayout);
		self.setLayout(mainLayout)

	# 設定表格	
	def setTableView(self):	
		print('*** step2 SetTableView'  )
		self.db =  QSqlDatabase.addDatabase('QSQLITE')
		# 設定資料庫名稱
		self.db.setDatabaseName('./db/database.db')
		# 開啟資料庫
		self.db.open() 
	
		# 宣告查詢模型
		self.queryModel = QSqlQueryModel(self)
		# 設定目前頁
		self.currentPage = 1;
		# 取得總記錄數
		self.totalRecrodCount = self.getTotalRecordCount()
		# 取得總頁數
		self.totalPage = self.getPageCount()
		# 刷新狀態
		self.updateStatus()
		# 設定總頁數標籤
		self.setTotalPageLabel()
		# 設定總記錄數標籤
		self.setTotalRecordLabel()
		
		# 記錄查詢
		self.recordQuery(0)
		# 設定模型
		self.tableView.setModel(self.queryModel)
		
		print('totalRecrodCount=' + str(self.totalRecrodCount) )		
		print('totalPage=' + str(self.totalPage) )
             		
		# 設定表頭
		self.queryModel.setHeaderData(0,Qt.Horizontal,"編號") 
		self.queryModel.setHeaderData(1,Qt.Horizontal,"姓名")
		self.queryModel.setHeaderData(2,Qt.Horizontal,"性別")
		self.queryModel.setHeaderData(3,Qt.Horizontal,"年齡")
		self.queryModel.setHeaderData(4,Qt.Horizontal,"院系")

	# 取得記錄數	
	def getTotalRecordCount(self):			
		self.queryModel.setQuery("select * from student")
		rowCount = self.queryModel.rowCount()
		print('rowCount=' + str(rowCount) )
		return rowCount
			
	# 取得頁數		
	def getPageCount(self):			
		if  self.totalRecrodCount % self.PageRecordCount == 0  :
			return (self.totalRecrodCount / self.PageRecordCount )
		else :
			return (self.totalRecrodCount / self.PageRecordCount + 1)

	# 記錄查詢		
	def recordQuery(self, limitIndex ):	
		szQuery = ("select * from student limit %d,%d" % (  limitIndex , self.PageRecordCount ) )
		print('query sql=' + szQuery )
		self.queryModel.setQuery(szQuery)
		
	# 刷新狀態		
	def updateStatus(self):				
		szCurrentText = ("目前第%d頁" % self.currentPage )
		self.currentPageLabel.setText( szCurrentText )
        
		#設定按鈕是否可用
		if self.currentPage == 1 :
			self.prevButton.setEnabled( False )
			self.nextButton.setEnabled( True )
		elif  self.currentPage == self.totalPage :
			self.prevButton.setEnabled( True )
			self.nextButton.setEnabled( False )
		else :
			self.prevButton.setEnabled( True )
			self.nextButton.setEnabled( True )

	# 設定總數頁
	def setTotalPageLabel(self):	
		szPageCountText  = ("總共%d頁" % self.totalPage )
		self.totalPageLabel.setText(szPageCountText)

	# 設定總記錄數
	def setTotalRecordLabel(self):	
		szTotalRecordText  = ("共%d筆" % self.totalRecrodCount )
		print('*** setTotalRecordLabel szTotalRecordText=' + szTotalRecordText )
		self.totalRecordLabel.setText(szTotalRecordText)
		
	# 按下前一頁按鈕
	def onPrevButtonClick(self):	
		print('*** onPrevButtonClick ');
		limitIndex = (self.currentPage - 2) * self.PageRecordCount
		self.recordQuery( limitIndex) 
		self.currentPage -= 1 
		self.updateStatus() 

	# 按下後一頁按鈕
	def onNextButtonClick(self):
		print('*** onNextButtonClick ');
		limitIndex =  self.currentPage * self.PageRecordCount
		self.recordQuery( limitIndex) 
		self.currentPage += 1
		self.updateStatus() 
		
	# 按下轉到頁按鈕
	def onSwitchPageButtonClick(self):			
		# 取得輸入字串
		szText = self.switchPageLineEdit.text()
		# 數字規則運算式		
		pattern = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
		match = pattern.match(szText)
		
		# 判斷是否為數字
		if not match :
			QMessageBox.information(self, "提示", "請輸入數字" )
			return
			
		# 是否為空
		if szText == '' :
			QMessageBox.information(self, "提示" , "請輸入跳越頁數" )
			return

		# 取得頁數
		pageIndex = int(szText)
		# 判斷是否有指定頁
		if pageIndex > self.totalPage or pageIndex < 1 :
			QMessageBox.information(self, "提示", "沒有指定的頁數，請重新輸入" )
			return
			
		# 取得查詢起始列號
		limitIndex = (pageIndex-1) * self.PageRecordCount			
			
		# 記錄查詢
		self.recordQuery(limitIndex);
		# 設定目前頁
		self.currentPage = pageIndex
		# 刷新狀態
		self.updateStatus();
			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	if createTableAndInit():    		
		# 建立視窗
		example = DataGrid() 
		# 顯示視窗
		example.show()   
	
	sys.exit(app.exec_())
