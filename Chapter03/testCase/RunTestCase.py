# -*- coding: utf-8 -*-

"""
    【簡介】
    自動化測試案例


"""
 
import unittest
import HTMLTestRunner
import time   
from MatrixWinTest import MatrixWinTest
	
if __name__ == "__main__":  
    
	now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))	
	print( now )
	testunit = unittest.TestSuite()
	testunit.addTest(unittest.makeSuite(MatrixWinTest ))
	    
	htmlFile = ".\\"+now+"HTMLtemplate.html"
	print( 'htmlFile='+ htmlFile)
	fp = open(htmlFile,'wb')
	runner = HTMLTestRunner.HTMLTestRunner(
		stream=fp, 
		title=u"PyQt5測試報告", 
		description=u"用例測試情況")
	runner.run(testunit)
	fp.close()

	
