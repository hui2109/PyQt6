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

class Btn(QPushButton):
    def hitButton(self, point):
        center_x=self.width()/2
        center_y=self.height()/2
        hit_x=point.x()
        hit_y=point.y()
        import math
        distance = math.sqrt(math.pow(hit_x - center_x, 2) + math.pow(hit_y - center_y, 2))
        if distance<self.width()/2:
            return True
        return False
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255,255,0),1))
        painter.drawEllipse(self.rect())
btn=Btn(window)
btn.setText('点我')
# btn.setCheckable(True)
# btn.pressed.connect(lambda :print('yes'))
# btn.released.connect(lambda :print('yes'))
btn.toggled.connect(lambda value:print('yes',value))

btn.move(100,100)
btn.resize(200,200)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())