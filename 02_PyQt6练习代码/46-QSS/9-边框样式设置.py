from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from QSSTool import QssTool
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('边框样式设置的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label1=QLabel('标签一',self)
        label1.setObjectName('label1')
        label2=QLabel('标签二',self)
        label2.setObjectName('label2')
        label3=QLabel('标签三',self)
        label3.setObjectName('label3')
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        self.setLayout(vbox)
       
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    QssTool.readqssfile('PyQt6布局/PyQt6练习代码/46-QSS/QSS样式表/7-边框样式.qss',app)
    sys.exit(app.exec())