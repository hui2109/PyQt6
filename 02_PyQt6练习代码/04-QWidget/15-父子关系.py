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
window.setWindowTitle('父子关系')
window.resize(500,500)
window.move(200,200)

label1=QLabel(window)
label1.setText('标签1')

label2=QLabel(window)
label2.setText('标签2')
label2.move(100,100)

label3=QLabel(window)
label3.setText('标签3')
label3.move(150,150)

print(window.childAt(105,105))
print(label3.parentWidget())
print(window.childrenRect())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())