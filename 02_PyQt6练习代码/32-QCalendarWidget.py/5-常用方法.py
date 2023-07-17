from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('常用方法的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.cw=QCalendarWidget(self)
        self.cw.resize(500,500)
        self.btn=QPushButton('点击',self)
        self.btn.move(100,500)
        self.btn.clicked.connect(self.btnClicked)
    def btnClicked(self):
        # self.cw.showToday()
        self.cw.showSelectedDate()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())