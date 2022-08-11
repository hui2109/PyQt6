from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('文本交互标志的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label=QLabel('你是谁？',self)
        label.setGeometry(QRect(100,100,100,100))

        label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByKeyboard | 
            Qt.TextInteractionFlag.TextSelectableByMouse | 
            Qt.TextInteractionFlag.TextEditable)
        label.setSelection (1,2)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())