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
def clickcao():
    content=label.text()
    label.setText(content+'很纠结')
    label.adjustSize()

window.setWindowTitle('动态调整标签大小')
window.resize(500,500)
window.move(200,200)
window.setFixedSize(800,800)

label=QLabel(window)
label.setText('很纠结')
label.move(200,200)
label.setStyleSheet('background-color:cyan')

btn=QPushButton(window)
btn.setText('点击我')
btn.move(190,220)
btn.clicked.connect(clickcao)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())