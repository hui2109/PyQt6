from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('获取日期时间的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.dt=QDateTime.currentDateTime()
        self.dte=QDateTimeEdit(self.dt,self)
        self.dte.setGeometry(10,10,300,300)
        self.dte.setDateTimeRange(QDateTime.currentDateTime().\
            addDays(-3), QDateTime.currentDateTime().addDays(3))
        self.dte.setCalendarPopup(True)
        
        print(self.dte.dateTime())
        print(self.dte.sectionText(QDateTimeEdit.Section.DaySection))


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())