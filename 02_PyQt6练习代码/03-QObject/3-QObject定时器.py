# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)
class Mytimer(QObject):
    #参数evt代表定时器事件
    def timerEvent(self,evt):
        print(evt,1)
    
# 2. 控件的操作
# 2.1 创建控件
window=QWidget()
# 2.2 设置控件
window.setWindowTitle('QObject定时器学习')
window.resize(500,500)
window.move(200,200)

obj=Mytimer()
timer_id=obj.startTimer(1000)
print(timer_id)
# obj.killTimer(timer_id)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())