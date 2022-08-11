from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('信号')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.pte=QPlainTextEdit(self)
        self.pte.setGeometry(10,10,300,300)
        self.pte1=QPlainTextEdit(self)
        self.pte1.setGeometry(10,320,300,300)
        self.btn=QPushButton('测试按钮',self)
        self.btn.setGeometry(300,320,100,30)
        self.btn.clicked.connect(self.btnClicked)
    def btnClicked(self):   
        # self.pte.textChanged.connect(lambda : print('文本内容改变了',\
        #                       self.pte.toPlainText()))

        # self.pte.selectionChanged.connect(lambda : print('选中内容改变了',\
        #                         self.pte.textCursor().selectedText()))
        
        # td=self.pte.document()
        # self.pte.modificationChanged.connect(lambda val: print('编辑状态改变了',val))
        # td.setModified(True)
        # td.setModified(False)

        # self.pte.cursorPositionChanged.connect(lambda : print('光标位置改变了'))
        
        # self.pte.cursorPositionChanged.connect(lambda : print('光标位置改变了'))

        self.pte.blockCountChanged.connect(lambda val: print('块的个数改变了',val))
        

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())