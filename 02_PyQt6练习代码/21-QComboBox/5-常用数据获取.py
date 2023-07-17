from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('常用数据获取的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        cb=QComboBox(self)
        cb.setGeometry(50,50,400,400)

        cb.addItem('Python')
        cb.addItem(QIcon("/Users/hui99563/Pictures/"+
            "IMG_20190721_175831.jpg"),'C++')
        cb.addItems(['Java','C#'])

        print(cb.count())
        print(cb.currentIndex())
        print(cb.currentText())



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())