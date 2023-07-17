from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('内外边距测试的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label=QLabel('您好!\nnosa\nad\nasd',self)
        label.move(150,150)
        label.setStyleSheet('''
            QLabel {
                
                background-color:cyan;
                padding-top:-30px;
                
                
                
                
            }        
        ''')

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())