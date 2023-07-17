from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('信号的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        fd=QFileDialog(self,'请打开一个文件','./',
        'All Files(*.*);;Images(*.png *.jpg);;Python文件(*.py)')

        fd.setFileMode(QFileDialog.FileMode.ExistingFiles)

        fd.currentChanged.connect(lambda val:print('当前路径改变了',val))
        fd.currentUrlChanged.connect(lambda val:print('当前Url改变了',val))
        fd.directoryEntered.connect(lambda val:print('当前进入目录了',val))
        fd.directoryUrlEntered.connect(lambda val:print('当前进入目录Url了',val))
        fd.filterSelected.connect(lambda val:print('选择过滤器了',val))
        fd.fileSelected.connect(lambda val:print('最终选择文件了',val))
        fd.filesSelected.connect(lambda val:print('最终选择多个文件了',val))
        fd.urlSelected.connect(lambda val:print('最终选择文件Url了',val))
        fd.urlsSelected.connect(lambda val:print('最终选择多个文件Url了',val))

        fd.fileSelected.connect(lambda val:print(val))
        fd.open()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())