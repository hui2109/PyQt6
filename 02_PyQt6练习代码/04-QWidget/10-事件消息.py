from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('事件消息的学习')
        self.resize(500,500)
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        pass
    def showEvent(self,evt):
        print('窗口被展示了')
    def closeEvent(self,evt):
        print('窗口被关闭了')
    def moveEvent(self,evt):
        print('窗口被移动了')
    def resizeEvent(self,evt):
        print('窗口调整了大小')
    def keyPressEvent(self, evt):
        print('按键按下了')
    def keyReleaseEvent(self, evt):
        print('按键松开了')
    def focusInEvent(self, evt):
        print('获得了焦点')
    def focusOutEvent(self, evt):
        print('失去了焦点')
    def enterEvent(self, evt):
        print('鼠标进入')
    def leaveEvent(self, evt):
        print('鼠标离开了')
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec())
