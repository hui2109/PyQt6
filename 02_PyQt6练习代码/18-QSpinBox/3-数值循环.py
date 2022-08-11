from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('数值循环的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        sb=QSpinBox(self)
        sb.setGeometry(100,100,100,100)
        sb.setRange(18,180)

        sb.setWrapping(True)

        te=QTextEdit(self)
        te.setGeometry(100,200,100,100)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())