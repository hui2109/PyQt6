from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('功能作用的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        frame=QFrame(self)
        frame.setGeometry(100,100,300,300)
        frame.setStyleSheet('background-color:cyan;')
        frame.setFrameStyle(QFrame.Shape.Box|\
                            QFrame.Shadow.Sunken)
        frame.setLineWidth(20)
        frame.setMidLineWidth(20)
        frame.setFrameRect(QRect(10,10,280,280))
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())