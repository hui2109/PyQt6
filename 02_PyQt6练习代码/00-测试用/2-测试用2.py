from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtMultimediaWidgets import *
from PyQt6.QtMultimedia import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.vw=QVideoWidget(self)
        self.vw.setGeometry(0,0,500,500)
        self.md=QMediaDevices()
        self.cd=self.md.videoInputs()[0]

        self.ca=QCamera(self.cd,self)
        self.ca.start()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())