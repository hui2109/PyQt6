from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('功能作用的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        fd=QFileDialog(self,'请打开一个文件','./',
        'All Files(*.*);;Images(*.png *.jpg);;Python文件(*.py)')

        fd.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        fd.setDefaultSuffix('.txt')
        fd.setOptions(QFileDialog.Option.DontUseNativeDialog)

        # fd.setFileMode(QFileDialog.FileMode.AnyFile)
        fd.setFileMode(QFileDialog.FileMode.ExistingFiles)
        # fd.setFileMode(QFileDialog.FileMode.Directory)
        # fd.setFileMode(QFileDialog.FileMode.ExistingFile)

        # fd.setNameFilter('Python文件(*.py);;Images(*.png *.jpg')
        fd.setNameFilters(['Python文件(*.py)','Images(*.png *.jpg'])

        fd.setViewMode(QFileDialog.ViewMode.Detail)
        fd.setViewMode(QFileDialog.ViewMode.List)

        fd.setLabelText(QFileDialog.DialogLabel.FileName,'辉哥的文件')
        fd.setLabelText(QFileDialog.DialogLabel.Accept,'辉哥的接受按钮')
        fd.setLabelText(QFileDialog.DialogLabel.Reject,'辉哥的拒绝按钮')
        fd.setLabelText(QFileDialog.DialogLabel.FileType,'辉哥的文件类型')
        fd.setLabelText(QFileDialog.DialogLabel.LookIn,'辉哥的查看路径')

        fd.fileSelected.connect(lambda val:print(val))
        fd.open()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())