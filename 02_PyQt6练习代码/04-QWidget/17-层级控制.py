# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)
class MyWidget(QWidget):
    def mousePressEvent(self, evt):
        x=evt.pos().x()
        y=evt.pos().y()
        sub_widget=self.childAt(x,y)
        sub_widget.raise_()
# 2. 控件的操作
# 2.1 创建控件
window=MyWidget()
# 2.2 设置控件
window.setWindowTitle('层级控制')
window.resize(500,500)
window.move(200,200)

label1=QLabel(window)
label1.setText('标签1')
label1.setStyleSheet('background-color:cyan;')
label1.resize(200,200)

label2=QLabel(window)
label2.setText('标签2')
label2.resize(200,200)
label2.setStyleSheet('background-color:yellow;')
label2.move(100,100)

# label1.raise_()
# label2.lower()
# label2.stackUnder(label1)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())