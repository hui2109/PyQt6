from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('输出模式的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        le=QLineEdit(self)
        le.setEchoMode(QLineEdit.EchoMode.Normal)
        le.setEchoMode(QLineEdit.EchoMode.NoEcho)
        le.setEchoMode(QLineEdit.EchoMode.Password)
        le.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        print(le.echoMode()==QLineEdit.EchoMode.PasswordEchoOnEdit)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())