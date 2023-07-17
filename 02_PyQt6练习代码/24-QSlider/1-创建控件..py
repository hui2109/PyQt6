from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('创建控件的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.slider=QSlider(self)
        self.slider.valueChanged.connect(self.valueChange)
        self.slider.setGeometry(200,50,100,300)
        self.label=QLabel(self)
        self.label.setGeometry(50,50,300,100)

        # self.slider.setTickPosition(QSlider.TickPosition.TicksLeft)
        # self.slider.setTickPosition(QSlider.TickPosition.TicksRight)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)

        self.slider.setTickInterval(2)
        # self.slider.setSingleStep(10)
        self.slider.setPageStep(10)

    def valueChange(self, value):
        self.label.setText(str(value))
        self.label.adjustSize()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())