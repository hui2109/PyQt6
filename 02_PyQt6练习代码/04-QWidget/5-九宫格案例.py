# 0. 导入需要的包和模块
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window=QWidget()
# 2.2 设置控件
window.setWindowTitle('九宫格案例')
window.resize(1000,500)
window.move(200,200)
sum_width=window.width()
sum_height=window.height()

widget_count=19
widget_column_count=3
if widget_count%widget_column_count==0:
    widget_height_count=widget_count/widget_column_count
else:
    widget_height_count=widget_count//widget_column_count+1
num=0 
one_dimension_list=[]
two_dimension_list=[]
for i in range(widget_height_count):
    for j in range(widget_column_count):
        one_dimension_list.append(num)
        num+=1
    two_dimension_list.append(one_dimension_list)
    one_dimension_list=[]
    num=0
two_dimension_list[widget_height_count-1]=list(range(\
                    widget_count%widget_column_count))

for i in list(enumerate(two_dimension_list)):
    j,k=i
    for m in k:
        wi=QWidget(window)
        wi.setStyleSheet('background-color: cyan;border:\
                1px solid yellow;')
        wi.resize(int(sum_width/widget_column_count),\
                int(sum_height/widget_height_count))
        wi.move(int(m*(sum_width/widget_column_count)),\
                int(j*(sum_height/widget_height_count)))
# 2.3 展示控件
window.show()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec())