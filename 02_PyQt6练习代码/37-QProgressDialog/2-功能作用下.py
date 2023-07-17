from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('功能作用下的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.pd=QProgressDialog('xx1','xx2',0,100,self)
        self.pd.setMinimumDuration(2000)

        self.pd.setWindowTitle('希望是这个标题')
        self.timer=QTimer(self.pd)
        self.timer.timeout.connect(self.time_out)
        self.timer.start(1000)
        self.pd.setValue(90)

        # self.pd.setAutoReset(False)
        # self.pd.setAutoClose(False)
        
    def time_out(self):
        print(self.pd.value())
        if self.pd.value()<100 and self.pd.value()>=0:
            print(self.pd.value())
            self.pd.setValue(self.pd.value()+1)
        else:
            print(self.pd.value())
            self.timer.stop()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())