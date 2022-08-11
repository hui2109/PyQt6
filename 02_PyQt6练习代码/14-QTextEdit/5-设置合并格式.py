from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('设置合并格式的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        te=QTextEdit(self)
        te.setGeometry(50,50,300,300)
        self.tc=te.textCursor()
        self.setformat()
    def setformat(self):
        tcf=QTextCharFormat()
        tcf.setFontFamily('Arial')
        tcf.setFontPointSize(20)
        tcf.setFontItalic(True)

        tbf=QTextBlockFormat()
        tbf.setAlignment(Qt.AlignmentFlag.AlignLeft)
        tbf.setIndent(2)

        self.tc.insertText('xxx',tcf)
        self.tc.setBlockCharFormat(tcf)
        # self.tc.setCharFormat(tcf)
        self.tc.setBlockFormat(tbf)
        # self.tc.mergeBlockCharFormat(tcf)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())