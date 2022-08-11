from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(600,600)
        self.setWindowTitle('对齐和缩进的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.label=QLabel('马上去吃饭了',self)
        self.label.setGeometry(100,100,400,400)
        self.label.setStyleSheet("background-color: cyan;")

        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)
        self.label.setIndent(50)
        self.label.setMargin(50)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())