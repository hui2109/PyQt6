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
        self.btn=QPushButton(self)
        self.btn.setGeometry(50,50,150,150)
        self.btn.setText('打开字体对话框')

        self.fd=QFontDialog(self)
        self.fd.setOption(
            QFontDialog.FontDialogOption.DontUseNativeDialog)

        self.btn.clicked.connect(lambda:self.fd.open())
        
        self.fd.currentFontChanged.connect(self.font_changed)
        self.fd.fontSelected.connect(self.font_changed_new)
    def font_changed(self,val):
        print(val)
    def font_changed_new(self,val):
        print(val)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())