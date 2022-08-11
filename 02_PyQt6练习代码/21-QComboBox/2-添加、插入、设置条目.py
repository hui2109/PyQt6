from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('添加、插入、设置条目的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        cb=QComboBox(self)
        cb.setGeometry(50,50,100,30)

        cb.addItem('Python')
        cb.addItem(QIcon('/Users/hui99563/Pictures/IMG_20190721_175831.jpg'),'C++')
        cb.addItems(['Java','C#'])

        cb.insertItem(1,'C')
        cb.insertItems(2,['C--','C#'])

        cb.setItemText(2,'C==')
        cb.setItemIcon(3,QIcon('/Users/hui99563/Pictures/IMG_20190721_175831.jpg'))
        
        cb.removeItem(2)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())