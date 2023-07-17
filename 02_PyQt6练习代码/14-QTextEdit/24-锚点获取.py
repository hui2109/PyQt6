from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyTextEdit(QTextEdit):
    def mousePressEvent(self,evt):
        print(evt.pos())
        link_str=self.anchorAt(evt.pos())
        if link_str!='':
            url=QUrl(link_str)
            a=QDesktopServices.openUrl(url)
            print(a)
        return super(MyTextEdit, self).mousePressEvent(evt)
        
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(1000,500)
        self.setWindowTitle('锚点获取的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.te=MyTextEdit(self)
        self.te.setGeometry(10,10,300,300)

        self.te.insertHtml('xxx\n'*300+
                            '<a name="123" href="https://www.baidu.com">我是谁</a>'+\
                            'aaa\n'*300)
        self.btn=QPushButton(self)
        self.btn.setText('选中')
        self.btn.setGeometry(160,350,100,30)
        self.btn.clicked.connect(self.select)
    def select(self):
        self.te.scrollToAnchor('123')
        
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())