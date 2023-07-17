from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('设置显示数值的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        lcd=QLCDNumber(15,self)
        # lcd.display('abcdef')
        # lcd.display(908)
        lcd.display(908.88)
        lcd.setGeometry(100,100,300,300)
        lcd.setDigitCount(6)
        lcd.setHexMode()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())