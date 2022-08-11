import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
app=QApplication(sys.argv)
class MyWindow(QWidget):
    def mouseMoveEvent(self, event):
        # print(event.globalPosition())
        print(event.pos())
        
window=MyWindow()
window.setMouseTracking(True)
print(window.hasMouseTracking())

window.show()
sys.exit(app.exec())