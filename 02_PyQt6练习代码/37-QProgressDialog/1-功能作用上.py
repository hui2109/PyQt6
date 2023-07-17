from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('功能作用上的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        pd=QProgressDialog('下载进度','取消',0,100,self)
        pd.setMinimumDuration(1000)
        pd.setAutoClose(False)
        pd.setAutoReset(False)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())