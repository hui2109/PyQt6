from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('简单使用与演示的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label1=QLabel()
        label1.setStyleSheet('background-color:cyan;')
        label2=QLabel()
        label2.setStyleSheet('background-color:yellow;')
        label3=QLabel()
        label3.setStyleSheet('background-color:blue;')

        # layout=QVBoxLayout()
        layout=QHBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.setLayout(layout)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        print(self.children())
        print(self.findChildren(QObject,
            options=Qt.FindChildOption.FindChildrenRecursively))

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())