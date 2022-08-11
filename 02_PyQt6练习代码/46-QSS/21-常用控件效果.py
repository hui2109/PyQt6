from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(450,700)
        self.setWindowTitle('常用控件效果的学习')
        self.move(460,60)
        self.initWidgets()
    def initWidgets(self):
        btn=QPushButton('点击我谢谢！')
        clb=QCommandLinkButton('命令链接按钮')
        rb=QRadioButton('吃饭了吗')
        cb=QCheckBox('彩色图像')
        cb.setTristate()
        le=QLineEdit('hello!')
        le.setEchoMode(QLineEdit.EchoMode.Password)
        le.setProperty('echoMode','2')
        le.setReadOnly(True)
        le.setProperty('readOnly','true')
        te=QTextEdit('你好！')
        te.setFixedSize(300,50)
        sb=QSpinBox()
        comb=QComboBox()
        comb.addItems(list('12345'))
        comb.setEditable(True)
        slider=QSlider(Qt.Orientation.Horizontal)
        pb=QProgressBar()
        pb.setValue(60)
        h_box=QVBoxLayout()
        h_box.addWidget(btn)
        h_box.addWidget(clb)
        h_box.addWidget(rb)
        h_box.addWidget(cb)
        h_box.addWidget(le)
        h_box.addWidget(te)
        h_box.addWidget(sb)
        h_box.addWidget(comb)
        h_box.addWidget(slider)
        h_box.addWidget(pb)
        self.setLayout(h_box)


if __name__ == '__main__':
    import sys,QSSTool
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    QSSTool.QssTool.readqssfile('PyQt6布局/PyQt6练习代码/46-QSS/QSS样式表/17-常用控件效果.qss',app)
    sys.exit(app.exec())