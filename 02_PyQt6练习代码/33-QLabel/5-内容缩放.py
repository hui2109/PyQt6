from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('内容缩放的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label=QLabel(self)
        label.setPixmap(QPixmap('PyQt6布局/PyQt6练习代码/04-QWidget/7-鼠标图.png'))
        label.setGeometry(QRect(100,100,100,100))
        # label.adjustSize()
        label.setScaledContents(True)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())