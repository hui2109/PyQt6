from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('静态方法的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        # a_tuple=QFileDialog.getOpenFileName(
        #     self,'请打开一个文件','./PyQt6布局/源代码',
        #     'All Files(*.*);;Images(*.png *.jpg);;Python文件(*.py)',
        #     'Python文件(*.py)')
        # print(a_tuple)

        # a_tuple=QFileDialog.getOpenFileNames(
        #     self,'请打开一个文件','./PyQt6布局/源代码',
        #     'All Files(*.*);;Images(*.png *.jpg);;Python文件(*.py)',
        #     'Python文件(*.py)')
        # print(a_tuple)

        # a_tuple=QFileDialog.getOpenFileUrl(
        #     self,'请打开一个文件',Url'./PyQt6布局/源代码'),
        #     'All Files(*.*);;Images(*.png *.jpg);;Python文件(*.py)',
        #     'Python文件(*.py)')
        # print(a_tuple)

        # a_tuple=QFileDialog.getOpenFileUrls(
        #     self,'请打开一个文件',QUrl('./PyQt6布局/源代码'),
        #     'All Files(*.*);;Images(*.png *.jpg);;Python文件(*.py)',
        #     'Python文件(*.py)')
        # print(a_tuple)

        # a_tuple=QFileDialog.getSaveFileName(
        #     self,'请打开一个文件','./PyQt6布局/源代码',
        #     'All Files(*.*);;Images(*.png *.jpg);;Python文件(*.py)',
        #     'Python文件(*.py)')
        # print(a_tuple)

        # a_tuple=QFileDialog.getSaveFileUrl(
        #     self,'请打开一个文件',QUrl('./PyQt6布局/源代码'),
        #     'All Files(*.*);;Images(*.png *.jpg);;Python文件(*.py)',
        #     'Python文件(*.py)')
        # print(a_tuple)

        # a_tuple=QFileDialog.getExistingDirectory(
        #     self,'请打开一个文件','./PyQt6布局/源代码',
        #     )
        # print(a_tuple)

        a_tuple=QFileDialog.getExistingDirectoryUrl(
            self,'请打开一个文件',QUrl('./PyQt6布局/源代码'),
            )
        print(a_tuple)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())