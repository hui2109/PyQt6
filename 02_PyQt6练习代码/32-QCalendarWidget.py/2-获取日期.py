from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('获取日期的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.cw=QCalendarWidget(self)

        self.cw.setDateRange(QDate(2012,1,1),QDate(2022,1,1))
        self.cw.setDateEditEnabled(True)

        self.btn=QPushButton('获取日期',self)
        self.btn.move(300,300)
        self.btn.clicked.connect(self.getDate)
    def getDate(self):
        print(self.cw.monthShown())
        print(self.cw.yearShown())
        print(self.cw.selectedDate())

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())