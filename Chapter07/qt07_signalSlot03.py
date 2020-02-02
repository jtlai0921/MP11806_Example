# -*- coding: utf-8 -*-

'''
    【簡介】
    訊號/槽N對N連結、斷開連結範例

'''

from PyQt5.QtCore import QObject , pyqtSignal

class SignalClass(QObject):

    # 宣告一個無參數的訊號
	signal1 = pyqtSignal()

    # 宣告帶一個int類型參數的訊號
	signal2 = pyqtSignal(int)

	def __init__(self,parent=None):
		super(SignalClass,self).__init__(parent)

		# 訊號sin1連接到sin1Call和sin2Call這兩個槽
		self.signal1.connect(self.sin1Call)
		self.signal1.connect(self.sin2Call)

		# 訊號sin2連接到訊號sin1
		self.signal2.connect(self.signal1)

        # 發射訊號
		self.signal1.emit()
		self.signal2.emit(1)

		# 斷開sin1、sin2訊號與各槽的連接
		self.signal1.disconnect(self.sin1Call)
		self.signal1.disconnect(self.sin2Call)
		self.signal2.disconnect(self.signal1)

		# 訊號sin1和sin2連接同一個槽sin1Call
		self.signal1.connect(self.sin1Call)
		self.signal2.connect(self.sin1Call)

        # 再次發射訊號
		self.signal1.emit()
		self.signal2.emit(1)

	def sin1Call(self):
		print("signal-1 emit")

	def sin2Call(self):
		print("signal-2 emit")
  
if __name__ == '__main__':  
	signal = SignalClass()
