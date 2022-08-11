from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from login import Ui_Form

class MyWindow(QWidget,Ui_Form):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('的学习')
        self.move(100, 100)

        self.setupUi(self)
        print(self.lineEdit_2.text())


    def initWidgets(self):
        pass
    def check_status(self):
        print(self.lineEdit_2.text())



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
