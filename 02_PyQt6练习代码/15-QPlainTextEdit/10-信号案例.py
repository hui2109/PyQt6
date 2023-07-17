from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('信号案例')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.pte=QPlainTextEdit(self)
        self.pte.setGeometry(100,10,300,300)
        self.btn=QPushButton('测试按钮',self)
        self.btn.setGeometry(300,320,100,30)
        self.btn.clicked.connect(self.btnClicked)

        # 展示行号
        line_num_parent = QWidget(self)
        line_num_parent.setGeometry(50,10,50,300)
        line_num_parent.setStyleSheet('background-color:cyan;')

        label_num='\n'.join([str(i) for i in range(1,101)])

        self.label=QLabel(line_num_parent)
        self.label.move(0, 5)
        self.label.setText(label_num)
        self.label.adjustSize()
    def btnClicked(self):   
        self.pte.updateRequest.connect(self.updateLabel)
    def updateLabel(self,rect,dy):
        self.label.move(self.label.x(),self.label.y()+dy)
        # print(dy)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())