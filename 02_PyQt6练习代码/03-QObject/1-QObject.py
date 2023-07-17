from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500, 500)
        self.setWindowTitle('QObject的学习')
        self.move(300, 300)
        self.initWidgets()
    def initWidgets(self):
        # self.show_parent()
        # self.show_name_property()
        # self.show_qss_style()
        self.show_two_method_set_parent()
        # self.signal_and_cao()
        # self.case1()
        # self.case2()
        # self.widget_type_judge()
        # self.widget_type_judge_case()
        # self.delete_widget()

    def show_parent(self):
        a = QLabel.mro()
        for i in a:
            print(i)

    def show_name_property(self):
        obj = QObject()

        obj.setObjectName('nice')
        print(obj.objectName())
        obj.setProperty('nice1', 'qwe')
        obj.setProperty('nice2', 'rty')
        print(obj.property('nice1'))

        print(obj.dynamicPropertyNames())

    def show_qss_style(self):
        label1 = QLabel(self)
        label1.setText('今天你吃饭了吗')
        label1.setObjectName("notice")
        label1.setProperty("notice_level", "warning")

        label2 = QLabel(self)
        label2.move(200, 200)
        label2.setText('今天我吃饭了')
        label2.setObjectName("notice")
        label2.setProperty("notice_level", "error")

        pushbn = QPushButton(self)
        pushbn.setText('这是一个按钮')
        pushbn.move(300, 300)

        # label3要求不能应用样式
        label3 = QLabel(self)
        label3.setText('我不能设置样式')
        label3.move(100, 450)

    def show_two_method_set_parent(self):
        #方法一
        label1=QLabel(self)
        label1.setText('label1')

        #方法二
        label2=QLabel()
        label2.setText('label2')
        label2.move(100,100)
        label2.setParent(self)

        label3=QLabel(self)
        label3.setText('label3')
        label3.move(200,200)

        btn=QPushButton()
        btn.setText('btn')
        btn.move(300,300)
        btn.setParent(self)

        #为QWidget组件中的所有QLabel设置背景颜色
        for i in self.findChildren(QLabel):
            i.setStyleSheet('background-color:cyan')

    def signal_and_cao(self):
        self.obj=QObject()
        #示范destyoyed信号
        def destroy_cao(obj1):
            print('对象被释放了',obj1)
        self.obj.destroyed.connect(destroy_cao)
        # del self.obj

        #示范objectNameChanged信号
        def change_name(name):
            print('对象名称发生了改变',name)
        self.obj.objectNameChanged.connect(change_name)
        print(self.obj.signalsBlocked())
        self.obj.setObjectName('xxx')
        #disconnect只是取消了链接，但信号还是发射了的，只是没有槽来接受它
        # self.obj.objectNameChanged.disconnect()
        self.obj.setObjectName('ooo')
        #block临时阻断链接
        #signalsBlocked判断信号是否被阻断
        #receivers判断连接到信号的槽的数量
        self.obj.blockSignals(False)
        print(self.obj.signalsBlocked())
        self.obj.setObjectName('xxoo')
        print(self.obj.receivers(self.obj.objectNameChanged))

        #绑定两个槽函数
        def change_name2(name):
            print('对象名称发生了改变2',name)
        self.obj.objectNameChanged.connect(change_name2)
        print(self.obj.receivers(self.obj.objectNameChanged))
        self.obj.setObjectName('xxxooo')

    def case1(self):
        btn=QPushButton(self)
        btn.setText('点击我')
        def click():
            print('点我嘎哈！')
        btn.clicked.connect(click)

    def case2(self):
        #绑定窗口标题变化的信号与槽
        pass

    def widget_type_judge(self):
        obj=QObject()
        wg=QWidget()
        bn=QPushButton()
        label=QLabel()
        objs=[obj,wg,bn,label]
        for i in objs:
            print(i.isWidgetType())
            print(i.inherits('QPushButton'))
            print('-----------------------') 

    def widget_type_judge_case(self):
        label1=QLabel(self)
        label2=QLabel(self)
        btn=QPushButton(self)
        label1.setText('今天你吃饭了吗？')
        label2.setText('今天我吃饭了')
        btn.setText('这是一个按钮')
        label1.move(100,100)
        label2.move(200,200)
        btn.move(300,300)
        #开始给标签控件设置样式，有两种方式：
        #方式一：使用findchildren方法
        # for i in self.findChildren(QLabel):
        #     print(i)
        #方式二：使用inherits方法
        for i in self.children():
            if i.inherits('QLabel'):
                i.setStyleSheet('background-color:cyan;')

    def delete_widget(self):
        obj1=QObject()
        obj2=QObject()
        obj3=QObject()

        #为了避免obj1被自动释放，引用一下obj1
        self.obj=obj1

        #设置父子关系
        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda :print('obj1被释放了'))
        obj2.destroyed.connect(lambda :print('obj2被释放了'))
        obj3.destroyed.connect(lambda :print('obj3被释放了'))

        #使用del命令只是删除了obj2的指针，但它还是被obj1引用
        # del obj2
        # print(obj1.findChildren(QObject))

        #deleteLater()并没有将对象立即销毁，
        # 而是向主消息循环发送了一个event，
        # 下一次主消息循环收到这个event之后才会销毁对象
        obj2.deleteLater()
        print(obj1.findChildren(QObject))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    style_path = '/Users/hui99563/Documents/01. 编程学习/python/python_code/PyQt6布局/PyQt6练习代码/03-QObject/4-QObject.qss'
    with open(style_path, 'r', True) as f:
        app.setStyleSheet(f.read())
    window = Window()
    #绑定窗口标题变化的信号与槽
    def change_windowtitle(title):
        #先断开连接，以免反复迭代
        # window.windowTitleChanged.disconnect(change_windowtitle)
        window.blockSignals(True)
        window.setWindowTitle('撩课-'+title)
        #再恢复连接
        # window.windowTitleChanged.connect(change_windowtitle)
        window.blockSignals(False)
    window.windowTitleChanged.connect(change_windowtitle)
    window.setWindowTitle('开心')
    window.setWindowTitle('幸福')
    window.setWindowTitle('兴奋')
    window.show()
    sys.exit(app.exec())
