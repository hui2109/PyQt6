from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('综合案例的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.slider=QSlider(self)
        self.slider.valueChanged.connect(self.valueChange)
        self.slider.setGeometry(200,50,100,300)

        self.slider.setMaximum(30)
        self.slider.setMinimum(0)
        self.slider.setTickPosition(QSlider.TickPosition.TicksLeft)
        self.slider.setTickInterval(5)

        self.label=QLabel(self)
        self.label.setStyleSheet("color: red;")

    def valueChange(self, value):
        ratio=1-self.slider.sliderPosition()/(self.slider.maximum()-\
                self.slider.minimum())
        self.label.setText(str(value))
        self.label.move(self.slider.width()/2-self.label.width()/2+\
                            self.slider.x(),
                         self.slider.y()+(self.slider.height()
                         -self.label.height())
                        *ratio
                         )
        self.label.adjustSize()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())