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
window.setWindowTitle('点击')
window.resize(500,500)
window.move(200,200)

btn1=QPushButton(window)
btn1.setText('按钮1')
btn1.move(50,50)
btn1.pressed.connect(lambda:print('按钮1被点击了'))

btn2=QPushButton(window)
btn2.setText('按钮2')
btn2.move(50,100)
def click():
    btn1.animateClick()
    # btn1.click()
btn2.pressed.connect(click)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())