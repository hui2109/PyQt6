from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500,500)
        self.setWindowTitle('QWidget的学习')
        self.move(300,300)
        self.initWidgets()
    def initWidgets(self):
        self.inherit()
    
    def inherit(self):
        #可以通过两种方式获取一个类的父类
        #mro是类方法，只能由类调用，打印直接和间接父类
        print(QWidget.mro())
        #------------------------------------------------
        #__bases__是类属性，只能由类调用，打印直接父类
        print(QWidget.__bases__)
        
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec())