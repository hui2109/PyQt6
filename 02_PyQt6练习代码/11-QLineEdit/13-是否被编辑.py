from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('是否被编辑的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(100,100,200,30)
        btn=QPushButton('点击',self)
        btn.clicked.connect(self.btnClick)
        line2=QLineEdit(self)
        line2.setGeometry(100,200,200,30)
    def btnClick(self):
        print(self.lineEdit.isModified())
        self.lineEdit.setModified(False)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())