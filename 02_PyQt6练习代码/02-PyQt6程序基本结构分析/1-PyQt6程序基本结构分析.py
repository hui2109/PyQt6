# 0. 导入需要的包和模块
from PySide6.QtWidgets import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 创建控件,设置控件(大小,位置,样式...),事件,信号的处理
# 2.1 创建控件
# 当我们创建一个控件之后, 如果这个控件没有父控件, 则把它当做顶层控件(窗口)
# 系统会自动的给窗口添加一些装饰(标题栏), 窗口控件具备一些特性(设置标题,图标)
window=QWidget()
# 2.2 设置控件
window.setWindowTitle(' Hello World! ')
window.resize(600,600)
window.move(200,200)
# 控件也可以作为一个容器(承载其他的控件)
label=QLabel(window)
label.setText('Hello World')
label.move(300,300)
# 2.3 展示控件
# 刚创建好一个控件之后,(这个控件没有什么父控件), 默认情况下不会被展示,只有手动的调用show()才可以
# 如果说这个控件有父控件,那么一般情况下, 父控件展示之后, 子控件会自动展示
window.show()
# label.show()这行代码不用写

# 3. 应用程序的执行, 进入到消息循环
# 让整个程序开始执行,并且进入到消息循环(无限循环、主循环)
# 检测整个程序所接收到的用户的交互信息
# app.exec_()意思是让程序进入主循环，不要停止
sys.exit(app.exec_())
