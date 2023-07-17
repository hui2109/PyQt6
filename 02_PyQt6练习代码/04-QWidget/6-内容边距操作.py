# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QLayout
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window=QWidget()
# 2.2 设置控件
window.setWindowTitle('内容边距操作')
window.resize(500,500)
window.move(200,200)

label=QLabel(window)
label.setText('今天也是学习的一天')
label.resize(300,300)
label.setStyleSheet("background-color:cyan;")

label.setContentsMargins(200,100,0,0)
print(label.contentsRect())
#label.getContentsMargins()方法找不到

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())