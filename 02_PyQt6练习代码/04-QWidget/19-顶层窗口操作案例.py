from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
class MyWidget(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("顶层窗口操作案例")
        self.resize(500,500)
        self.move(100,100)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        # 设置公共数据
        self.btn_width=50
        self.btn_height=50
        self.btn_loc_y=0
        self.initWidgets()
    def initWidgets(self):
        self.close_btn=QPushButton(self)
        self.close_btn.setText('关闭')
        self.close_btn.resize(self.btn_width,self.btn_height)

        self.max_btn=QPushButton(self)
        self.max_btn.setText('最大化')
        self.max_btn.resize(self.btn_width,self.btn_height)       

        self.min_btn=QPushButton(self)
        self.min_btn.setText('最小化')
        self.min_btn.resize(self.btn_width,self.btn_height)
        
        self.close_btn.pressed.connect(self.close)
        self.min_btn.pressed.connect(self.showMinimized)
        def max_normal():
            if self.windowState()==Qt.WindowState.WindowMaximized:
                self.showNormal()
                self.max_btn.setText('最大化')
            else:
                self.showMaximized()
                self.max_btn.setText('还原')
        self.max_btn.pressed.connect(max_normal)
    def resizeEvent(self, event):
        close_loc_x=self.width()-self.btn_width
        self.close_btn.move(close_loc_x,self.btn_loc_y)

        max_loc_x=self.close_btn.x()-self.btn_width
        self.max_btn.move(max_loc_x,self.btn_loc_y)

        min_loc_x=self.max_btn.x()-self.btn_width
        self.min_btn.move(min_loc_x,self.btn_loc_y)
    # 下面设置窗口拖拽移动
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.press_x=event.globalPosition().x()
            self.press_y=event.globalPosition().y()
            self.original_x=self.pos().x()
            self.original_y=self.pos().y()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            move_x=event.globalPosition().x()
            move_y=event.globalPosition().y()
            move_x_diff=move_x-self.press_x
            move_y_diff=move_y-self.press_y
            self.move(self.original_x+move_x_diff,\
                        self.original_y+move_y_diff)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=MyWidget()
    window.show()
    sys.exit(app.exec())