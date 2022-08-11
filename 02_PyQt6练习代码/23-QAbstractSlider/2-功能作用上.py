from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('功能作用上的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.slider=QSlider(self)
        self.slider.valueChanged.connect(self.valueChange)

        self.label=QLabel(self)
        self.label.setGeometry(50,50,100,100)

        self.slider.setMaximum(100)
        self.slider.setMinimum(10)

        self.slider.setValue(50)

        self.slider.setSingleStep(10)

    def valueChange(self,val):
        self.label.setText(str(val))
        self.label.adjustSize()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())