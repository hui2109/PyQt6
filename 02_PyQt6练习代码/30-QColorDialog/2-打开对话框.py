from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('打开对话框的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.cd=QColorDialog(self)
        
        self.cd.setOption(
            QColorDialog.ColorDialogOption.DontUseNativeDialog)
        self.cd.colorSelected.connect(self.color)

        self.cd.open()

    def color(self,color):
        print(color)
        palette=QPalette()
        # palette.setColor(QPalette.ColorRole.Window,self.cd.selectedColor())
        palette.setColor(QPalette.ColorRole.Window,color)
        # print(self.cd.selectedColor())
        self.setPalette(palette)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())