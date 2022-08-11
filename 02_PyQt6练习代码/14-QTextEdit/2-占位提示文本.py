from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('占位提示文本的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        te1=QTextEdit(self)
        te1.setGeometry(50,50,400,400)
        self.te1=te1
        self.te1.setPlaceholderText('请输入您的姓名')

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())