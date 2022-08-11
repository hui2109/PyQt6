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
window.setWindowTitle('排他性')
window.resize(500,500)
window.move(200,200)

for i in range(3):
    cb=QCheckBox(window)
    cb.setText('checkbox'+str(i))
    cb.move(50,50+i*50)
    print(cb.isCheckable())
    print(cb.autoExclusive())
    cb.setAutoExclusive(True)
cb=QCheckBox(window)
cb.setText('checkbox')
cb.move(50,200)
# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())    