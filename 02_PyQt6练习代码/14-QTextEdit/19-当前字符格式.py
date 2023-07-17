from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('当前字符格式的学习')
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
        tcf1=QTextCharFormat()
        tcf1.setFontFamily('Times New Roman')
        tcf1.setFontPointSize(20)
        tcf1.setFontCapitalization(QFont.Capitalization.Capitalize)
        self.te.setCurrentCharFormat(tcf1)

        tcf2=QTextCharFormat()
        tcf2.setFontOverline(True)
        self.te.mergeCurrentCharFormat(tcf2)
        
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())