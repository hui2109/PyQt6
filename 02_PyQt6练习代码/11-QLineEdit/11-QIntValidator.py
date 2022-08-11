from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyValidator(QIntValidator):
    def fixup(self,input_str):
        print('调用了fixup方法',input_str)
        if len(input_str)==0 or int(input_str)<18:
            return '18'
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('QIntValidator的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        le1=QLineEdit(self)
        le1.move(100,100)
        validator=MyValidator(18,180,self)
        le1.setValidator(validator)
        le2=QLineEdit(self)
        le2.move(100,200)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())