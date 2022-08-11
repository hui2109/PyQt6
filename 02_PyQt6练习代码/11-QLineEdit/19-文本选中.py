from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('文本选中的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.line1=QLineEdit(self)
        self.line1.setGeometry(10,10,150,150)
        self.btn=QPushButton(self)
        self.btn.setGeometry(10,330,100,30)
        self.btn.setText('点击')
        self.btn.clicked.connect(self.btnClicked)
    def btnClicked(self):
        # self.line1.setSelection(2,6)
        # self.line1.selectAll()
        # self.line1.setSelection(0,len(self.line1.text()))
        self.line1.deselect()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())