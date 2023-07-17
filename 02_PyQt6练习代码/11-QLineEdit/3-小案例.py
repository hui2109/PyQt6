from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('小案例的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        le_1=QLineEdit(self)
        le_1.move(100,100)
        le_2=QLineEdit(self)
        le_2.move(100,150)
        btn=QPushButton(self)
        btn.setText('复制')
        btn.move(100,200)
        def cao():
            a=le_1.text()
            le_2.setText(a)
        btn.clicked.connect(cao)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())    