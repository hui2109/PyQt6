from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('常用编辑功能2的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.line1=QLineEdit(self)
        self.line1.setGeometry(10,10,150,150)
        self.line1.setTextMargins(100,100,0,0)
        self.line1.setAlignment(Qt.AlignmentFlag.AlignLeft\
                                |Qt.AlignmentFlag.AlignTop)
        self.line2=QLineEdit(self)
        self.line2.setGeometry(300,10,150,150)
        self.line1.setDragEnabled(True)
        btn=QPushButton('点击',self)
        btn.setGeometry(10,330,100,30)
        btn.clicked.connect(self.btnClicked)
    def btnClicked(self):
        self.line1.copy()
        self.line1.end(False)
        self.line1.paste()
        
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())