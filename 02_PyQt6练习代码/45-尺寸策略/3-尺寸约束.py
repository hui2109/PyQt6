from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class Label(QLabel):
    def sizeHint(self):
        return QSize(100,100)
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.setMinimumSize(QSize(300,300))
        self.setMaximumSize(QSize(600,600))
        self.setWindowTitle('尺寸约束的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label1=Label()
        label1.setStyleSheet('background-color:cyan;')
        label2=Label()
        label2.setStyleSheet('background-color:yellow;')
        label3=Label()
        label3.setStyleSheet('background-color:blue;')
        label4=Label()
        label4.setStyleSheet('background-color:red;')
        label5=Label()
        label5.setStyleSheet('background-color:orange;')
        label6=Label()
        label6.setStyleSheet('background-color:purple;')
        label7=Label()
        label7.setStyleSheet('background-color:green;')
        label8=Label()
        label8.setStyleSheet('background-color:grey;')

        layout=QBoxLayout(QBoxLayout.Direction.LeftToRight)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        
        # layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        # layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        # layout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        # layout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        # layout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        layout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)

        self.setLayout(layout)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())