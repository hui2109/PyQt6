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
        print(QColorDialog.customCount())
        QColorDialog.setCustomColor(1,QColor(0,255,0))
        QColorDialog.getColor(QColor(255,0,0),self,'请选择颜色',
                QColorDialog.ColorDialogOption.DontUseNativeDialog|
                QColorDialog.ColorDialogOption.ShowAlphaChannel)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())