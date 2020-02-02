# -*- coding: utf-8 -*-

"""
    【簡介】
    自動化測試案例


"""

import sys
import unittest
import HTMLTestRunner
import time
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt , QThread  ,  pyqtSignal
import CallMatrixWinUi

# 繼承 QThread 類別
class BackWorkThread(QThread):  
	# 宣告一個訊號，同時返回一個str
	finishSignal = pyqtSignal(str)
	# 建構函數裡增加形參
	def __init__(self, sleepTime,parent=None):
		super(BackWorkThread, self).__init__(parent)
		# 儲存參數
		self.sleepTime = sleepTime

	#重寫run()函數，在裡面定時執行任務。
	def run(self):
		# 休眠一段時間
		time.sleep(self.sleepTime)
		# 休眠結束，傳送一個訊號告訴主執行緒視窗
		self.finishSignal.emit('ok , begin to close Window')
		
class MatrixWinTest(unittest.TestCase):  
    # 初始化工作  
	def setUp(self):  
		print('*** setUp ***')
		self.app = QApplication(sys.argv)	
		self.form = CallMatrixWinUi.CallMatrixWinUi()
		self.form.show()		
		
		# 新建物件，傳入參數。每5秒關閉一個測試案例
		self.bkThread = BackWorkThread(int( 5 ))
		# 連接子處理序的訊號和槽函數
		self.bkThread.finishSignal.connect(self.closeWindow)
		#self.bkThread.finishSignal.connect(self.app.exec_)
		
		# 啟動執行緒，開始執行run()函數的內容
		self.bkThread.start()
		        
	# 退出清理工作
	def tearDown(self):  
		print('*** tearDown ***')
		self.app.exec_()  		
	
	# 設定視窗中所有元件的值為0，狀態為初始狀態。	
	def setFormToZero(self):
		print('* setFormToZero *')  				
		self.form.ui.tequilaScrollBar.setValue(0)
		self.form.ui.tripleSecSpinBox.setValue(0)
		self.form.ui.limeJuiceLineEdit.setText("0.0")
		self.form.ui.iceHorizontalSlider.setValue(0)
		
		self.form.ui.selScrollBarLbl.setText("0")	
		self.form.ui.selIceSliderLbl.setText("0")	
		
	# 關閉視窗
	def closeWindow(self):
		print( '*  關閉視窗')
		self.app.quit()
		
	# 測試用例-在預設狀態下測試GUI	
	def test_defaults(self):
		'''測試GUI處於預設狀態'''
		print('*** testCase test_defaults begin ***')
		self.form.setWindowTitle('開始測試用例 test_defaults ')
				
		self.assertEqual(self.form.ui.tequilaScrollBar.value(), 8)
		self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 4)
		self.assertEqual(self.form.ui.limeJuiceLineEdit.text(), "12.0")
		self.assertEqual(self.form.ui.iceHorizontalSlider.value(), 12)
		self.assertEqual(self.form.ui.speedButtonGroup.checkedButton().text(), "&Karate Chop") 		
		print('*** speedName='+ self.form.getSpeedName() )
	
		# 用滑鼠左鍵按OK		
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		
		# 即使沒有按OK，Class也處於預設狀態
		self.assertEqual(self.form.getJiggers() , 36.0)
		self.assertEqual(self.form.getSpeedName(), "&Karate Chop")
		print('*** testCase test_defaults end ***')		      	
		
	# 測試案例-測試滑動條
	def test_moveScrollBar(self):
		'''測試用例test_moveScrollBar'''	
		print('*** testCase test_moveScrollBar begin ***')
		self.form.setWindowTitle('開始測試用例 test_moveScrollBar ')	
		self.setFormToZero()
		
        # 測試將龍舌蘭酒的滑動條的值設為 12 ，ui中它實際的最大值為 11
		self.form.ui.tequilaScrollBar.setValue( 12 )
		print('* 當執行self.form.ui.tequilaScrollBar.setValue(12) 後，ui.tequilaScrollBar.value() => ' + str( self.form.ui.tequilaScrollBar.value() ) )
		self.assertEqual(self.form.ui.tequilaScrollBar.value(), 11 )
		
        # 測試將龍舌蘭酒的滑動條的值設為 -1 ，ui中它實際的最小值為 0
		self.form.ui.tequilaScrollBar.setValue(-1)
		print('* 當執行self.form.ui.tequilaScrollBar.setValue(-1) 後，ui.tequilaScrollBar.value() => ' + str( self.form.ui.tequilaScrollBar.value() ) )
		self.assertEqual(self.form.ui.tequilaScrollBar.value(), 0)
		
		# 重新將龍舌蘭酒滑動條的值設為 5
		self.form.ui.tequilaScrollBar.setValue(5)
		
        # 用滑鼠左鍵按OK按鈕
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		self.assertEqual(self.form.getJiggers() , 5)
		print('*** testCase test_moveScrollBar end ***')

	# 測試案例-測試計數器控制項
	def test_tripleSecSpinBox(self):
		'''	測試用例 test_tripleSecSpinBox '''	
		print('*** testCase test_tripleSecSpinBox begin ***')
		self.form.setWindowTitle('開始測試用例 test_tripleSecSpinBox ')	
		'''	測試修改spinBox元件的最大最小值
			測試它的最小和最大值作為讀者的練習。
        '''		
		self.setFormToZero()
		# tripleSecSpinBox在介面中的取值範圍為 0 到 11，將其最大值設為 12，看是否顯示正常。
		self.form.ui.tripleSecSpinBox.setValue(12)
		print('* 當執行self.form.ui.tripleSecSpinBox.setValue(12) 後，ui.tripleSecSpinBox.value() => ' + str( self.form.ui.tripleSecSpinBox.value() ) )				
		self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 11 )	

		# tripleSecSpinBox在介面中的取值範圍為 0 到 11，將其最小值設為 -1，看是否顯示正常。
		self.form.ui.tripleSecSpinBox.setValue(-1)
		print('* 當執行self.form.ui.tripleSecSpinBox.setValue(-1) 後，ui.tripleSecSpinBox.value() => ' + str( self.form.ui.tripleSecSpinBox.value() ) )				
		self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 0 )	
		
		self.form.ui.tripleSecSpinBox.setValue(2)

        # 用滑鼠左鍵按OK按鈕
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		self.assertEqual(self.form.getJiggers(), 2)		
		print('*** testCase test_tripleSecSpinBox end ***')

	# 測試案例-測試檸檬汁單列文字框		
	def test_limeJuiceLineEdit(self):
		'''	測試用例 test_limeJuiceLineEdit '''	
		print('*** testCase test_limeJuiceLineEdit begin ***')
		self.form.setWindowTitle('開始測試用例 test_limeJuiceLineEdit ')			
		'''	測試修改juice line edit元件的最大最小值
			測試它的最小和最大值作為讀者的練習。
		'''
		self.setFormToZero()		
        # 清除lineEdit文字方塊，然後鍵入"3.5"
		self.form.ui.limeJuiceLineEdit.clear()		
		QTest.keyClicks(self.form.ui.limeJuiceLineEdit, "3.5")
		
        # 用滑鼠左鍵按OK按鈕
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		self.assertEqual(self.form.getJiggers() , 3.5)
		print('*** testCase test_limeJuiceLineEdit end ***')

	# 測試用例-測試iceHorizontalSlider
	def test_iceHorizontalSlider(self):
		'''	測試用例 test_iceHorizontalSlider '''	
		print('*** testCase test_iceHorizontalSlider begin ***')	
		self.form.setWindowTitle('開始測試案例 test_iceHorizontalSlider ')	
				
		'''	測試ice slider.
			測試它的最小和最大值作為讀者的練習。
		'''
		self.setFormToZero()
		self.form.ui.iceHorizontalSlider.setValue(4)

		# 用滑鼠左鍵按OK按鈕
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		self.assertEqual(self.form.getJiggers(), 4)		
		print('*** testCase test_iceHorizontalSlider end ***')

	# 測試用例- 
	def test_liters(self):
		'''測試用例 test_liters '''		
		print('*** testCase test_liters begin ***')		
		self.form.setWindowTitle('開始測試案例 test_liters ')	
		
		self.setFormToZero()
		self.assertAlmostEqual(self.form.getLiters() , 0.0)
		self.form.ui.iceHorizontalSlider.setValue(1 )
		self.assertAlmostEqual(self.form.getLiters(), 0.0444)
		self.form.ui.iceHorizontalSlider.setValue(2)
		self.assertAlmostEqual(self.form.getLiters(), 0.0444 * 2)
		print('*** testCase test_liters end ***')

	# 測試用例- 		
	def test_blenderSpeedButtons(self):
		print('*** testCase test_blenderSpeedButtons begin ***')		
		'''測試選擇攪拌速度按鈕'''
		self.form.ui.speedButton1.click()
		self.assertEqual(self.form.getSpeedName(), "&Mix")		
		self.form.ui.speedButton2.click()
		self.assertEqual(self.form.getSpeedName(), "&Whip")
		self.form.ui.speedButton3.click()
		self.assertEqual(self.form.getSpeedName(), "&Puree")		
		self.form.ui.speedButton4.click()
		self.assertEqual(self.form.getSpeedName(), "&Chop")
		self.form.ui.speedButton5.click()
		self.assertEqual(self.form.getSpeedName(), "&Karate Chop")		
		self.form.ui.speedButton6.click()
		self.assertEqual(self.form.getSpeedName(), "&Beat")
		self.form.ui.speedButton7.click()
		self.assertEqual(self.form.getSpeedName(), "&Smash")
		self.form.ui.speedButton8.click()
		self.assertEqual(self.form.getSpeedName(), "&Liquefy")
		self.form.ui.speedButton9.click()
		self.assertEqual(self.form.getSpeedName(), "&Vaporize")		
		print('*** testCase test_blenderSpeedButtons end ***')

def runUnitTest1(  ):
	# 預設測試所有的測試用例
	unittest.main() 	

def runUnitTest2(  ):
	# 按照指定順序執行測試用例
	suite = unittest.TestSuite()
	suite.addTest(MatrixWinTest("test_defaults"))
	#suite.addTest(MatrixWinTest("test_moveScrollBar"))
	#suite.addTest(MatrixWinTest("test_tripleSecSpinBox"))
	#suite.addTest(MatrixWinTest("test_limeJuiceLineEdit"))
	#suite.addTest(MatrixWinTest("test_iceHorizontalSlider"))
	#suite.addTest(MatrixWinTest("test_liters"))
	#suite.addTest(MatrixWinTest("test_blenderSpeedButtons"))    	
	runner = unittest.TextTestRunner()
	runner.run(suite)
	
if __name__ == "__main__":  
	#runUnitTest1()
    runUnitTest2()

