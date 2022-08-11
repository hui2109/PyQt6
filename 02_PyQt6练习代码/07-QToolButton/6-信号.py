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
window.setWindowTitle('信号')
window.resize(500,500)
window.move(200,200)

path='Python3/pyside6布局/PySide6练习代码/04-QWidget/7-鼠标图.png'
main_menu=QMenu(window)
main_menu.setTitle('xyz')
main_menu.setIcon(QIcon(path))

sub_menu=QMenu(window)
sub_menu.setTitle('123')
sub_menu.setIcon(QIcon(path))
ac4=QAction(QIcon(path),'Python-GUI',window)
ac4.triggered.connect(lambda :print('打开Python-GUI'))
sub_menu.addAction(ac4)

ac1=QAction(QIcon(path),'新建',window)
ac1.triggered.connect(lambda :print('新建'))
ac1.setData('qwer')
main_menu.addAction(ac1)
ac2=QAction(QIcon(path),'打开',window)
ac2.triggered.connect(lambda :print('打开'))
main_menu.addAction(ac2)
main_menu.addMenu(sub_menu)
main_menu.addSeparator()
ac3=QAction(QIcon(path),'退出',window)
ac3.triggered.connect(lambda :print('退出'))
main_menu.addAction(ac3)

btn=QToolButton(window)
btn.setText('菜单123')
btn.setMenu(main_menu)
btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
btn.setArrowType(Qt.ArrowType.RightArrow)
btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

def cao(action):
    print('123',action.data())
btn.triggered.connect(cao)

# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())