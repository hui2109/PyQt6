from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(1200,700)
        self.setWindowTitle('QAnimationGroup的学习')
        self.move(0,0)
        self.initWidgets()
    def initWidgets(self):
        btn1=QPushButton('按钮1',self)
        btn2=QPushButton('按钮2',self)
        btn1.setGeometry(0,0,100,100)
        btn2.setGeometry(150,150,100,100)
        btn1.setStyleSheet('''
                background-color:red;
        
        ''')
        btn2.setStyleSheet('''
                background-color:blue;
        
        ''')

        animation1=QPropertyAnimation(btn1,b'pos',self)
        animation1.setKeyValues([[0,QPoint(0,0)],[0.25,QPoint(1100,0)],
                                [0.5,QPoint(1100,600)],[0.75,QPoint(0,600)],
                                [1,QPoint(0,0)]])
        animation1.setDuration(5000)
        # animation1.start()

        animation2=QPropertyAnimation(btn2,b'pos',self)
        animation2.setKeyValues([[0,QPoint(150,150)],[0.25,QPoint(950,150)],
                                [0.5,QPoint(950,450)],[0.75,QPoint(150,450)],
                                [1,QPoint(150,150)]])
        animation2.setDuration(5000)
        # animation2.start()

        # animation_group=QParallelAnimationGroup(self)
        animation_group=QSequentialAnimationGroup(self)
        animation_group.currentAnimationChanged.connect(lambda val:print(val))
        animation_group.addAnimation(animation1)
        animation_group.addPause(5000)
        animation_group.addAnimation(animation2)
        animation_group.start()
        
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())