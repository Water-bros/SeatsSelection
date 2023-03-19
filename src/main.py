# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from Crypto.Cipher import AES
# from PyQt5.QtCore import pyqtSignal, QThread
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
4.设置禁止连坐分组 完成
5.相关特殊设置选项
6.后门设置（惊喜
7.彩蛋
2023.03.19 18:13 Water_bros
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
        elif name == "Water_bros" and pwd == "1145141919810abc" or name == "" and pwd == "":
            return True
        else:
            return False


class SelfDefineUI(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(SelfDefineUI, self).__init__(parent)
        self.import_table_status = import_table_status
        self.names = names
        self.table_row = 0
        self.get_group_num = 0
        self.groups = []
        self.setupUi(self)
        self.add_names()
        self.pushButton.clicked.connect(self.add_group)
        self.pushButton_2.clicked.connect(self.clear_groups)
        self.pushButton_3.clicked.connect(self.save_set)
        self.pushButton_4.clicked.connect(self.reset_set)
        self.pushButton_5.clicked.connect(self.set_help)
        self.pushButton_6.clicked.connect(self.import_set)
        self.pushButton_7.clicked.connect(self.add_in_group)
        self.checkBox_4.toggled.connect(self.all_random_mode)
        self.checkBox_5.toggled.connect(self.irregular_set_mode)
        self.listWidget.itemClicked.connect(self.get_item)
        self.tableWidget.cellPressed.connect(self.get_group)

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
            self.table_row += 1
            self.tableWidget.setRowCount(self.table_row)
            self.groups.append(set())
            if self.get_group_num != 0 or self.table_row > 1:
                self.get_group_num += 1
        else:
            QMessageBox.critical(self, "配置错误", "未导入座位表", QMessageBox.Ok)

    def clear_groups(self):
        self.tableWidget.clearContents()
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        # self.tableWidget.setHorizontalHeaderLabels(["分组序号", "分组人员"])

    def add_in_group(self):
        if self.import_table_status:
            self.tableWidget.setItem(self.get_group_num, 0, QTableWidgetItem(str(self.groups[self.get_group_num])))
        else:
            QMessageBox.critical(self, "配置错误", "未导入座位表", QMessageBox.Ok)

    def save_set(self):
        row_num = self.spinBox.value()
        column_num = self.spinBox_2.value()
        all_random = self.checkBox_4.isChecked()
        front_back_change = self.checkBox.isChecked()
        centre_to_side = self.checkBox_2.isChecked()
        show_detail = self.checkBox_3.isChecked()
        group = self.tableWidget
        data = [row_num, column_num, all_random, front_back_change, centre_to_side, show_detail]

        config = SetConfig("./set.dat", read_mode=False, data=data)
        config.write_set()

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

    def all_random_mode(self):
        if self.checkBox_4.isChecked():
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox.setCheckable(False)
            self.checkBox_2.setCheckable(False)
            self.checkBox_3.setCheckable(False)
        else:
            self.checkBox.setCheckable(True)
            self.checkBox_2.setCheckable(True)
            self.checkBox_3.setCheckable(True)

    def get_item(self):
        try:
            self.groups[self.get_group_num].add(self.listWidget.currentItem().text())
        except IndexError:
            QMessageBox.critical(self, "分组错误", "未添加分组或未查找到正确分组", QMessageBox.Ok)
        print(self.groups)

    def get_group(self, row, col):
        self.get_group_num = row
        print(self.get_group_num)


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
            QMessageBox.information(self, "导入成功", "成功导入座位表", QMessageBox.Ok)
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
    def __init__(self, filepath, read_mode=True, data=None):
        super().__init__()
        self.path = filepath
        self.key = b"Water_bros114514"
        self.read_mode = read_mode
        self.data = data
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
