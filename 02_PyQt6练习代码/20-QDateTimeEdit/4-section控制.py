from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('section控制的学习')
        self.move(100, 100)
        self.initWidgets()

    def initWidgets(self):
        self.dt = QDateTime.currentDateTime()
        self.dte = QDateTimeEdit(self.dt, self)
        self.dte.setGeometry(10, 10, 300, 300)

        print(self.dte.sectionCount())
        print(self.dte.currentSectionIndex())

        self.dte.setCurrentSectionIndex(2)
        self.dte.setCurrentSection(QDateTimeEdit.Section.DaySection)
        print(self.dte.currentSection())

        print(self.dte.sectionText(QDateTimeEdit.Section.DaySection))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
