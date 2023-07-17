from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('综合案例的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        self.cb_pro=QComboBox(self)
        self.cb_pro.setGeometry(50,50,100,100)
        self.cb_city=QComboBox(self)
        self.cb_city.setGeometry(200,50,100,100)

        self.cb_pro.currentTextChanged.connect(self.pro_changed)
        self.cb_city.currentIndexChanged.connect(self.city_changed)

        self.city_dic = {
            "北京": {
                "东城": "001",
                "西城": "002",
                "朝阳": "003",
                "丰台": "004"
            },
            "上海": {
                "黄埔": "005",
                "徐汇": "006",
                "长宁": "007",
                "静安": "008",
                "松江": "009"
            },
            "广东": {
                "广州": "010",
                "深圳": "011",
                "湛江": "012",
                "佛山": "013"
            }
        }
        self.cb_pro.addItems(self.city_dic.keys())

    def pro_changed(self,val):
        new_dict=self.city_dic[val]

        self.cb_city.blockSignals(True)
        self.cb_city.clear()
        self.cb_city.blockSignals(False)

        # self.cb_city.addItems(new_dict.keys())

        for key,value in new_dict.items():
            self.cb_city.addItem(key,value)

    def city_changed(self,val):
        print(self.cb_city.itemData(val))

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())