from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('分段样式的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        lcd1=QLCDNumber(self)
        lcd2=QLCDNumber(self)
        lcd3=QLCDNumber(self)

        lcd1.setGeometry(50,50,100,100)
        lcd2.setGeometry(50,200,100,100)        
        lcd3.setGeometry(50,350,100,100)

        lcd1.display(999)        
        lcd2.display(999)        
        lcd3.display(999)

        lcd1.setSegmentStyle(QLCDNumber.SegmentStyle.Outline)        
        lcd2.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)        
        lcd3.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)        

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())