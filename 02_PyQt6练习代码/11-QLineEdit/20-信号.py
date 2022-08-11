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
        line1=QLineEdit(self)
        line1.setGeometry(10,10,150,150)
        def cao1(str):
            print('cao1',str)
        def cao2(str):
            print('cao2',str)
        def cao3():
            line2.setFocus()
        def cao4():
            print('cao4')
        def cao5():
            print(line1.selectedText())
        line1.textEdited.connect(cao1)
        line1.textChanged.connect(cao2)
        line1.setText('123')
        line1.returnPressed.connect(cao3)
        line1.editingFinished.connect(cao4)
        line1.selectionChanged.connect(cao5)
        line2=QLineEdit(self)
        line2.setGeometry(10,170,150,150)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())