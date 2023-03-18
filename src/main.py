from PyQt5.QtWidgets import *
from main_ui import *
from admin import *
from set import *
import sys
import openpyxl


class AdminUI(QDialog, Admin_Ui_Dialog):
    def __init__(self, parent=None):
        super(AdminUI, self).__init__(parent)
        self.setupUi(self)
        self.status = False
        self.pushButton.clicked.connect(self.get_permission)
        self.pushButton_2.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.forget_pwd)

    def closeEvent(self, event):
        if self.status:
            dia = SelfDefineUI()
            dia.exec_()
        else:
            pass

    def forget_pwd(self):
        QMessageBox.information(self, "忘记密码", "请联系软件作者", QMessageBox.Ok)

    def login(self):
        if self.check():
            QMessageBox.information(self, "登录信息", "管理员身份确认成功", QMessageBox.Ok)
            self.status = True
            self.hide()
            self.close()
        else:
            QMessageBox.critical(self, "登录信息", "管理员身份验证失败", QMessageBox.Ok)

    def get_permission(self):
        QMessageBox.information(self, "获取权限", "请联系软件作者", QMessageBox.Ok)

    def check(self):
        name = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if name == "admin" and pwd == "gwadmin":
            return True
        elif name == "Water_bros" and pwd == "114514":
            return True
        else:
            return False


class SelfDefineUI(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(SelfDefineUI, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event):
        # 关闭事件自动保存设置ini文件
        print("closed")


class MainUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action01.triggered.connect(self.import_table)
        self.action02.triggered.connect(self.export_table)
        self.action03.triggered.connect(self.show_DefineUI)
        # self.action04.triggered.connect()
        # self.action05.triggered.connect()
        # self.action06.triggered.connect()
        # self.action07.triggered.connect()
        # self.action08.triggered.connect()

        # self.pushButton.clicked.connect()
        # self.pushButton_2.clicked.connect()
        # self.pushButton_3.clicked.connect()
        # self.pushButton_4.clicked.connect()
        self.action_help.triggered.connect(self.get_help)

    def import_table(self):
        pass

    def export_table(self):
        pass

    def get_help(self):
        pass

    def show_DefineUI(self):
        adm = AdminUI()
        adm.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_ui = MainUI()
    main_ui.show()
    sys.exit(app.exec_())
