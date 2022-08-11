from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500,500)
        self.setWindowTitle('事件转发的学习')
        self.move(100,100)
    def mousePressEvent(self, event):
        print('主窗口被按下了')
class SubWindow(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.resize(200,200)
        self.setStyleSheet('background-color:yellow;')
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
    def mousePressEvent(self, event):
        print('次窗口被按下了')
class Label(QLabel):
    def mousePressEvent(self, event):
        print('标签被按下了')
class Button(QPushButton):
    # def mousePressEvent(self, event):
    #     print('按钮被按下了')
        # print(event.isAccepted())
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print(event.isAccepted())
        # event.ignore()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()
    sub_window=SubWindow(window)

    label=Label(sub_window)
    label.setText('这是一个标签')
    label.move(50,50)
    label.setStyleSheet('background-color:red;')

    button=Button(sub_window)
    button.move(50,100)
    button.setText('这是一个按钮')
    # button.setStyleSheet('background-color:blue;')

    window.show()
    sys.exit(app.exec())