from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('创建控件的学习')
        self.move(100, 100)
        self.initWidgets()

    def initWidgets(self):
        # self.d=QDialog()
        self.d = QDialog(self)
        # self.d.setModal(True)
        self.d.setWindowModality(Qt.WindowModality.WindowModal)
        # self.d.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.d.exec()
        # self.d.open()
        # self.d.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
