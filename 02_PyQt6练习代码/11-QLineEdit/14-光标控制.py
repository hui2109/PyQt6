from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('光标控制的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.line1=QLineEdit(self)
        self.line1.setGeometry(10,10,300,30)
        btn=QPushButton(self)
        btn.setText('获取光标')
        btn.move(10,50)
        btn.clicked.connect(self.cao)
    def cao(self):
            # self.line1.cursorBackward(False,2)
            # self.line1.cursorWordBackward(True)
            # self.line1.home(False)
            # self.line1.setCursorPosition(10)
            # print(self.line1.cursorPosition())
            print(self.line1.cursorPositionAt(QPoint(100,1000000)))
            self.line1.setFocus()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())