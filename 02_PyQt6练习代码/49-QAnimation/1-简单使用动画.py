from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(700,700)
        self.setWindowTitle('简单使用动画的学习')
        self.move(0,0)
        self.initWidgets()
    def initWidgets(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        btn.resize(200, 200)
        btn.setStyleSheet("background-color: cyan;")

        # 1. 创建一个动画对象, 并且设置目标、属性
        # animation = QPropertyAnimation(self)
        # animation.setTargetObject(btn)
        # animation.setPropertyName(b"pos")
        animation = QPropertyAnimation(btn, b"pos", self)

        # 2. 设置属性值:开始、插值、结束
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(300, 300))

        # 3. 动画时长
        animation.setDuration(3000)

        # 4. 启动动画
        animation.start()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())