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
        btn1=QRadioButton(self)
        btn1.setText('男')
        btn1.move(100,50)
        btn2=QRadioButton(self)
        btn2.setText('女')
        btn2.move(100,100)
        btn1.setChecked(True)

        btn3=QRadioButton(self)
        btn3.setText('yes')
        btn3.move(200,50)
        btn4=QRadioButton(self)
        btn4.setText('no')
        btn4.move(200,100)

        group1=QButtonGroup(self)
        group1.addButton(btn1,1)
        group1.addButton(btn2,2)
        group2=QButtonGroup(self)
        group2.addButton(btn3)
        group2.addButton(btn4)
        
        #######################
        def cao(val):
            print(group1.id(val))
        group1.buttonClicked.connect(cao)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())