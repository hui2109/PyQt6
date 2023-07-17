from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('输入限制的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        le1=QLineEdit(self)
        le1.setGeometry(50,50,200,30)
        le2=QLineEdit(self)
        le2.setGeometry(50,100,200,30)
        le1.setMaxLength(3)
        print(le1.maxLength())

        le2.setReadOnly(True)
        le2.setText('123')
        print(le2.isReadOnly())
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())