from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('文本的设置和获取的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        le=QLineEdit(self)
        le.setText('我是谁')
        # le.insert('123')
        print(le.text())
        print(le.displayText())

        btn=QPushButton(self)
        btn.move(100,100)
        btn.pressed.connect(lambda :le.insert('123'))
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())    