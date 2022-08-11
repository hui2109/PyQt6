# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

# 1. 创建一个应用程序对象
class MyWidget(QWidget):
    def mousePressEvent(self, evt):
        print(self.focusWidget())
        # self.focusNextChild()
        # self.focusPreviousChild()
        self.focusNextPrevChild(False)
        
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window=MyWidget()
# 2.2 设置控件
window.setWindowTitle('焦点控制')
window.resize(500,500)
window.move(200,200)

line1=QLineEdit(window)
line1.move(100,100)
line2=QLineEdit(window)
line2.move(100,150)
line3=QLineEdit(window)
line3.move(100,200)
line4=QLineEdit(window)
line4.move(100,250)
line5=QLineEdit(window)
line5.move(100,300)
line6=QLineEdit(window)
line6.move(100,350)

# line2.setFocus()
# line2.clearFocus()

# line3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

MyWidget.setTabOrder(line2,line6)
MyWidget.setTabOrder(line6,line1)
MyWidget.setTabOrder(line1,line4)
# MyWidget.setTabOrder(line5,line3)
# MyWidget.setTabOrder(line3,line4)


print(window.focusWidget()) # 不能得到执行

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())
