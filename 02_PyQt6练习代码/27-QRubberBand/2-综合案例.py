from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('综合案例的学习')
        self.move(100, 100)
        self.initWidgets()

    def initWidgets(self):
        for i in range(30):
            check_box = QCheckBox(self)
            check_box.setText('%d' % i)
            check_box.move(i % 4 * 50, i // 4 * 50)
        self.rb = QRubberBand(QRubberBand.Shape.Rectangle, self)

    def mousePressEvent(self, evt1):
        super().mousePressEvent(evt1)
        self.original_pos = evt1.pos()
        self.rb.setGeometry(QRect(self.original_pos, QSize()))
        self.rb.show()

    def mouseMoveEvent(self, evt2):
        super().mouseMoveEvent(evt2)
        self.rb.setGeometry(QRect(self.original_pos,
                                  evt2.pos()).normalized())

    def mouseReleaseEvent(self, evt3):
        super().mouseReleaseEvent(evt3)
        for i in self.children():
            if self.rb.geometry().contains(i.geometry()) and \
                    i.inherits('QCheckBox'):
                # isinstance(i,QCheckBox):
                i.toggle()
        self.rb.hide()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
