import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle('鼠标跟踪案例')
        self.move(200,200)
        self.resize(500,500)
        self.setMouseTracking(True)

        pixmap=QPixmap('Python3/pyside6布局/PySide6练习代码/04-QWidget/7-鼠标图.png')
        new_pixmap=pixmap.scaled(50,50)
        cursor=QCursor(new_pixmap,0,0)
        self.setCursor(cursor)
        
        self.initWidgets()
    def initWidgets(self):
        self.label=QLabel(self)
        self.label.move(100,100)
        self.label.setText('今天天气真好,我马上就去吃饭了')
        self.label.setStyleSheet('background-color:cyan;')
    def mouseMoveEvent(self, evt):
        # print('鼠标移动了')
        self.label.move(evt.pos().x(),evt.pos().y())

app=QApplication(sys.argv)
window=MyWindow()
window.show()
sys.exit(app.exec())
