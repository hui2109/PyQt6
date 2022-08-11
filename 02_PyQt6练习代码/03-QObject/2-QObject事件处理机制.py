import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
# 简单的事件处理机制分为4层：
# ① 操作系统产生消息，并将消息传递到QApplication的notify方法
# ② QApplication的notify方法将消息分发到指定接受者的event方法
# ③ 接受者的event方法对evt的类型进行判定，分发到对应的具体事件方法，
#       如mousePressEvent方法
# ④ mousePressEvent方法向外发射信号，绑定信号与槽函数
class App(QApplication):
    def notify(self,receiver,evt):
        #判断receiver一定要是QPushButton
        if receiver.inherits('QPushButton') and evt.type()==QEvent.Type.MouseButtonPress:
            print(receiver,evt)
        #一定要输入return，因为父函数的notify方法有返回值
        return super().notify(receiver,evt)

app=App(sys.argv)

window=QWidget()

class Btn(QPushButton):
    def event(self,evt):
        if evt.type()==QEvent.Type.MouseButtonPress:
            print(evt)
        return super().event(evt)
    def mousePressEvent(self,evt):
        print('鼠标被按下了...')
        super().mousePressEvent(evt)
 
btn=Btn()
btn.setParent(window)
btn.setText('点击我')
btn.move(150,150)
btn.pressed.connect(lambda :print('按钮被点击了'))




window.show()
sys.exit(app.exec())



