from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('设置模型的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        cb=QComboBox(self)
        cb.setGeometry(50,50,400,400)

        # print(QAbstractItemModel.__subclasses__())

        model=QStandardItemModel(self)

        item1=QStandardItem('item1')
        item2=QStandardItem('item2')
        item22=QStandardItem('item22')
        item11=QStandardItem('item11')
        item1.appendRow(item11)
        item2.appendRow(item22)

        model.appendRow(item1)
        model.appendRow(item2)
        # model.appendRow(item22)
        # model.appendRow(item11)

        cb.setModel(model)
        cb.setView(QTreeView(self))
        # print(QAbstractItemView.__subclasses__())

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())