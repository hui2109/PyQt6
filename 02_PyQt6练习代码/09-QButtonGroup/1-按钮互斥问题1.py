from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('按钮互斥问题1的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        wi1= QWidget(self)
        wi1.resize(200,200)
        wi1.setStyleSheet('background-color:red')
        wi2= QWidget(self)
        wi2.resize(200,200)
        wi2.move(200,200)
        wi2.setStyleSheet('background-color:blue')

        btn1=QRadioButton(wi1)
        btn1.setText('男')
        btn1.move(100,50)
        btn2=QRadioButton(wi1)
        btn2.setText('女')
        btn2.move(100,100)

        btn3=QRadioButton(wi2)
        btn3.setText('yes')
        btn3.move(100,50)
        btn4=QRadioButton(wi2)
        btn4.setText('no')
        btn4.move(100,100)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())