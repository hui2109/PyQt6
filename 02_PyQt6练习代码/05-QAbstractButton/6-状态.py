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
window.setWindowTitle('状态')
window.resize(500,500)
window.move(200,200)

pb=QPushButton(window)
pb.setText('这是一个pushbutton')
pb.move(100,100)

rb=QRadioButton(window)
rb.setText('这是一个radiobutton')
rb.move(100,150)

cb=QCheckBox(window)
cb.setText('这是一个checkbox')
cb.move(100,200)

# pb.setDown(True)
# rb.setDown(True)
# cb.setDown(True)
print(pb.isCheckable())
print(rb.isCheckable())
print(cb.isCheckable())
pb.setCheckable(True)

pb.setChecked(True)
rb.setChecked(True)
cb.setChecked(True)
print('--------------------------------')
print(pb.isChecked())
print(rb.isChecked())
print(cb.isChecked())

btn=QPushButton(window)
btn.setText('切换')
btn.setIcon(QIcon('Python3/pyside6布局/PySide6练习代码/04-QWidget/7-鼠标图.png'))
btn.setIconSize(QSize(50,50))
def toggle1():
    pb.toggle()
    rb.toggle()
    cb.toggle()
btn.pressed.connect(toggle1)

cb.setEnabled(False)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())