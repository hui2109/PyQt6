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
window.setWindowTitle('resize与move的学习')

#！切记resize更改的是用户界面的大小，不包括窗口框架！
#！resize有一个最小值，最小值往下就不能缩小了
# window.resize(100,100)

#move更改的是窗口框架的位置！
# window.move(200,200)
# window.setGeometry(0,0,150,150)
# 2.3 展示控件
window.show()
window.setGeometry(0,0,150,150)
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())