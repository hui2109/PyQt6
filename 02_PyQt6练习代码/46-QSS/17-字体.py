from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from QSSTool import QssTool
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('字体的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        te=QTextEdit(self)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    QssTool.readqssfile('PyQt6布局/PyQt6练习代码/46-QSS/QSS样式表/15-字体.qss',app)
    sys.exit(app.exec())