from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('信号的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label=QLabel(self)
        label.setGeometry(50,50,100,100)
        label.setText('马上要去<a href="https://www.baidu.com">百度一下，你就知道</a>值夜班了')
        label.adjustSize()
        label.setOpenExternalLinks(True)
        label.linkHovered.connect(lambda val:print('hovered',val))
        label.linkActivated.connect(lambda val:print('activated',val))
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())