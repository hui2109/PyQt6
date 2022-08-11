from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('信号的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        rb_man=QRadioButton(self)
        rb_man.setText('男')
        rb_man.move(100,100)
        rb_man.setChecked(True)

        rb_woman=QRadioButton(self)
        rb_woman.setText('女')
        rb_woman.move(100,150)
        icon=QIcon('Python3/pyside6布局/PySide6练习代码/04-QWidget/7-鼠标图.png')
        rb_woman.setIcon(icon)
        rb_woman.setIconSize(QSize(50,50))
        rb_woman.setShortcut('Ctrl+W')
        
        def cao(signal):
            print(signal)
        rb_man.toggled.connect(cao)

        rb_woman.setAutoExclusive(False)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())    