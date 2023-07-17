from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('日期时间的学习')
        self.move(100, 100)
        self.initWidgets()

    def initWidgets(self):
        self.dt = QDateTime.currentDateTime()
        self.d = QDate(2023, 12, 31)
        self.dte = QDateTimeEdit(self.d, self)
        self.dte.setGeometry(10, 10, 300, 300)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
