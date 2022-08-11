from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(350,350)
        self.setWindowTitle('完善步骤的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        btn=QPushButton('按钮1',self)
        btn.resize(50,50)
        animation=QPropertyAnimation(btn,b'pos',self)
        animation.setStartValue(QPoint(0,0))
        animation.setEndValue(QPoint(300,300))
        animation.setDuration(3000)

        animation.setEasingCurve(QEasingCurve.Type.OutBounce)

        animation.start()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())