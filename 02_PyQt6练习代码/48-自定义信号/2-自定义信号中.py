from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from pkg_resources import ContextualVersionConflict
QMouseEvent
class Btn(QPushButton):
    rightClicked=pyqtSignal([str],[int],[str,int])
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button() == Qt.MouseButton.RightButton:
            print('右键被点击了-1')
            self.rightClicked[str].emit(self.text())
            self.rightClicked[int].emit(888)
            self.rightClicked[str,int].emit(self.text(),123)

class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('右键单击信号的学习')
        self.move(100, 100)
        self.initWidgets()

    def initWidgets(self):
        btn=Btn('按钮1',self)
        btn.pressed.connect(lambda:print('按钮被按下了'))
        btn.rightClicked[str].connect(lambda content:print('右键被点击了-2',content))
        btn.rightClicked[int].connect(lambda content:print('右键被点击了-2',content))
        btn.rightClicked[str,int].connect(lambda content1,content2:print('右键被点击了-2',content1,content2))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
