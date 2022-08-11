from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('第三方样式表的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        btn=QPushButton('请点击我')
        comb=QComboBox()
        comb.addItems(['1','2','3','4'])
        cb=QSpinBox()
        label=QLabel('天气很热')
        te=QTextEdit('hello!')
        vbox=QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(comb)
        vbox.addWidget(cb)
        vbox.addWidget(label)
        vbox.addWidget(te)
        self.setLayout(vbox)

if __name__ == '__main__':
    import sys,qdarkstyle
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    print(qdarkstyle.load_stylesheet_pyqt5())
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec())