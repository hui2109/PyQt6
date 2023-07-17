from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('创建控件的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.cd=QColorDialog(self)
        # self.cd=QColorDialog(212,self)
        self.cd.open()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())