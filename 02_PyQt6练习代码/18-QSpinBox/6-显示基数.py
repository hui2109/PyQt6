from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('显示基数的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        sb=QSpinBox(self)
        sb.setGeometry(100,100,100,100)

        sb.setWrapping(True)

        sb.setDisplayIntegerBase(2)

        te=QTextEdit(self)
        te.setGeometry(100,200,100,100)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())