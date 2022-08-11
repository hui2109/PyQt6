from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('创建控件2的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        msg=QMessageBox(QMessageBox.Icon.Warning,
                        '警告',
                        '<h1>这是一个警告消息框</h1>',
                        QMessageBox.StandardButton.Apply | 
                        QMessageBox.StandardButton.Cancel,
                        self)
        msg.show()
        # msg.open()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())