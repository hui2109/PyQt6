from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('软换行模式的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.te=QTextEdit(self)
        self.te.setGeometry(10,10,300,300)
        self.btn=QPushButton(self)
        self.btn.setText('选中')
        self.btn.setGeometry(160,350,100,30)
        self.btn.clicked.connect(self.select)
    def select(self):
        # self.te.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.te.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)

        # self.te.setLineWrapMode(QTextEdit.LineWrapMode.FixedPixelWidth)
        # self.te.setLineWrapColumnOrWidth(100)

        # self.te.setLineWrapMode(QTextEdit.LineWrapMode.FixedColumnWidth)
        # self.te.setLineWrapColumnOrWidth(9)

        # self.te.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)
        self.te.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())