from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('开始和结束编辑标识的学习')
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
        tc=self.te.textCursor()
        # tc.insertText("我是文本框的内容\n")
        # tc.insertText("xxx\n")
        # tc.insertText("aaa\n")
        # tc.insertText("bbb\n")

        # tc.insertText("我是文本框的内容")
        # tc.insertBlock()
        # tc.insertText("xxx")
        # tc.insertBlock()
        # tc.insertText("aaa")
        # tc.insertBlock()
        # tc.insertText("bbb")

        tc.beginEditBlock()
        tc.insertText("我是文本框的内容")
        tc.insertBlock()
        tc.insertText("xxx")
        tc.insertBlock()
        tc.insertText("aaa")
        tc.endEditBlock()
        tc.insertBlock()
        tc.insertText("bbb")

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())