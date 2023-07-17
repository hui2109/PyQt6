from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('QSS初体验的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        w1=QWidget()
        w2=QWidget()

        label1=QLabel('我是一个标签',w1)
        btn1=QPushButton('我是一个按钮',w1)
        btn1.setGeometry(50,50,100,50)
        label2=QLabel('我是一个标签',w2)
        btn2=QPushButton('我是一个按钮',w2)
        btn2.setGeometry(50,50,100,50)
        self.btn3=QPushButton('我是一个按钮')
        self.btn3.setGeometry(50,50,100,50)
        self.btn3.show()

        vbox=QVBoxLayout()
        vbox.addWidget(w1)
        vbox.addWidget(w2)

        # w1.setStyleSheet('QPushButton {background-color:cyan;}')
        # w2.setStyleSheet('background-color:yellow;')

        self.setLayout(vbox)

        # self.setStyleSheet('QPushButton {background-color:cyan;}')

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()

    app.setStyleSheet('QPushButton {background-color:cyan;}')

    sys.exit(app.exec())