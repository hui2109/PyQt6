from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('信号的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.pb=QProgressBar(self)
        self.pb.valueChanged.connect(lambda val:print(val))
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.time_out)
        self.timer.start(1000)
        self.pb.setValue(90)
    def time_out(self):
        if self.pb.value==self.pb.maximum():
            self.timer.stop()
        self.pb.setValue(self.pb.value()+1)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())