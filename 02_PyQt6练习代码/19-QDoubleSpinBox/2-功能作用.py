from PyQt6.QtWidgets import *


class MyDoubleSpinBox(QDoubleSpinBox):
    def textFromValue(self, value):
        return str(value) + '元'


def valueChanged(val):
    print(val)


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('功能作用的学习')
        self.move(100, 100)
        self.initWidgets()

    def initWidgets(self):
        dsb = MyDoubleSpinBox(self)
        dsb.setGeometry(50, 50, 100, 30)
        dsb.setDecimals(4)
        dsb.setRange(1.0000, 50.0000)
        dsb.setSingleStep(1)
        dsb.setWrapping(True)

        dsb.setPrefix('$')
        dsb.setSuffix('%')

        dsb.setSpecialValueText('这是最小值')
        dsb.setValue(10.00009)
        print(dsb.value(), type(dsb.value()))
        print(dsb.cleanText(), type(dsb.cleanText()))

        dsb.valueChanged.connect(valueChanged)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
