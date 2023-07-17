from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('打开对话框的学习')
        self.move(100, 100)
        self.initWidgets()

    def initWidgets(self):
        self.fd=QFontDialog(self)
        self.btn=QPushButton(self)
        self.btn.setGeometry(50,50,150,150)
        self.btn.setText('打开字体对话框')
        # self.btn.clicked.connect(lambda:self.fd.open())
        # self.btn.clicked.connect(lambda:self.fd.open(self.font_cao))
        self.btn.clicked.connect(lambda:print(self.fd.exec()))
        self.font_cao()
    def font_cao(self,*args):
        print(args)
        print(self.fd.selectedFont())
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
