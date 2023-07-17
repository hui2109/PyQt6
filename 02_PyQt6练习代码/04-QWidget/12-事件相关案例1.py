from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500,500)
        self.setWindowTitle('事件案例1的学习')
        self.move(100,100)
class MyLabel(QLabel):
    def __init__(self,parent):
        super().__init__(parent)
        self.resize(200,200)
        self.move(150,150)
        self.setStyleSheet('background-color:cyan;')
    def enterEvent(self,evt):
        self.setText('欢迎光临')
        self.setContentsMargins(75,75,0,75)
    def leaveEvent(self,evt):
        self.setContentsMargins(75,75,0,75)
        print(self.contentsRect())
        self.setText('谢谢惠顾')   

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    label=MyLabel(window)
    window.show()
    sys.exit(app.exec())