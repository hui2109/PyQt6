from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from Ui_signal import Ui_Form
class MyWindow(QWidget,Ui_Form):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('自定义信号下的学习')
        self.move(100,100)
        self.setupUi(self)
    @pyqtSlot(bool)
    def on_pushButton_clicked(self,val):
            print('按钮被点击了',val)

    @pyqtSlot()
    def on_pushButton_pressed(self):
            print('按钮被按下了')

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())