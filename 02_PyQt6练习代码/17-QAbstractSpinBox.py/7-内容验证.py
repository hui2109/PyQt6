from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MySpinBox(QAbstractSpinBox):
    def __init__(self,parent=None,num=0,*args,**kwargs):
        super(MySpinBox,self).__init__(parent,*args,**kwargs)
        self.lineEdit().setText(str(num))
    def stepEnabled(self):
        if self.text()!='':
            if int(self.text())<19:
                return QAbstractSpinBox.StepEnabledFlag.StepUpEnabled
            elif int(self.text())>18 and int(self.text())<180:
                return QAbstractSpinBox.StepEnabledFlag.StepUpEnabled|QAbstractSpinBox.StepEnabledFlag.StepDownEnabled
            else:
                return QAbstractSpinBox.StepEnabledFlag.StepDownEnabled
        else:
            return QAbstractSpinBox.StepEnabledFlag.StepNone
    def stepBy(self,step):
        self.lineEdit().setText(str(int(self.text())+step))
    def validate(self,input,pos):
        if input != '':
            if int(input)<18:
                return (QValidator.State.Intermediate,input,pos)
            elif int(input)<=180:
                return (QValidator.State.Acceptable,input,pos)
            else:
                return (QValidator.State.Invalid,input,pos)
        else:
            return (QValidator.State.Intermediate,input,pos)
    def fixup(self,input):
        return '18'
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('内容验证的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.asb=MySpinBox(self,18)
        self.asb.setGeometry(100,100,100,100)
        self.asb.setAccelerated(True)
        self.btn=QTextEdit('点我',self)
        self.btn.setGeometry(100,300,100,100)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())