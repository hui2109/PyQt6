from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('溢出的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        lcd=QLCDNumber(self)
        lcd.setDigitCount(4)
        print(lcd.checkOverflow(90.888888))
        
        lcd.setGeometry(100,100,300,300)
        lcd.overflow.connect(lambda:print('数据溢出了'))
        lcd.display('adsfghjfdasf')

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())