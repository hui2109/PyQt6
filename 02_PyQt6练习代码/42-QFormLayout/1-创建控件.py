from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('创建控件的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        name=QLabel('姓名')
        name_le=QLineEdit()
        age=QLabel('年龄')
        age_sb=QSpinBox()

        forml=QFormLayout()
        forml.addRow(name,name_le)
        forml.addRow(age,age_sb)

        # forml.addWidget(age)
        # forml.addWidget(age_sb)

        self.setLayout(forml)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())