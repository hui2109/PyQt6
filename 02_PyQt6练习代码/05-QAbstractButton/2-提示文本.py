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
window.setWindowTitle('提示文本')
window.resize(500,500)
window.move(200,200)

btn=QPushButton(window)
btn.setText('1')
def plus_one():
    print("点击了加一")
    num=int(btn.text())+1
    btn.setText(str(num))
btn.pressed.connect(plus_one)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())