# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window=QMainWindow()
# 2.2 设置控件
window.setWindowTitle('信息提示')
window.resize(500,500)
window.move(200,200)
window.statusBar()
window.setStatusTip('这是窗口')
window.setWindowFlags(Qt.WindowType.WindowContextHelpButtonHint)

label=QLabel(window)
label.setText('这是标签')
label.setToolTip('今天天气不好')
label.setToolTipDuration(1000)

label.setWhatsThis('这是啥？')

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())