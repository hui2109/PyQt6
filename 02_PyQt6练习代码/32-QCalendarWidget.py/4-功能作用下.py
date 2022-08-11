from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('功能作用下的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.cw=QCalendarWidget(self)
        self.cw.resize(500,500)

        self.tcf1=QTextCharFormat()
        self.tcf1.setFontPointSize(40)
        self.tcf1.setFontFamily('Songti SC')
        self.tcf2=QTextCharFormat()
        self.tcf2.setForeground(Qt.GlobalColor.green)
        self.tcf2.setFontPointSize(40)
        self.tcf3=QTextCharFormat()
        self.tcf3.setForeground(Qt.GlobalColor.cyan)
        self.tcf3.setFontPointSize(40)


        self.cw.setHeaderTextFormat(self.tcf1)

        self.cw.setHorizontalHeaderFormat(
            # QCalendarWidget.HorizontalHeaderFormat.ShortDayNames
            QCalendarWidget.HorizontalHeaderFormat.SingleLetterDayNames
            )
        self.cw.setVerticalHeaderFormat(
            QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader
            )
        
        self.cw.setWeekdayTextFormat(Qt.DayOfWeek.Tuesday,self.tcf2)
        self.cw.setDateTextFormat(QDate(2020,1,1),self.tcf3)

        self.cw.setSelectedDate(QDate(2020,1,1))
        self.cw.setSelectionMode(QCalendarWidget.SelectionMode.NoSelection)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())