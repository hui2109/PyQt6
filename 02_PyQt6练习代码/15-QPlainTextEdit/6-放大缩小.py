from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('放大缩小的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.pte=QPlainTextEdit(self)
        self.pte.setGeometry(10,10,300,300)
        self.btn=QPushButton('测试按钮',self)
        self.btn.setGeometry(10,320,100,30)
        self.btn.clicked.connect(self.btnClicked)
    def btnClicked(self):
        # self.pte.zoomIn(-5)
        self.pte.zoomOut(-5)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())