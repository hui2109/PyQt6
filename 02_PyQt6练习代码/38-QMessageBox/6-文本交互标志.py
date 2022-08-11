from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('文本交互标志的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        msg=QMessageBox(self)
        msg.setWindowTitle('<h1>消息框</h1>')
        msg.setIconPixmap(QPixmap('PyQt6布局/PyQt6练习代码/04-QWidget/7-鼠标图.png').scaled(50,50))
        msg.setText('<h2>这是一个消息框</h2>')
        msg.setTextFormat(Qt.TextFormat.PlainText)
        msg.setInformativeText('<h3>这是两个消息框</h3>')
        msg.setDetailedText('<h4>这是三个消息框</h4>')
        msg.setCheckBox(QCheckBox('这是一个复选框',msg))

        msg.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditorInteraction)

        msg.show()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())    