from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('信号的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.te=QTextEdit(self)
        self.te.setGeometry(10,10,300,300)
        self.te.textChanged.connect(self.textChanged)
        self.te.selectionChanged.connect(self.selectionChanged)
        self.te.copyAvailable.connect(self.copyAvailable)
    def textChanged(self):
        print('文本内容发生了改变')
    def selectionChanged(self):
        print('选中的内容发生了改变')
    def copyAvailable(self):
        print('当前复制可用')

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())