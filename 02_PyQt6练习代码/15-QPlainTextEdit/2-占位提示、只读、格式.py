from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('占位提示、只读、格式的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        pte=QPlainTextEdit(self)
        pte.setGeometry(10,10,300,300)
        pte.setPlaceholderText('请输入内容')
        pte.setReadOnly(False)
        tcf=QTextCharFormat()
        tcf.setFontFamily('Helvetica')
        tcf.setFontPointSize(20)
        pte.setCurrentCharFormat(tcf)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())