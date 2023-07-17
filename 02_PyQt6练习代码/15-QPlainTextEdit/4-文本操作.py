from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('文本操作的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.pte=QPlainTextEdit(self)
        self.pte.setGeometry(10,10,300,300)
        self.pte.setPlainText('马上要下雨了，快快行动吧！\n')
        self.pte.insertPlainText('我马上就去吃饭\n')
        self.pte.appendPlainText('顺便把电瓶车骑回家\n')
        self.pte.appendHtml('<a href="https://www.google.com">\
                            打开谷歌</a>')
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())