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
window.setWindowTitle('鼠标相关操作')
window.resize(500,500)
window.move(200,200)

# 设置鼠标形状
# window.setCursor(Qt.CursorShape.BusyCursor)
# label=QLabel(window)
# label.setStyleSheet('background-color:cyan;')
# label.setText('豆腐块结构简单')
# label.resize(300,300)
# label.setCursor(Qt.CursorShape.BusyCursor)

# 自定义鼠标形状
# 注意这里有坑，PyQt6默认是去你的工程目录下寻找图片！
pixmap=QPixmap('./Python3/pyside6布局/PySide6练习代码/04-QWidget/7-鼠标图.png')
new_pixmap=pixmap.scaled(50,50)
cursor=QCursor(new_pixmap,20,20)
window.setCursor(cursor)

#获取鼠标对象
cursor1=window.cursor()
cursor1.setPos(100,100)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())