import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('窗口拖拽的学习')
        self.move(100,100)
        self.resize(500,500)
        # self.move_flag=False
    def mousePressEvent(self,evt):
        if evt.button() == Qt.MouseButton.LeftButton:
            # self.move_flag=True
            self.move_x=evt.globalPosition().x()
            self.move_y=evt.globalPosition().y()
            self.original_x=self.x()
            self.original_y=self.y()
    def mouseMoveEvent(self, evt): 
        # if self.move_flag:
        if evt.buttons() == Qt.MouseButton.LeftButton:
            new_x=self.original_x+evt.globalPosition().x()-self.move_x
            new_y=self.original_y+evt.globalPosition().y()-self.move_y
            self.move(int(new_x),int(new_y))
    def mouseReleaseEvent(self,evt):
        # self.move_flag=False
        pass

app=QApplication(sys.argv)
window=MyWindow()
window.show()
sys.exit(app.exec())