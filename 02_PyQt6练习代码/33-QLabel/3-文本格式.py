from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('文本格式的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label=QLabel('<h1>ad</h1>',self)
        label.setTextFormat(Qt.TextFormat.PlainText)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())