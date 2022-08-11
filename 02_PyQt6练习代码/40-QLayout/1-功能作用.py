from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(600,600)
        self.setWindowTitle('功能作用的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label1=QLabel()
        label1.setStyleSheet('background-color:cyan;')
        label2=QLabel()
        label2.setStyleSheet('background-color:yellow;')
        label3=QLabel()
        label3.setStyleSheet('background-color:blue;')
        label4=QLabel()
        label4.setStyleSheet('background-color:red;')
        label5=QLabel()
        label5.setStyleSheet('background-color:orange;')
        label6=QLabel()
        label6.setStyleSheet('background-color:purple;')
        label7=QLabel()
        label7.setStyleSheet('background-color:green;')
        label8=QLabel()
        label8.setStyleSheet('background-color:grey;')

        layout=QBoxLayout(QBoxLayout.Direction.LeftToRight)      
        layout.setSpacing(20)
        layout.setContentsMargins(20,20,20,20)

        # layout.replaceWidget(label1,label5)
        # label1.hide()

        layout_sub=QBoxLayout(QBoxLayout.Direction.TopToBottom)
        layout.setSpacing(20)
        layout.setContentsMargins(20,20,20,20)    
        layout_sub.addWidget(label8)
        layout_sub.addWidget(label7)
        layout_sub.addWidget(label6)


        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addLayout(layout_sub)

        # layout.addWidget(label6)
        # layout.addWidget(label7)
        # layout.addWidget(label8)

        # layout.setEnabled(False)
        layout_sub.setEnabled(False)

        self.setLayout(layout)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())