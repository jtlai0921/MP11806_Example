# -*- coding: utf-8 -*-


from PyQt5.QtCore import QObject , pyqtSignal

#訊號物件
class QTypeSignal(QObject):
    #定義一個訊號
	sendmsg = pyqtSignal( str,str)
      
	def __init__( self):
		super( QTypeSignal, self).__init__()
            
	def run( self):
        # 發射訊號
		self.sendmsg.emit('第一個參數', '第二個參數')
          
# 槽物件
class QTypeSlot(QObject):
	def __init__( self):
		super( QTypeSlot, self).__init__()
    
    # 槽物件裡的槽函數      
	def get(self, msg1, msg2):
		print("QSlot get msg => " + msg1 + ' ' + msg2)


if __name__ == '__main__':
	send = QTypeSignal()
	slot = QTypeSlot()
   #1 
	print('--- 把訊號連結到槽函數上 ---')    
	send.sendmsg.connect( slot.get)
	send.run()
    
    #2
	print('--- 斷開訊號與槽函數的連結 ---')        
	send.sendmsg.disconnect( slot.get )
	send.run()   

