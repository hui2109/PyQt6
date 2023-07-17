from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('创建控件的学习')
        self.move(100, 100)
        self.initWidgets()

    def initWidgets(self):
        self.btn=QPushButton(self)
        self.btn.setGeometry(50,50,30,30)

        # self.fd1=QFontDialog(self)

        font=QFont()
        font.setFamilies(['Songti SC'])
        font.setPointSize(34)
        self.fd1=QFontDialog(font,self)

        self.btn.clicked.connect(lambda:self.fd1.open())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
