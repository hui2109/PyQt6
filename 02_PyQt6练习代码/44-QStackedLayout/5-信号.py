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
        bl=QBoxLayout(QBoxLayout.Direction.TopToBottom)
        sl=QStackedLayout()
        self.setLayout(sl)

        label1=QLabel()
        label1.setStyleSheet('background-color:cyan;')
        label2=QLabel('标签2')
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

        bl.addWidget(label5)
        bl.addWidget(label6)
        bl.addWidget(label7)
        bl.addWidget(label8)
        
        sl.addWidget(label1)
        sl.addWidget(label2)
        sl.addWidget(label3)
        sl.addWidget(label4)

        sl.currentChanged.connect(self.currentchanged)
        sl.widgetRemoved.connect(self.widgetremoved)

        sl.setCurrentIndex(1)
        sl.removeWidget(label4)

    def currentchanged(self,val):
        print('currentChanged:',val)
    def widgetremoved(self,val):
        print('widgetRemoved:',val)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())