from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('修改行的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label_name=QLabel('姓名')
        line_name=QLineEdit()
        btn_1=QRadioButton('男')
        btn_2=QRadioButton('女')
        line_submit=QPushButton('提交')

        h_box=QHBoxLayout()
        h_box.addWidget(btn_1)
        h_box.addWidget(btn_2)

        form_layout=QFormLayout()
        form_layout.addRow(label_name,line_name)
        form_layout.setLayout(0,QFormLayout.ItemRole.FieldRole,h_box)

        self.setLayout(form_layout) 

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())