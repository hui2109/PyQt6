from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('右键菜单的学习')
        self.move(100,100)
        self.initWidgets()
    QContextMenuEvent
    def initWidgets(self):
        self.setContextMenuPolicy(Qt.ContextMenuPolicy\
                                    .CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
    def showMenu(self,point):
        QPoint
        
        path='Python3/pyside6布局/PySide6练习代码/04-QWidget/7-鼠标图.png'
        main_menu=QMenu(self)
        main_menu.setTitle('xyz')
        main_menu.setIcon(QIcon(path))

        sub_menu=QMenu(self)
        sub_menu.setTitle('123')
        sub_menu.setIcon(QIcon(path))
        ac4=QAction(QIcon(path),'Python-GUI',self)
        ac4.triggered.connect(lambda :print('打开Python-GUI'))
        sub_menu.addAction(ac4)

        ac1=QAction(QIcon(path),'新建',self)
        ac1.triggered.connect(lambda :print('新建'))
        main_menu.addAction(ac1)
        ac2=QAction(QIcon(path),'打开',self)
        ac2.triggered.connect(lambda :print('打开'))
        main_menu.addAction(ac2)
        main_menu.addMenu(sub_menu)
        main_menu.addSeparator()
        ac3=QAction(QIcon(path),'退出123',self)
        ac3.triggered.connect(lambda :print('退出'))
        main_menu.addAction(ac3)

        des_point=self.mapToGlobal(point)
        # print(main_menu.exec(des_point))
        main_menu.exec(des_point)
    def contextMenuEvent(self,event):
        QContextMenuEvent
        path='Python3/pyside6布局/PySide6练习代码/04-QWidget/7-鼠标图.png'
        main_menu=QMenu(self)
        main_menu.setTitle('xyz')
        main_menu.setIcon(QIcon(path))

        sub_menu=QMenu(self)
        sub_menu.setTitle('123')
        sub_menu.setIcon(QIcon(path))
        ac4=QAction(QIcon(path),'Python-GUI',self)
        ac4.triggered.connect(lambda :print('打开Python-GUI'))
        sub_menu.addAction(ac4)

        ac1=QAction(QIcon(path),'新建',self)
        ac1.triggered.connect(lambda :print('新建'))
        main_menu.addAction(ac1)
        ac2=QAction(QIcon(path),'打开',self)
        ac2.triggered.connect(lambda :print('打开'))
        main_menu.addAction(ac2)
        main_menu.addMenu(sub_menu)
        main_menu.addSeparator()
        ac3=QAction(QIcon(path),'退出',self)
        ac3.triggered.connect(lambda :print('退出'))
        main_menu.addAction(ac3)

        main_menu.exec(event.globalPos())

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())