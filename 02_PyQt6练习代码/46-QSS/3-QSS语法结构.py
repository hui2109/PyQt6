from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from QSSTool import QssTool
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('QSS语法结构的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        w1=QWidget()
        label1=QLabel('我是一个标签-1',w1)
        label1.setObjectName('l1')
        btn1=QPushButton('我是一个按钮-1',w1)
        btn1.setGeometry(50,50,200,50)

        w2=QWidget()        
        label2=QLabel('我是一个标签-2',w2)
        btn2=QPushButton('我是一个按钮-2',w2)
        btn2.setGeometry(50,50,200,50)
        btn2.setObjectName('btn2')

        vbox=QVBoxLayout()
        vbox.addWidget(w1)
        vbox.addWidget(w2)

        self.setLayout(vbox)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    QssTool.readqssfile('PyQt6布局/PyQt6练习代码/46-QSS/QSS样式表/1-test1.qss',app)
    sys.exit(app.exec())