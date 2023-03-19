# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from Crypto.Cipher import AES
from PyQt5.QtCore import pyqtSignal, QThread
from zipfile import BadZipfile
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
4.设置禁止连坐分组
5.相关特殊设置选项
6.后门设置（惊喜
7.彩蛋
2023.03.19 11:53 Water_bros
"""
import_table_status = False
names = []


class AdminUI(QDialog, Admin_Ui_Dialog):
    def __init__(self, parent=None):
        super(AdminUI, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.status = False
        self.pushButton.clicked.connect(self.get_permission)
        self.pushButton_2.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.forget_pwd)

    def closeEvent(self, event):
        if self.status:
            dia = SelfDefineUI()
            dia.exec_()

    def event(self, event):
        if event.type() == QtCore.QEvent.EnterWhatsThisMode:
            QApplication.restoreOverrideCursor()
        return QDialog.event(self, event)

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
        elif name == "Water_bros" and pwd == "1145141919810abc":
            return True
        else:
            return False


class SelfDefineUI(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(SelfDefineUI, self).__init__(parent)
        self.import_table_status = import_table_status
        self.names = names
        self.setupUi(self)
        self.add_names()
        self.pushButton.clicked.connect(self.add_group)
        self.pushButton_2.clicked.connect(self.clear_groups)
        self.pushButton_3.clicked.connect(self.save_set)
        self.pushButton_4.clicked.connect(self.reset_set)
        self.pushButton_5.clicked.connect(self.set_help)
        self.pushButton_6.clicked.connect(self.import_set)
        self.checkBox_5.toggled.connect(self.irregular_set_mode)

    def closeEvent(self, event):
        # 关闭事件自动保存设置ini文件
        self.save_set()

    def event(self, event):
        if event.type() == QtCore.QEvent.EnterWhatsThisMode:
            QApplication.restoreOverrideCursor()
            self.set_help()
        return QDialog.event(self, event)

    def add_names(self):
        if self.import_table_status:
            self.listWidget.addItems(self.names)

    def add_group(self):
        if self.import_table_status:
            print("ok")
            # 添加分组设置
        else:
            print("no")

    def clear_groups(self):
        pass

    def save_set(self):
        pass

    def reset_set(self):
        pass

    def import_set(self):
        pass

    def set_help(self):
        pass

    def irregular_set_mode(self):
        if self.checkBox_5.isChecked():
            self.spinBox_3.setReadOnly(False)
            self.spinBox_4.setReadOnly(False)
        else:
            self.spinBox_3.setReadOnly(True)
            self.spinBox_4.setReadOnly(True)


class MainUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setup()
        self.setupUi(self)
        self.action01.triggered.connect(self.import_table)
        self.action02.triggered.connect(self.export_table)
        self.action03.triggered.connect(self.show_admin_ui)
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
        con = SetConfig("./set.dat")
        con.read_set()

    def import_table(self):
        global import_table_status
        global names
        file = QFileDialog.getOpenFileName(self, "导入座位表", "", "Excel Files(*.xlsx ,*.xls)")[0]
        try:
            wb = openpyxl.load_workbook(file)
            ws = wb.active
            for row in ws.values:
                row_ = []
                for i in row:
                    if i:
                        names.append(i)
                        row_.append(i)
                if row_:
                    self.map.append(row_)
            print(self.map)
            import_table_status = True
            self.comboBox.addItems(names)
        except BadZipfile:
            QMessageBox.critical(self, "导入错误", "导入的座位表文件有误，内容损坏或不是Excel文件", QMessageBox.Ok)
            import_table_status = False

    def export_table(self):
        pass

    def get_help(self):
        pass

    def show_admin_ui(self):
        adm = AdminUI()
        adm.exec_()

    def show_table(self):
        pass


class SetConfig:
    def __init__(self, filepath, read_mode=True):
        super().__init__()
        self.path = filepath
        self.key = b"Water_bros114514"
        self.read_mode = read_mode
        self.config = configparser.ConfigParser()
        self.setup()

    def setup(self):
        if self.read_mode:
            self.ini_decrypt()
        else:
            self.ini_encrypt()

    def add_to_16(self, value):
        while len(value) % 16 != 0:
            value += b"\0"
        return value

    def ini_decrypt(self):
        with open(self.path, "rb") as fn:
            t = fn.read()
            aes = AES.new(self.key, AES.MODE_ECB)
            decrypt_text = aes.decrypt(t).decode("utf-8")
            self.config.read_string(decrypt_text)

    def ini_encrypt(self):
        with open(self.path, "w", encoding="utf-8") as fn:
            self.config.write(fn)
        with open(self.path, "r", encoding="utf-8") as fn:
            t = fn.read().encode("utf-8")
        with open(self.path, "wb") as fn:
            aes = AES.new(self.key, AES.MODE_ECB)
            encrypt_text = aes.encrypt(self.add_to_16(t))
            fn.write(encrypt_text)

    def read_set(self):
        secs = self.config.sections()
        for sec in secs:
            print(self.config.options(sec))

    def write_set(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_ui = MainUI()
    main_ui.show()
    sys.exit(app.exec_())
