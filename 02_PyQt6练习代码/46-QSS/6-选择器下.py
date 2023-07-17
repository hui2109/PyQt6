from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from QSSTool import QssTool
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('选择器下的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        box1=QWidget(self)
        box1.setObjectName('box1')
        box2=QWidget(box1)
        btn1=QPushButton('按钮1',box2)
        btn2=QPushButton('按钮2',box1)
        label=QLabel('标签三',box1)
        btn2.move(100,0)
        label.move(200,400)

        cb=QCheckBox('复选框',self)
        cb.move(200,300)
        

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    QssTool.readqssfile('PyQt6布局/PyQt6练习代码/46-QSS/QSS样式表/4-选择器.qss',app)
    sys.exit(app.exec())