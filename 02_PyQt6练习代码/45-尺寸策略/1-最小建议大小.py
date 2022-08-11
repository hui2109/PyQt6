from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class Label(QLabel):
    def minimumSizeHint(self):
        return QSize(100, 100)
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('最小建议大小的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label1=Label()
        label1.setStyleSheet('background-color:cyan;')
        label2=QLabel()
        label2.setStyleSheet('background-color:yellow;')
        label3=QLabel()
        label3.setStyleSheet('background-color:blue;')
        label4=QLabel()
        label4.setStyleSheet('background-color:red;')
        label5=QLabel()
        label5.setStyleSheet('background-color:orange;')
        label6=QLabel()
        label6.setStyleSheet('background-color:purple;')
        label7=QLabel()
        label7.setStyleSheet('background-color:green;')
        label8=QLabel()
        label8.setStyleSheet('background-color:grey;')

        layout=QBoxLayout(QBoxLayout.Direction.LeftToRight)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)

        self.setLayout(layout)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())    