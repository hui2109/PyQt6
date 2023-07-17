from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.cd=QColorDialog(self)        
        self.cd.setOptions(
            QColorDialog.ColorDialogOption.ShowAlphaChannel |
            QColorDialog.ColorDialogOption.DontUseNativeDialog)
        self.cd.currentColorChanged.connect(self.color)
        self.cd.show()

    def color(self,color):
        palette=QPalette()
        palette.setColor(QPalette.ColorRole.Window,color)
        self.setPalette(palette)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())