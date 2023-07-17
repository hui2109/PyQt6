from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class SB(QSpinBox):
    def textFromValue(self, v):
        week={0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期天'}
        return week[v]
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('自定义展示格式的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        sb=SB(self)
        sb.setGeometry(100,100,100,100)
        sb.setWrapping(True)
        sb.setRange(0,6)

        te=QTextEdit(self)
        te.setGeometry(100,200,100,100)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())