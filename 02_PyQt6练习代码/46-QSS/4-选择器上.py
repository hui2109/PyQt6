from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from QSSTool import QssTool
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('选择器上的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        btn1=QPushButton('按钮1')
        btn2=QCommandLinkButton('按钮2')
        label1=QLabel('标签1')
        label2=QLabel('标签2')
        fl=QFormLayout()
        fl.addRow(btn1,label1)
        fl.addRow(btn2,label2)
        self.setLayout(fl)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    QssTool.readqssfile('PyQt6布局/PyQt6练习代码/46-QSS/QSS样式表/2-选择器.qss',app)
    sys.exit(app.exec())