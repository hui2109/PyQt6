from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('字体的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        te=QTextEdit()
        te.setStyleSheet('''
                min-width:200px;
                min-height:200px;
                max-width:400px;                        
                max-height:400px;
            
            ''')
        vbox=QVBoxLayout()
        vbox.addWidget(te)
        self.setLayout(vbox)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())