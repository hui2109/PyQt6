from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MySpinBox(QAbstractSpinBox):
    def __init__(self,parent=None,num=0,*args,**kwargs):
        super(MySpinBox,self).__init__(parent,*args,**kwargs)
        self.lineEdit().setText(str(num))
    def stepEnabled(self):
        return QAbstractSpinBox.StepEnabledFlag.StepDownEnabled|QAbstractSpinBox.StepEnabledFlag.StepUpEnabled
    def stepBy(self,step):
        self.lineEdit().setText(str(int(self.text())+step))
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('设置及获取内容的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.asb=MySpinBox(self,2)
        self.asb.setGeometry(100,100,100,100)
        self.asb.setAccelerated(True)
        print(self.asb.text())
        print(self.asb.lineEdit().text())
        self.asb.lineEdit().setText('45')
        self.asb.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())