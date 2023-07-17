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
        self.cw=QCalendarWidget(self)
        self.cw.resize(500,500)
        
        # self.cw.activated.connect(lambda val:print(val))
        # self.cw.clicked.connect(lambda val:print(val))
        # self.cw.currentPageChanged.connect(lambda val1,val2:print(val1,val2))
        self.cw.selectionChanged.connect(lambda :print('选中值改变了',
                self.cw.selectedDate()))
        
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())