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
window.setWindowTitle('交互状态[*]')
window.resize(500,500)
window.move(200,200)

window.setWindowModified(True)

btn=QPushButton(window)
btn.setText('按钮1')

# btn.setVisible(False)
# btn.setHidden(True)
# btn.hide()
btn.setEnabled(False)
# setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)需要写在前面
btn.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
# btn.close()

btn.destroyed.connect(lambda :print('xxx'))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())