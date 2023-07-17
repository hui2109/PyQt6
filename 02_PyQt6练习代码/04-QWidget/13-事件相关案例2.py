from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500,500)
        self.setWindowTitle('事件案例2的学习')
        self.move(100,100)
class MyLabel(QLabel):
    def __init__(self,parent):
        super().__init__(parent)
        self.resize(200,200)
        self.move(150,150)
        self.setStyleSheet('background-color:cyan;')
    def keyPressEvent(self,evt):
        print('xxxx')
        if evt.key()==Qt.Key.Key_Enter:
            print('用户按下了enter键')
        elif evt.modifiers()==Qt.KeyboardModifier.ControlModifier \
                and evt.key()==Qt.Key.Key_S:
            print('用户按下了ctrl+s键')
        elif evt.modifiers()==Qt.KeyboardModifier.ControlModifier \
                | Qt.KeyboardModifier.ShiftModifier \
                    and evt.key()==Qt.Key.Key_S:
            print('用户按下了ctrl+shift+s键')
            
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    label=MyLabel(window)
    label.grabKeyboard()
    window.show()
    sys.exit(app.exec())