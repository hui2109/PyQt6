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
window.setWindowTitle('扁平化及默认处理')
window.resize(500,500)
window.move(200,200)

btn1=QPushButton('按钮1',window)
btn1.setFlat(True)
btn1.setStyleSheet('background-color:cyan;')

btn2=QPushButton('按钮2',window)
btn2.move(200,200)
btn2.setAutoDefault(True)
# btn2.setDefault(True)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())