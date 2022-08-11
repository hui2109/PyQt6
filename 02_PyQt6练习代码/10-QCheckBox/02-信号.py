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
        cb=QCheckBox("所有线代码",self)
        cb.setIcon(QIcon('Python3/pyside6布局/PySide6练习代码/04-QWidget/7-鼠标图.png'))
        cb.setIconSize(QSize(150,150))
        cb.setTristate(True)
        cb.setCheckState(Qt.CheckState.PartiallyChecked)
        # cb.setCheckState(Qt.CheckState.Checked)
        # cb.setCheckState(Qt.CheckState.Unchecked)
        def cao(val):
            print(val)
        cb.stateChanged.connect(cao)
        cb.toggled.connect(cao)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())