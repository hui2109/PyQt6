from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from QSSTool import QssTool
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('伪状态下的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        checkbox=QCheckBox('选择我',self)
        checkbox.setGeometry(50,50,100,100)
        checkbox.setTristate(True)
        pushbutton=QPushButton('按下我',self)
        pushbutton.setGeometry(300,50,100,100)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    QssTool.readqssfile('PyQt6布局/PyQt6练习代码/46-QSS/QSS样式表/6-伪状态下.qss',app)
    sys.exit(app.exec())