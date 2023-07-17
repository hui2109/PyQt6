from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('掩码设置的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        line1=QLineEdit(self)
        line1.setGeometry(QRect(100,100,200,30))
        line1.setInputMask('%s.999.999.999;0'%'999')

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())