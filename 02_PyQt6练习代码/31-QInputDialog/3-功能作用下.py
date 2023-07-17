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
        self.id=QInputDialog(self,Qt.WindowType.FramelessWindowHint)
        self.id.open()

        self.id.setLabelText('请输入用户名')
        self.id.setOkButtonText('我想确定')
        self.id.setCancelButtonText('我想取消')

        self.id.setInputMode(QInputDialog.InputMode.TextInput)
        # self.id.setInputMode(QInputDialog.InputMode.IntInput)
        # self.id.setInputMode(QInputDialog.InputMode.DoubleInput)

        self.id.setTextEchoMode(QLineEdit.EchoMode.Password)
        self.id.setTextValue('2')

        self.id.setComboBoxItems(['1','2','3'])

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())