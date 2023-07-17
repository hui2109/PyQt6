from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('光标位置的学习')
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
        
        print("是否在段落的结尾:", tc.atBlockEnd())
        print("是否在段落的开始:", tc.atBlockStart())
        print("是否在文档的结尾:", tc.atEnd())
        print("是否在文档的开始:", tc.atStart())

        print("在第几列", tc.columnNumber())
        print("光标位置", tc.position())
        print("在文本块中的位置",tc.positionInBlock())

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())