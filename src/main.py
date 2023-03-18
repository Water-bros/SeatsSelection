from PyQt5.QtWidgets import *
from Crypto.Cipher import AES
from PyQt5.QtCore import pyqtSignal, QThread
from main_ui import *
from admin import *
from set import *
import sys
import openpyxl
import configparser

"""
未完成：
1.配置导入导出
2.配置写入ini文件，读取ini文件
3.设置座位
2023.03.18 20.22 Water_bros
"""


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
        self.setup()
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

        self.map = []

    def setup(self):
        SetConfig("./set.dat").start()

    def import_table(self):
        file = QFileDialog.getOpenFileName(self, "导入座位表", "", "Excel Files(*.xlsx ,*.xls)")[0]
        wb = openpyxl.load_workbook(file)
        ws = wb.active
        for row in ws.values:
            row_ = []
            for i in row:
                if i:
                    row_.append(i)
            if row_:
                self.map.append(row_)
        print(self.map)

    def export_table(self):
        pass

    def get_help(self):
        pass

    def show_DefineUI(self):
        adm = AdminUI()
        adm.exec_()

    def show_table(self):
        pass


class SetConfig(QThread):
    def __init__(self, filepath, read_mode=True):
        super().__init__()
        self.path = filepath
        self.key = b"Water_bros"
        self.read_mode = read_mode
        self.config_str = ""
        self.config = configparser.ConfigParser()
        self.setup()

    def setup(self):
        if self.read_mode:
            self.ini_decrypt()
        else:
            self.ini_encrypt()

    def ini_decrypt(self):
        with open(self.path, "rb") as fn:
            t = fn.read()
            aes = AES.new(self.key, AES.MODE_ECB)
            decrypt_text = aes.decrypt(t).decode("utf-8")
            self.config.read_string(decrypt_text)

    def ini_encrypt(self):
        with open(self.path, "w", encoding="utf-8") as fn:
            self.config.write(fn)
            t = fn.read().encode("utf-8")
        with open(self.path, "wb") as fn:
            aes = AES.new(self.key, AES.MODE_ECB)
            encrypt_text = aes.encrypt(t)
            fn.write(encrypt_text)

    def read_set(self):
        secs = self.config.sections()
        for sec in secs:
            self.config.options(sec)

    def write_set(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_ui = MainUI()
    main_ui.show()
    sys.exit(app.exec_())
