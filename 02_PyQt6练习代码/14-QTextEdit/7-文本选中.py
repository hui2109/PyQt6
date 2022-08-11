from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('文本选中的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.te=QTextEdit(self)
        self.te.setGeometry(10,10,300,300)
        self.btn=QPushButton(self)
        self.btn.setText('选中')
        self.btn.setGeometry(160,350,100,30)
        # self.btn.clicked.connect(self.select_position)
        # self.btn.clicked.connect(self.move_position)
        self.btn.clicked.connect(self.select)
    def select_position(self):
        tc=self.te.textCursor()
        # tc.setPosition(7,QTextCursor.MoveMode.KeepAnchor)
        tc.setPosition(7,QTextCursor.MoveMode.MoveAnchor)
        self.te.setTextCursor(tc)
    def move_position(self):
        tc=self.te.textCursor()
        tc.movePosition(QTextCursor.MoveOperation.Left,\
                        QTextCursor.MoveMode.KeepAnchor,2)
        self.te.setTextCursor(tc)
    def select(self):
        tc=self.te.textCursor()
        tc.select(QTextCursor.SelectionType.LineUnderCursor)
        self.te.setTextCursor(tc)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())