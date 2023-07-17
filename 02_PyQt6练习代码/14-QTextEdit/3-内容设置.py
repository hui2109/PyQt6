from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('内容设置的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        text_edit=QTextEdit('要下雨了',self)
        text_edit.setGeometry(50,50,300,300)
        self.te=text_edit
        # self.plaintext()
        # self.htmltext()
        # self.usualtext()
        # self.appendtext()
        self.cleartext()

    # 设置普通文本    
    def plaintext(self):
        # self.te.setPlainText('xxx')
        self.te.insertPlainText('xxx')
        print(self.te.toPlainText())
    
    # 设置HTML文本
    def htmltext(self):
        # self.te.setHtml('<h1>哈哈哈</h1>')
        self.te.insertHtml('<h1>哈哈哈</h1>')
        print(self.te.toHtml())

    # 设置通用文本
    def usualtext(self):
        # self.te.setText('<h1>哈哈哈</h1>')
        self.te.setText('<h1asfd>哈哈哈</h1xxxx>')

    # 设置追加文本
    def appendtext(self):
        self.te.append('1234')
    
    # 清空文件
    def cleartext(self):
        self.te.clear()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())