from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('交互状态案例的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label=QLabel(self)
        # label.setText('标签')
        label.move(100,50)
        label.hide()

        line=QLineEdit(self)
        # line.setText('输入框')
        line.move(100,100)

        button=QPushButton(self)
        button.setText('按钮')
        button.move(100,150)
        button.setEnabled(False)

        def line_cao(text):
            if len(text) == 0:
                button.setEnabled(False)
            else:
                button.setEnabled(True)
        line.textChanged.connect(line_cao)

        def check():
            text=line.text()
            label.show()
            if text == 'Sz':
                label.setText('登陆成功')
                label.adjustSize()
            else:
                label.setText('登陆失败')
                label.adjustSize()
        button.pressed.connect(check)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())