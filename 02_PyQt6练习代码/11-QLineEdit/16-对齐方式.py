from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('对齐方式的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        line1=QLineEdit(self)
        line1.setGeometry(10,10,300,300)
        line1.setTextMargins(100,100,0,0)
        line1.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())