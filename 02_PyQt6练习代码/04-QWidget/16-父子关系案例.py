# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

class MyWidget(QWidget):
    def mousePressEvent(self,evt):
        print('鼠标按下了')
        x=evt.pos().x()
        y=evt.pos().y()
        sub_widget=self.childAt(x,y)
        if sub_widget is not None:
            sub_widget.setStyleSheet('background-color:cyan;')

# 2. 控件的操作
# 2.1 创建控件
window=MyWidget()
# 2.2 设置控件
window.setWindowTitle('父子关系案例')
window.resize(500,500)
window.move(200,200)

for i in range(10):
    label=QLabel(window)
    label.setText('标签'+str(i))
    label.move(30*i,30*i)
# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())