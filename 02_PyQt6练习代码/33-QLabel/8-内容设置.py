from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('内容设置的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label=QLabel(self)
        label.setGeometry(50,50,100,100)

        label.setText("<img src='PyQt6布局/PyQt6练习代码/04-QWidget/7-鼠标图.png' width=100 height=100>")
        label.setNum(888.89)

        picture=QPicture()
        painter=QPainter(picture)
        painter.setBrush(QColor(200,0,0))
        painter.drawEllipse(0,0,90,90)
        label.setPicture(picture)

        movie=QMovie('/Users/hui99563/Documents/01. 编程学习/python/书籍及资料/pyqt5资料/PyQt5学习课件/05. Gif_Resource/QCalendarWidget.gif')
        label.setMovie(movie)
        movie.start()
        label.adjustSize()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())