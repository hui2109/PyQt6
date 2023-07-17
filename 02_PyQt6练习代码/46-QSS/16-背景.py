from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from QSSTool import QssTool
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(800,800)
        self.setWindowTitle('背景的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label=QLabel('标签一',self)
        label.setGeometry(0,0,700,700)
        te=QTextEdit('文本编辑器',self)
        te.setGeometry(900,100,500,500)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    QssTool.readqssfile('PyQt6布局/PyQt6练习代码/46-QSS/QSS样式表/14-背景.qss',app)
    sys.exit(app.exec())