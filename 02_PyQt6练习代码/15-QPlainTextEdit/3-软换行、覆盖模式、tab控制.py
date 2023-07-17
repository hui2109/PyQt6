from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('软换行、覆盖模式、tab控制的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.pte=QPlainTextEdit(self)
        self.pte.setGeometry(10,10,300,300)
        self.pte.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.pte.setOverwriteMode(False)
        self.pte.setTabChangesFocus(True)
        self.pte.setTabStopDistance(100)

        self.btn=QPushButton(self)
        self.btn.setGeometry(350,10,100,30)
        self.btn.setText('点我谢谢')
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())