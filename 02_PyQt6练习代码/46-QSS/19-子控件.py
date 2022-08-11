from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from QSSTool import QssTool
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('子控件的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        sb=QSpinBox()
        cb=QCheckBox('今天出太阳吗？')
        comb=QComboBox()
        comb.addItems(['q','w','e','r'])
        vbox=QVBoxLayout()
        vbox.addWidget(sb)
        vbox.addWidget(cb)
        vbox.addWidget(comb)
        self.setLayout(vbox)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    QssTool.readqssfile('PyQt6布局/PyQt6练习代码/46-QSS/QSS样式表/16-子控件.qss',app)
    sys.exit(app.exec())