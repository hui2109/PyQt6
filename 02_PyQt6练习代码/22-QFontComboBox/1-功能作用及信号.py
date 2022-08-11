from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('功能作用及信号的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.fcb=QFontComboBox(self)
        self.fcb.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.label=QLabel(self)
        self.label.setText('字体abc')
        self.label.setGeometry(50,50,100,100)
        self.label.setFont(QFont('SongTi SC',20))

        self.fcb.currentFontChanged.connect(self.changeFont)
    def changeFont(self,val):
        print(val.family())
        print(val.families())
        self.label.setFont(val)
        
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())