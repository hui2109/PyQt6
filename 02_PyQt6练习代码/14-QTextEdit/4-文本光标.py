from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('文本光标的学习')
        self.move(100,100)
        self.initWidgets()
    def initWidgets(self):
        text_edit=QTextEdit('要下雨了',self)
        text_edit.setGeometry(50,50,300,300)
        self.te=text_edit
        # self.inserttext()
        # self.htmltext()
        # self.imagetext()
        # self.fragmenttext()
        # self.listtext()
        # self.tabletext()
        # self.blocktext()
        self.frametext()

    # 插入文本
    def inserttext(self):
        tc=self.te.textCursor()
        tcf=QTextCharFormat()
        tcf.setToolTip('你好')
        tcf.setFontFamily('Times New Roman')
        tcf.setFontPointSize(66)
        tc.insertText('123',tcf)

    # 插入html
    def htmltext(self):
        tc=self.te.textCursor()
        tcf=QTextCharFormat()
        tcf.setToolTip('你好')
        tcf.setFontFamily('Times New Roman')
        tcf.setFontPointSize(66)
        tc.insertHtml('<a href="https://www.baidu.com">百度</a>')
    
    # 插入图片
    def imagetext(self):
        tc=self.te.textCursor()
        tif=QTextImageFormat()
        tif.setName('/Users/hui99563/Desktop/练习代码/Python3/pyside6布局/PySide6练习代码/11-QLineEdit/open.png')
        tc.insertImage(tif,QTextFrameFormat.Position.FloatRight)

    # 插入句子
    def fragmenttext(self):
        tc=self.te.textCursor()
        
        tdf2=QTextDocumentFragment.fromPlainText('qwer')
        tc.insertFragment(tdf2)

        tdf=QTextDocumentFragment.fromHtml('<h1>吃饭了</h1>')
        tc.insertFragment(tdf)

    # 插入列表
    def listtext(self):
        tc=self.te.textCursor()
        tlf=QTextListFormat()
        tlf.setIndent(3)
        tlf.setNumberPrefix('<<<')
        tlf.setNumberSuffix('>>>')
        tlf.setStyle(QTextListFormat.Style.ListDecimal)
        tl=tc.insertList(tlf)
    
    # 插入表格
    def tabletext(self):
        tc=self.te.textCursor()
        ttf=QTextTableFormat()
        ttf.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        ttf.setCellPadding(10)
        ttf.setCellSpacing(10)
        ttf.setColumnWidthConstraints([
            QTextLength(QTextLength.Type.PercentageLength,10),
            QTextLength(QTextLength.Type.PercentageLength,10),
            QTextLength(QTextLength.Type.PercentageLength,10)
                                  ])
        tc.insertTable(5,3,ttf)
    
    # 插入文本块
    def blocktext(self):
        tc=self.te.textCursor()
        tbf=QTextBlockFormat()
        tbf.setAlignment(Qt.AlignmentFlag.AlignRight)
        tbf.setRightMargin(50)
        tbf.setBottomMargin(50)
        # tbf.setTextIndent(30)
        tbf.setIndent(10)
        tcf=QTextCharFormat()
        tcf.setFontPointSize(60)
        tcf.setFontFamily('Times New Roman')
        tc.insertBlock(tbf,tcf)
    
    # 插入框架
    def frametext(self):
        tc=self.te.textCursor()
        tff=QTextFrameFormat()
        tff.setBorder(10)
        tff.setBorderBrush(QColor(255,0,0))
        tff.setRightMargin(50)
        tc.insertFrame(tff)

        doc=self.te.document()
        root_frame=doc.rootFrame()
        root_frame.setFrameFormat(tff)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())