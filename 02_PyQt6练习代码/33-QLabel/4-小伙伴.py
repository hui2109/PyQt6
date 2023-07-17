from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('小伙伴的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label=QLabel('1234qwe&r',self)
        line1=QLineEdit(self)
        line1.setGeometry(QRect(100,100,100,30))
        line2=QLineEdit(self)
        line2.setGeometry(QRect(100,150,100,30))

        label.setBuddy(line1)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())