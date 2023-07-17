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
        # a=QInputDialog.getInt(self,'马上下雨了','请输入您的年龄',5
        #                     ,0,100,1)
        # print(a)

        # a=QInputDialog.getDouble(self,'xxx','请输入您的年龄',5,
        #                          0,100,2,step=3.0)
        # print(a)

        # a=QInputDialog.getText(self,'ads','请输入您的年龄',
        #                     QLineEdit.EchoMode.Normal,
        #                     inputMethodHints=
        #                     Qt.InputMethodHint.ImhDate)
        # print(a)

        # a=QInputDialog.getMultiLineText(self,'ads','请输入您的年龄',
        #                     inputMethodHints=
        #                     Qt.InputMethodHint.ImhDate)
        # print(a)

        a=QInputDialog.getItem(self,'xxx','请输入您的年龄',
                                ['男','女'],0,True,
                                inputMethodHints=
                            Qt.InputMethodHint.ImhDate)
        print(a)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())