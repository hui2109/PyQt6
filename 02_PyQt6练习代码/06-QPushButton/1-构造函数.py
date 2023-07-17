# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window=QWidget()
# 2.2 设置控件
window.setWindowTitle('构造函数')
window.resize(500,500)
window.move(200,200)

btn=QPushButton(QIcon('Python3/pyside6布局/PySide6练习代码/04-QWidget/7-鼠标图.png'),'按钮1',window)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())