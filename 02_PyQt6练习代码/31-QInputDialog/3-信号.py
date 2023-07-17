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
        self.id=QInputDialog(self,Qt.WindowType.FramelessWindowHint)
        self.id.open()

        self.id.setLabelText('请输入用户名')
        self.id.setOkButtonText('我想确定')
        self.id.setCancelButtonText('我想取消')

        self.id.setInputMode(QInputDialog.InputMode.IntInput)

        self.id.intValueChanged.connect(self.intValueChanged)
        self.id.intValueSelected.connect(self.intValueSelected)

        self.id.doubleValueChanged.connect(lambda val:print("浮点型数据发生改变", val))
        self.id.doubleValueSelected.connect(lambda val:print("浮点型数据最终被选中", val))

        self.id.textValueChanged.connect(lambda val:print("字符串型数据发生改变", val))
        self.id.textValueSelected.connect(lambda val:print("字符串型数据最终被选中", val))
    
    def intValueChanged(self,value):
        print('intValueChanged',value)
    def intValueSelected(self,value):
        print('intValueSelected',value)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())