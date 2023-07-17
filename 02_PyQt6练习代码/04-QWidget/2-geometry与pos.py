# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window=QWidget()
# 2.2 设置控件
window.setWindowTitle('geometry与pos的学习')
window.resize(500,500)
window.move(200,200)

print(window.x())
print(window.y())
print('------------------------------------------------')
print(window.geometry())


# 2.3 展示控件
window.show()

#注意: 控件显示完毕之后, 具体的位置或者尺寸数据才会正确
print(window.x())
print(window.y())
print('------------------------------------------------')
print(window.geometry())
print(window.frameGeometry())

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())