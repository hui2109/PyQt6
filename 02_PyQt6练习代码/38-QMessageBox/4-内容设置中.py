from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('内容设置中的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        msg=QMessageBox(self)
        btn1=QPushButton('确定',self)
        msg.addButton(btn1,QMessageBox.ButtonRole.YesRole)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        # msg.setDefaultButton(btn1)
        msg.setDefaultButton(QMessageBox.StandardButton.Cancel)
        msg.setEscapeButton(btn1)
        msg.show()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())