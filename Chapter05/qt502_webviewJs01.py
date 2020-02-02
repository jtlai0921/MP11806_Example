# -*- coding: utf-8 -*- 

'''
    【簡介】
	QWebView中網頁呼叫JavaScript 
  
'''


from PyQt5.QtWidgets  import QApplication , QWidget , QVBoxLayout , QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys


# 建立一個應用程式實例
app = QApplication(sys.argv)  
win = QWidget()
win.setWindowTitle('Web頁面的JavaScript與QWebEngineView互動範例')

# 建立一個垂直佈局器
layout = QVBoxLayout()
win.setLayout(layout)

# 建立一個 QWebEngineView 物件
view = QWebEngineView()
view.setHtml('''
  <html>
    <head>
      <title>A Demo Page</title>

      <script language="javascript">
        // Completes the full-name control and
        // shows the submit button
        function completeAndReturnName() {
          var fname = document.getElementById('fname').value;
          var lname = document.getElementById('lname').value;
          var full = fname + ' ' + lname;

          document.getElementById('fullname').value = full;
          document.getElementById('submit-btn').style.display = 'block';

          return full;
        }
      </script>
    </head>

    <body>
      <form>
        <label for="fname">First name:</label>
        <input type="text" name="fname" id="fname"></input>
        <br />
        <label for="lname">Last name:</label>
        <input type="text" name="lname" id="lname"></input>
        <br />
        <label for="fullname">Full name:</label>
        <input disabled type="text" name="fullname" id="fullname"></input>
        <br />
        <input style="display: none;" type="submit" id="submit-btn"></input>
      </form>
    </body>
  </html>
''')

# 建立一個按鈕，以便呼叫JavaScript腳本
button = QPushButton('設定全名')

def js_callback(result):
    print(result)
    
def complete_name():
   view.page().runJavaScript('completeAndReturnName();', js_callback)

# 按鈕連接'complete_name'槽函數，按一下按鈕時便觸發訊號
button.clicked.connect(complete_name)

# 把QWebEngineView控制項和按鈕控制項載入layout佈局
layout.addWidget(view)
layout.addWidget(button)

# 顯示視窗和執行
win.show()
sys.exit(app.exec_())
