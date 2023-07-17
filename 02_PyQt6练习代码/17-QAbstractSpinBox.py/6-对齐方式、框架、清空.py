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
        self.setWindowTitle('对齐方式的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.asb=MySpinBox(self,2)
        self.asb.setGeometry(100,100,100,100)
        self.asb.setAccelerated(True)
        print(self.asb.text())
        print(self.asb.lineEdit().text())
        self.asb.lineEdit().setText('45')
        self.asb.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)
        self.asb.setFrame(True)
        print(self.asb.hasFrame())
        # self.asb.clear()
        # self.asb.lineEdit().clear()

        self.asb.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())