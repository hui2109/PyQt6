from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('字体格式的学习')
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
        # 29-QFontDialog.getFont()
        self.te.setFontFamily('宋体-简')
        self.te.setFontPointSize(20)
        # self.te.setFontWeight(10)
        self.te.setFontWeight(QFont.Weight.Black)
        self.te.setFontItalic(True)
        self.te.setFontUnderline(True)

        font=QFont()
        font.setBold(True)
        font.setStrikeOut(True)
        self.te.setCurrentFont(font)
        
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())