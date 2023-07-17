# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)
class MyWidget(QWidget):
    def mousePressEvent(self, evt):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
# 2. 控件的操作
# 2.1 创建控件
window=MyWidget()
# 2.2 设置控件
window.setWindowTitle('顶层窗口操作')
window.resize(500,500)
window.move(200,200)

icon=QIcon('/Users/hui99563/Desktop/练习代码/Python3/pyside6布局\
            /PySide6练习代码/04-QWidget/7-鼠标图.png')
window.setWindowIcon(icon)

window.setWindowOpacity(1)

print(window.windowState()==\
    Qt.WindowState.WindowNoState)

# window.setWindowState(Qt.WindowState.WindowMinimized)
# window.setWindowState(Qt.WindowState.WindowMaximized)
# window.setWindowState(Qt.WindowState.WindowFullScreen)
# w2=QWidget()
# w2.setWindowTitle('w2')
window.setWindowFlags(Qt.WindowType.WindowMinMaxButtonsHint)

# 2.3 展示控件
window.show()
# w2.show()
window.setWindowState(Qt.WindowState.WindowActive)

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())