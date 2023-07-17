from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('信号的学习')
        self.move(100, 100)
        self.initWidgets()

    def initWidgets(self):
        self.d = QDialog(self)
        self.d.setGeometry(50,50,500,500)

        self.btn1=QPushButton(self.d)
        self.btn1.setGeometry(50,50,50,50)
        self.btn1.setText('接受')

        self.btn2=QPushButton(self.d)
        self.btn2.setGeometry(150,50,50,50)
        self.btn2.setText('拒绝')

        self.btn3=QPushButton(self.d)
        self.btn3.setGeometry(250,50,50,50)
        self.btn3.setText('完成')

        self.btn4=QPushButton(self.d)
        self.btn4.setGeometry(350,50,50,50)
        self.btn4.setText('自定义')

        self.btn1.clicked.connect(lambda:self.d.accept())
        self.btn1.clicked.connect(lambda:print(self.d.result()))

        self.btn2.clicked.connect(lambda:self.d.reject())
        self.btn2.clicked.connect(lambda:print(self.d.result()))

        self.btn3.clicked.connect(lambda:self.d.done(98))
        self.btn3.clicked.connect(lambda:print(self.d.result()))

        self.btn4.clicked.connect(self.clicked_btn4)

        self.d.accepted.connect(lambda:print('点击了接受按钮'))
        self.d.rejected.connect(lambda:print('点击了拒绝按钮'))
        self.d.finished.connect(lambda val:print('点击了完成按钮',val))

        # result=self.d.exec()
        # print('exec的结果',result)

        self.d.open()

    def clicked_btn4(self):
        self.d.setResult(23)
        print(self.d.result())
        ce=QCloseEvent()
        self.d.closeEvent(ce)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
