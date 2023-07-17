from operator import le
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class AgeValidator(QValidator):
    def validate(self,input_str,pos):
        print('调用了validate方法',input_str,pos)
        if int(input_str)>=18 and int(input_str)<=180:
            return (QValidator.State.Acceptable,input_str,pos)
        elif int(input_str)>=1 and int(input_str)<=17:
            return (QValidator.State.Intermediate,input_str,pos)
        return (QValidator.State.Invalid,input_str,pos)
    def fixup(self,input_str):
        print('调用了fixup方法',input_str)
        if int(input_str)<18:
            return '18'
        else:
            return '180'
        # return (QValidator.State.Acceptable,'input_str',1)
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('QValidator基本使用的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        le1=QLineEdit(self)
        le1.move(100,100)
        validator=AgeValidator(self)
        le1.setValidator(validator)


        le2=QLineEdit(self)
        le2.move(100,200)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())