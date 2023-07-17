from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(args,kwargs)
        self.resize(500,500)
        self.setWindowTitle('的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        tb=QToolBox(self)
        print(QToolBox.__subclasses__())
        print(QToolBox.mro())
        print([i for i in dir(QToolBox) if not i.startswith('__')])
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())