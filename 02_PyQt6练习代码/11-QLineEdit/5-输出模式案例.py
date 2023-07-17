from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class AccountTool:
    ACCOUNT_ERROR=1
    PASSWORD_ERROR=2
    SUCCESS=0
    @staticmethod
    def check(account,password):
        if account!='admin':
            return AccountTool.ACCOUNT_ERROR
        elif password!='123456':
            return AccountTool.PASSWORD_ERROR
        else:
            return AccountTool.SUCCESS
class MyWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle('输出模式案例的学习')
        self.move(100,100)
        self.statusBar().showMessage('欢迎使用')
        self.initWidgets()
    def initWidgets(self):
        self.wighets_w=250
        self.wighets_h=40
        self.account=QLineEdit(self)
        self.account.setPlaceholderText('请输入账号')
        self.account.resize(self.wighets_w,self.wighets_h)
        self.password=QLineEdit(self)
        self.password.setPlaceholderText('请输入密码')
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.resize(self.wighets_w,self.wighets_h)
        self.login=QPushButton(self)
        self.login.setText('登    录')
        self.login.resize(self.wighets_w,self.wighets_h)
        self.login.clicked.connect(self.judge)
    def keyPressEvent(self,evt):
        if evt.key()==Qt.Key.Key_Return:
            self.judge()
        else:
            super().keyPressEvent(evt)
    def resizeEvent(self, evt):
        self.w=self.width()
        self.h=self.height()
        self.margin_beside=50
        self.margin_top=(self.height()-self.account.height()-\
            self.password.height()-self.login.height()-\
            self.margin_beside*2)/2
        self.account.move(int((self.w-self.wighets_w)/2),\
                                int(self.margin_top))
        self.password.move(int((self.w-self.wighets_w)/2),\
            self.account.y()+self.account.height()+self.margin_beside)
        self.login.move(int((self.w-self.wighets_w)/2),\
            self.password.y()+self.password.height()+self.margin_beside)
        self.setMinimumSize(self.wighets_w,self.account.height()+\
            self.password.height()+self.login.height()+\
            self.margin_beside*2)
        self.setMaximumSize(1000,700)
    def judge(self):
        if self.account.text()=='' and self.password.text()=='':
            self.statusBar().showMessage('您还未输入任何信息！')
        else:
            state=AccountTool.check(self.account.text(),self.password.text())
            if state==AccountTool.ACCOUNT_ERROR:
                self.account.setText('')
                self.password.setText('')
                self.account.setFocus()
                self.statusBar().showMessage('账号错误')
            elif state==AccountTool.PASSWORD_ERROR:
                self.password.setText('')
                self.password.setFocus()
                self.statusBar().showMessage('密码错误')
            else:
                self.statusBar().showMessage('登录成功')
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())