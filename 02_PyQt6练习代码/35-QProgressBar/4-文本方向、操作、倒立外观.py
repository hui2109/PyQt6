from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('文本方向、操作、倒立外观的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        pb=QProgressBar(self)
        pb.setGeometry(50,50,400,100)

        pb.setTextVisible(True)
        pb.setOrientation(Qt.Orientation.Vertical)
        pb.setTextDirection(QProgressBar.Direction.BottomToTop)
        pb.setValue(75)

        pb.setInvertedAppearance(True)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())