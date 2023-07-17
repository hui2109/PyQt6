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
        self.kse=QKeySequenceEdit(self)

        # ks=QKeySequence('Ctrl+Q')
        # ks=QKeySequence(QKeySequence.StandardKey.Copy)
        # ks=QKeySequence(Qt.KeyboardModifier.ControlModifier|Qt.Key.Key_C)
        # ks=QKeySequence.fromString('Ctrl+C')
        # self.kse.setKeySequence(ks)

        # self.kse.setKeySequence('Ctrl+C')

        # self.kse.setKeySequence(QKeySequence.StandardKey.Copy)

        # self.kse.setKeySequence(Qt.Key.Key_C)
        btn=QPushButton(self)
        btn.setGeometry(100,100,100,100)
        btn.clicked.connect(lambda :print(self.kse.keySequence().toString(),self.kse.keySequence().count()))

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())