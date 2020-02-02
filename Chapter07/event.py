
import sys
from PyQt5.QtCore import (QEvent, QTimer, Qt)
from PyQt5.QtWidgets import (QApplication, QMenu, QWidget)
from PyQt5.QtGui import QPainter


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.justDoubleClicked = False
        self.key = ""
        self.text = ""
        self.message = ""
        self.resize(400, 300)
        self.move(100, 100)
        self.setWindowTitle("Events")
		# 避免受視窗大小重繪事件的影響，可將參數0改成3000（3秒），然後再執行，就可以明白這行程式碼的意思。
        QTimer.singleShot(0, self.giveHelp)  

    def giveHelp(self):
        self.text = "請點擊這裡觸發滑鼠追蹤功能"
        self.update() # 重繪事件，也就是觸發paintEvent函數。

    '''重新實作關閉事件'''
    def closeEvent(self, event):
        print("Closed")

    '''重新實作快顯功能表事件'''
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        oneAction = menu.addAction("&One")
        twoAction = menu.addAction("&Two")
        oneAction.triggered.connect(self.one)
        twoAction.triggered.connect(self.two)
        if not self.message:
            menu.addSeparator()
            threeAction = menu.addAction("Thre&e")
            threeAction.triggered.connect(self.three)
        menu.exec_(event.globalPos())

    '''快顯功能表的槽函數'''
    def one(self):
        self.message = "Menu option One"
        self.update()

    def two(self):
        self.message = "Menu option Two"
        self.update()

    def three(self):
        self.message = "Menu option Three"
        self.update()

    '''重新實作繪製事件'''
    def paintEvent(self, event):
        text = self.text
        i = text.find("\n\n")
        if i >= 0:
            text = text[0:i]
        if self.key: # 若觸發鍵盤按鍵，則在訊息文字中記錄按鍵資訊
            text += "\n\n您按下了: {0}".format(self.key)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.drawText(self.rect(), Qt.AlignCenter, text) # 繪製訊息文字的內容
        if self.message: # 若訊息文字存在，則在底部置中顯示，5秒後清空並重繪
            painter.drawText(self.rect(), Qt.AlignBottom | Qt.AlignHCenter,
                             self.message)
            QTimer.singleShot(5000, self.clearMessage)
            QTimer.singleShot(5000, self.update)

    '''清空訊息文字的槽函數'''
    def clearMessage(self):
        self.message = ""

    '''重新實作調整視窗大小事件'''
    def resizeEvent(self, event):
        self.text = "調整後的視窗大小為：QSize({0}, {1})".format(
            event.size().width(), event.size().height())
        self.update()

    '''重新實作滑鼠釋放事件'''
    def mouseReleaseEvent(self, event):
        # 若滑鼠為按兩下釋放，則不追蹤滑鼠移動
        # 若滑鼠改為按一下釋放，必須改變追蹤功能的狀態。如果已開啟追蹤功能的話就追蹤，否則便不追蹤
        if self.justDoubleClicked:
            self.justDoubleClicked = False
        else:
            self.setMouseTracking(not self.hasMouseTracking()) # 按一下滑鼠
            if self.hasMouseTracking():
                self.text = "開啟滑鼠追蹤功能。\n" + \
                            "請移動一下滑鼠！\n" + \
                            "按一下滑鼠就可以關閉這個功能"
            else:
                self.text = "關閉滑鼠追蹤功能。\n" + \
                            "按一下滑鼠就可以開啟這個功能"
            self.update()

    '''重新實作滑鼠移動事件'''
    def mouseMoveEvent(self, event):
        if not self.justDoubleClicked:
            globalPos = self.mapToGlobal(event.pos()) # 視窗坐標轉換為螢幕坐標
            self.text = """滑鼠位置：
            視窗坐標為：QPoint({0}, {1}) 
            螢幕坐標為：QPoint({2}, {3}) """.format(event.pos().x(), event.pos().y(), globalPos.x(), globalPos.y())
            self.update()

    '''重新實作按滑鼠兩下事件'''
    def mouseDoubleClickEvent(self, event):
        self.justDoubleClicked = True
        self.text = "您按了兩下滑鼠"
        self.update()

    '''重新實作按下鍵盤事件'''
    def keyPressEvent(self, event):
        self.key = ""
        if event.key() == Qt.Key_Home:
            self.key = "Home"
        elif event.key() == Qt.Key_End:
            self.key = "End"
        elif event.key() == Qt.Key_PageUp:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageUp"
            else:
                self.key = "PageUp"
        elif event.key() == Qt.Key_PageDown:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageDown"
            else:
                self.key = "PageDown"
        elif Qt.Key_A <= event.key() <= Qt.Key_Z:
            if event.modifiers() & Qt.ShiftModifier:
                self.key = "Shift+"
            self.key += event.text()
        if self.key:
            self.key = self.key
            self.update()
        else:
            QWidget.keyPressEvent(self, event)

    # 重新實作其他事件，適用於PyQt沒有提供該事件的處理函數的情況。
	# 由於Tab鍵涉及焦點切換，不會傳遞給keyPressEvent，因此必須在這裡重新定義。
    def event(self, event):
        if (event.type() == QEvent.KeyPress and
                    event.key() == Qt.Key_Tab):
            self.key = "在event()中捕獲Tab鍵"
            self.update()
            return True
        return QWidget.event(self, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()
