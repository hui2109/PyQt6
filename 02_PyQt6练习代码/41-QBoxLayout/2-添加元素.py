from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('添加元素的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        label1=QLabel()
        label1.setStyleSheet('background-color:cyan;')
        label1.setText('标签1-cyan颜色')
        label2=QLabel()
        label2.setStyleSheet('background-color:yellow;')
        label2.setText('标签2-黄色')
        label3=QLabel()
        label3.setStyleSheet('background-color:blue;')
        label3.setText('标签3-蓝色')
        label4=QLabel()
        label4.setStyleSheet('background-color:red;')
        label4.setText('标签4-红色')
        label5=QLabel()
        label5.setStyleSheet('background-color:orange;')
        label5.setText('标签5-橙色')
        label6=QLabel()
        label6.setStyleSheet('background-color:purple;')
        label6.setText('标签6-紫色')
        label7=QLabel()
        label7.setStyleSheet('background-color:green;')
        label7.setText('标签7-绿色')
        label8=QLabel()
        label8.setStyleSheet('background-color:grey;')
        label8.setText('标签8-灰色')

        layout=QBoxLayout(QBoxLayout.Direction.LeftToRight)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)

        layout.insertWidget(1,label5)

        layout_sub=QBoxLayout(QBoxLayout.Direction.TopToBottom)
        layout.setSpacing(30)
        layout.setContentsMargins(50,50,50,50)    
        layout_sub.addWidget(label8)
        layout_sub.addWidget(label7)
        layout_sub.addWidget(label6)

        layout.insertLayout(1,layout_sub)
        # layout.removeWidget(label1)
        label1.hide()
        label1.show()

        self.setLayout(layout)
        
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())