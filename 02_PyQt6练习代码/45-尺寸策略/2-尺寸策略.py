from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class Label(QLabel):
    def sizeHint(self):
        return QSize(100,100)

class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('尺寸策略的学习')
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

        policy=QSizePolicy(QSizePolicy.Policy.Fixed,
                    QSizePolicy.Policy.Fixed)
        # policy=QSizePolicy(QSizePolicy.Policy.Fixed,
        #             QSizePolicy.Policy.Minimum)
        # policy=QSizePolicy(QSizePolicy.Policy.Fixed,
        #             QSizePolicy.Policy.Maximum)
        # policy=QSizePolicy(QSizePolicy.Policy.Fixed,
        #             QSizePolicy.Policy.Preferred)
        # policy=QSizePolicy(QSizePolicy.Policy.Fixed,
        #             QSizePolicy.Policy.MinimumExpanding)
        # policy=QSizePolicy(QSizePolicy.Policy.Ignored,
        #             QSizePolicy.Policy.Ignored)

        # policy.setRetainSizeWhenHidden(True)
        # label1.setSizePolicy(policy)
        # label1.hide()

        print(policy.expandingDirections())
        
        label1.setSizePolicy(policy)

        self.setLayout(layout)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())