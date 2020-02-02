# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import *
from MatrixWinUi import *

class CallMatrixWinUi(QWidget ):
	def __init__(self, parent=None):    
		super(CallMatrixWinUi, self).__init__(parent)
		self.ui = Ui_MatrixWin()
		self.ui.setupUi(self)
		self.initUi()
		
	# 初始化視窗	
	def initUi(self):
		scrollVal = self.ui.tequilaScrollBar.value()	
		self.ui.selScrollBarLbl.setText( str(scrollVal) )	
		sliderVal = self.ui.iceHorizontalSlider.value()
		self.ui.selIceSliderLbl.setText( str(sliderVal) )		
		
	# 取得一量杯酒的重量，單位：克
	def getJiggers(self):
		# 返回瑪格麗特雞尾酒的總容量，以jigger量酒器為單位
		# 一個量酒器可以容納0.0444升的酒
		jiggersTequila = self.ui.tequilaScrollBar.value()
		jiggersTripleSec = self.ui.tripleSecSpinBox.value()
		jiggersLimeJuice = float(self.ui.limeJuiceLineEdit.text())
		jiggersIce = self.ui.iceHorizontalSlider.value()
		return jiggersTequila + jiggersTripleSec + jiggersLimeJuice + jiggersIce

	# 取得一量杯酒的體積，單位：升
	def getLiters(self):
		'''返回鸡尾酒的总容量(升)'''
		return 0.0444 * self.getJiggers()

	# 取得攪拌速度
	def getSpeedName(self):
		speedButton = self.ui.speedButtonGroup.checkedButton()
		if speedButton is None:
			return None
		return speedButton.text()

	# 點擊ok鈕後，將回應的結果顯示在resultText文字框裡	
	def uiAccept(self):
		print('* CallMatrixWinUi accept ')
		print('The volume of drinks is {0} liters ({1} jiggers).'.format(self.getLiters() , self.getJiggers() ))
		print('The blender is running at speed "{0}"'.format(self.getSpeedName() ))
		msg1 = '飲料量為： {0} 升 ({1} 個量酒器)。'.format(self.getLiters() , self.getJiggers() )
		msg2 = '調酒器的攪拌速度是： "{0}"。'.format(self.getSpeedName() )
		self.ui.resultText.clear()	
		self.ui.resultText.append(msg1)
		self.ui.resultText.append(msg2)
				      
	# 點擊cancel按鈕，關閉視窗	
	def uiReject(self):
		print('* CallMatrixWinUi reject ')
		'''Cancel.'''
		self.close()

	# 點擊clear按鈕，清空操作結果			
	def uiClear(self):
		print('* CallMatrixWinUi uiClear ')
		self.ui.resultText.clear()		

	def uiScrollBarValueChanged(self):
		print('* uiScrollBarValueChanged ---------')
		pos = self.ui.tequilaScrollBar.value()	
		self.ui.selScrollBarLbl.setText( str(pos) )		
		
	def uiIceSliderValueChanged( self):
		print('* uiIceSliderValueChanged ---------')
		pos = self.ui.iceHorizontalSlider.value()
		self.ui.selIceSliderLbl.setText( str(pos) )
		          		
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	demo = CallMatrixWinUi()  
	demo.show()  
	sys.exit(app.exec_())  
