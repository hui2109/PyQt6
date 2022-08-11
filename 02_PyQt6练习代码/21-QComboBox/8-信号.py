from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('信号的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        cb=QComboBox(self)
        cb.setGeometry(50,50,400,400)

        # 五大信号
        cb.activated.connect(self.Activated)
        cb.currentIndexChanged.connect(self.Indexchanged)
        cb.currentTextChanged.connect(self.currentTextChanged)
        cb.editTextChanged.connect(self.edittextChanged)
        cb.highlighted.connect(self.highlighted)

        cb.addItem('Python')
        cb.addItem(QIcon('/Users/hui99563/Pictures/IMG_20190721_175831.jpg'),'C++')
        cb.addItems(['Java','C#'])

        cb.setEditable(True)
        cb.setDuplicatesEnabled(True)
        cb.setFrame(True)
        cb.setIconSize(QSize(100,100))

        cb.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        cb.showPopup()

    def Activated(self,val):
        print('条目被选中了',val)
    def Indexchanged(self,val):
        print('当前选择的索引发生了改变',val)
    def currentTextChanged(self,val):
        print('当前的文本内容发生了改变',val)
    def edittextChanged(self,val):
        print('当前的文本内容再一次发生了改变',val)
    def highlighted(self,val):
        print('当前的文本内容被高亮了',val)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())