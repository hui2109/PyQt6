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
        btn_open=QPushButton('打开文件',self)
        btn_open.setGeometry(50,50,100,30)
        btn_open.clicked.connect(self.openFile)
        
        btn_save=QPushButton('保存文件',self)
        btn_save.setGeometry(200,50,100,30)
        btn_save.clicked.connect(self.saveFile)

        self.text=QTextEdit(self)
        self.text.setGeometry(50,100,400,300)

    def openFile(self):
        file_path=QFileDialog.getOpenFileName(self,'打开文件',
        '/Users/hui99563/Desktop','文本文档(*.txt)','文本文档(*.txt)',
        QFileDialog.Option.DontUseNativeDialog)[0]
        self.text.setText(open(file_path,'r',encoding='utf-8').read())
        
    def saveFile(self):
        save_path=QFileDialog.getSaveFileName(self,'保存文件',
            '/Users/hui99563/Desktop','All(*.*);;文本文档(*.txt)',
            '文本文档(*.txt)')[0]
        open(save_path,'w').write(self.text.toPlainText())

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())