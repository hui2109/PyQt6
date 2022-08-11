from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('信号的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.dte = QDateTimeEdit(self)
        self.dte.setGeometry(10, 10, 300, 300)
        self.dte.dateTimeChanged.connect(lambda:print('日期时间改变了'))
        self.dte.dateChanged.connect(lambda:print('日期改变了'))
        self.dte.timeChanged.connect(lambda:print('时间改变了'))

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())