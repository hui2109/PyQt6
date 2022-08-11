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
        self.label=QLabel('请选择颜色',self)
        self.label.setGeometry(50,50,100,100)


        self.cd=QColorDialog(self)
        self.cd.setWindowTitle('请选择颜色')
        self.cd.setOptions(QColorDialog.ColorDialogOption.DontUseNativeDialog |
                           QColorDialog.ColorDialogOption.ShowAlphaChannel)
        self.cd.colorSelected.connect(self.colorselected)
        self.cd.currentColorChanged.connect(lambda color :print(color))
        self.cd.show()
    def colorselected(self,color):
        print(color)
        palette=QPalette()
        palette.setColor(QPalette.ColorRole.BrightText,color)
        self.label.setPalette(palette)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())