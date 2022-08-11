from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('获取信息的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        bl=QBoxLayout(QBoxLayout.Direction.TopToBottom)
        gl=QGridLayout()

        label1=QLabel()
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

        bl.addWidget(label5)
        bl.addWidget(label6)
        bl.addWidget(label7)
        bl.addWidget(label8)

        gl.addWidget(label1,0,0)
        gl.addWidget(label2,0,1)
        gl.addWidget(label3,1,0,2,2)
        gl.addWidget(label4,0,2,3,1)
        gl.addLayout(bl,3,0,1,3)

        print(gl.columnCount())
        print(gl.rowCount())
        

        self.setLayout(gl)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()

    gl=window.layout()
    print(gl.cellRect(0,0))

    sys.exit(app.exec())    