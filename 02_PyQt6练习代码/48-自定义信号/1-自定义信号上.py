from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
QMouseEvent
class Btn(QPushButton):
    rightClicked=pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button() == Qt.MouseButton.RightButton:
            print('右键被点击了-1')
            self.rightClicked.emit()

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
        btn.rightClicked.connect(lambda:print('右键被点击了-2'))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
