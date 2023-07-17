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
        self.btn=QPushButton(self)
        self.btn.setGeometry(50,50,150,150)
        self.btn.setText('打开字体对话框')
        self.btn.clicked.connect(self.btn_font)

    def btn_font(self):
        # a=QFontDialog.getFont(self)
        a=QFontDialog.getFont(QFont(),self,'请选择字体',
            QFontDialog.FontDialogOption.DontUseNativeDialog)
        print(a)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())