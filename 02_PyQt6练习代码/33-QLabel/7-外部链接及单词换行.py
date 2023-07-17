from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('外部链接及单词换行的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label1=QLabel('<a href="https://www.baidu.com">百度一下，你就知道</a>',self)
        label1.setGeometry(QRect(100,100,200,100))
        label1.setOpenExternalLinks(True)

        label2=QLabel('\n'.join('123456789'),self)
        label2.setGeometry(QRect(100,200,200,200))
        
        label3=QLabel('tonight is a fantacy night',self)
        label3.setGeometry(QRect(100,350,50,200))
        label3.setWordWrap(True)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())