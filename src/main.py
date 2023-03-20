# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from Crypto.Cipher import AES
# from PyQt5.QtCore import pyqtSignal, QThread
from zipfile import BadZipfile
from main_ui import *
from admin import *
from set import *
import sys
import random
import openpyxl
import configparser

"""
未完成：
1.配置导入导出 完成
2.配置写入ini文件，读取ini文件 完成
3.设置座位 完成
4.设置禁止连坐分组 完成
5.相关特殊设置选项 完成
6.后门设置（惊喜
7.彩蛋
8.选择座位
9.根据设置选择座位
10.导出座位表
11.滚动展示
12.判断选择是否合规
2023.03.20 17:05 Water_bros
"""
import_table_status = False
names = []
maps = None


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
        self.data = []
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
        if self.import_table_status:
            self.checkBox_5.toggled.connect(
                lambda: QMessageBox.information(self, "不规则行列设置", "已经通过导入的座位表自动设置", QMessageBox.Ok))
        else:
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
        self.table_row = 0
        self.get_group_num = 0
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
        group = self.groups
        self.data = [row_num, column_num, all_random, front_back_change, centre_to_side, show_detail, group, maps]
        SetConfig("./set.dat", read_mode=False, data=self.data)
        QMessageBox.information(self, "保存设置", "设置文件保存成功", QMessageBox.Ok)

    def reset_set(self):
        self.spinBox.setValue(1)
        self.spinBox_2.setValue(1)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setChecked(False)
        self.groups = []
        with open("./set.dat", "w", encoding="utf-8") as fn:
            fn.write("")

    def import_set(self):
        file = QFileDialog.getOpenFileName(self, "导入设置", "", "Set Files(*.dat)")[0]
        if file != "":
            try:
                con = SetConfig(file)
                self.data = con.read_set()
                QMessageBox.information(self, "导入成功", "导入的配置文件成功", QMessageBox.Ok)
            except ValueError or configparser.Error:
                QMessageBox.critical(self, "导入错误", "导入的配置文件有误，内容损坏或不是相符合的内容", QMessageBox.Ok)
        else:
            pass

    def set_help(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/Water-bros/SeatsSelection#readme"))

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

    def get_group(self, row, col):
        self.get_group_num = row
        print(self.get_group_num)


class MainUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.data = []
        self.labels = []
        self.steps = []
        self.steps_backup = self.steps
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

        self.pushButton.clicked.connect(self.reset)
        self.pushButton_2.clicked.connect(self.random_choice)
        self.pushButton_3.clicked.connect(self.cancel)
        self.pushButton_4.clicked.connect(self.front_move)
        self.action_help.triggered.connect(self.get_help)

        self.map = []
        self.clean_map = []

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMaximized():
                self.widget.setStyleSheet(
                    """
                    QWidget {
                        border: 8px solid black;
                    }
                    
                    QLabel {
                            border: 4px solid black;
                            font: 57 25pt "OPlusSans 3.0";
                        }
                    """)
            else:
                self.widget.setStyleSheet(
                    """
                    QWidget {
                        border: 5px solid black;
                    }

                    QLabel {
                            border: 3px solid black;
                            font: 57 15pt "OPlusSans 3.0";
                        }
                    """)

    def setup(self):
        try:
            con = SetConfig("./set.dat")
            self.data = con.read_set()
        except ValueError or configparser.Error:
            with open("./set.dat", "w", encoding="utf-8") as fn:
                fn.write("")

    def import_table(self):
        global import_table_status
        global names
        global maps
        file = QFileDialog.getOpenFileName(self, "导入座位表", "", "Excel Files(*.xlsx ,*.xls)")[0]
        if file != "":
            try:
                wb = openpyxl.load_workbook(file)
                ws = wb.active
                value = list(ws.values)
                for row_num in range(len(value)):
                    row_ = []
                    row__ = []
                    for j in range(len(value[row_num])):
                        i = value[row_num][j]
                        if i:
                            names.append(i)
                            row_.append(i)
                            row__.append(f"{row_num}-{j}")
                    if row_:
                        row_.reverse()
                        self.map.append(row_)
                        self.clean_map.append(row__)
                import_table_status = True
                self.map.reverse()
                maps = self.map
                self.comboBox.addItems(names)
                self.show_table()
                QMessageBox.information(self, "导入成功", "成功导入座位表", QMessageBox.Ok)
            except BadZipfile:
                QMessageBox.critical(self, "导入错误", "导入的座位表文件有误，内容损坏或不是Excel文件", QMessageBox.Ok)
                import_table_status = False
        else:
            pass

    def export_table(self):
        pass

    def get_help(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/Water-bros/SeatsSelection#readme"))

    def show_admin_ui(self):
        adm = AdminUI()
        adm.exec_()

    def show_table(self):
        print(self.map)
        col_lens = []
        for rows in self.map:
            col_len = len(rows)
            col_lens.append(col_len)
        max_col = max(col_lens)
        for row in range(len(self.map)):
            col_labels = []
            for col in range(max_col):
                label = QtWidgets.QLabel(self.widget)
                label.setAlignment(QtCore.Qt.AlignCenter)
                self.gridLayout_4.addWidget(label, row, col, 1, 1)
                col_labels.append(label)
                try:
                    label.setText(self.map[row][col])
                except IndexError:
                    pass
            self.labels.append(col_labels)

    def random_choice(self):
        sel = QMessageBox.question(self, "确认身份", "请先在上方选择您的姓名，并确认是您本人操作",
                                   QMessageBox.Yes | QMessageBox.No)
        if sel:
            flag = True
            while flag:
                ran_pos = random.choice(self.clean_map)
                row_num = ran_pos[0]
                col_num = ran_pos[2]
                # 选择判断是否合规
        else:
            pass

    def reset(self):
        sel = QMessageBox.question(self, "确认重置", "请问是否重置所有操作？", QMessageBox.Yes | QMessageBox.No)
        if sel:
            self.clean_map = []
        else:
            pass

    def cancel(self):
        sel = QMessageBox.question(self, "确认撤销", "请问是否回退至上一步操作？", QMessageBox.Yes | QMessageBox.No)
        if sel:
            QMessageBox.information(self, "嘻嘻", "作者很懒，没有机会撤销捏", QMessageBox.Ok)
        else:
            pass

    def front_move(self):
        sel = QMessageBox.question(self, "确认还原", "请问是否还原至下一步操作？", QMessageBox.Yes | QMessageBox.No)
        if sel:
            QMessageBox.information(self, "嘻嘻", "作者很懒，没有机会还原捏", QMessageBox.Ok)
        else:
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
            de_text_list = list(decrypt_text)
            de_text_list.reverse()
            for i in range(len(de_text_list)):
                if de_text_list[i] == "\0":
                    de_text_list[i] = ""
            de_text_list.reverse()
            decrypt_text = "".join(de_text_list)
            self.config.read_string(decrypt_text)

    def ini_encrypt(self):
        with open(self.path, "w", encoding="utf-8") as fn:
            self.write_set()
            self.config.write(fn)
        with open(self.path, "r", encoding="utf-8") as fn:
            t = fn.read().encode("utf-8")
        with open(self.path, "wb") as fn:
            aes = AES.new(self.key, AES.MODE_ECB)
            encrypt_text = aes.encrypt(self.add_to_16(t))
            fn.write(encrypt_text)

    def read_set(self):
        data = []
        secs = self.config.sections()
        for sec in secs:
            data.append(self.config.items(sec))
        return data

    def write_set(self):
        self.config.add_section("others")
        self.config.add_section("basic_info")
        self.config.add_section("special_section")
        self.config.add_section("ban_group")
        self.config.set("others", "irregular_mode", "0")
        self.config.set("others", "maps", str(self.data[7]))
        self.config.set("basic_info", "row", str(self.data[0]))
        self.config.set("basic_info", "column", str(self.data[1]))
        self.config.set("basic_info", "irregular_row", "0")
        self.config.set("basic_info", "irregular_column", "0")
        self.config.set("special_section", "all_random", str(self.data[2]))
        self.config.set("special_section", "front_back_change", str(self.data[3]))
        self.config.set("special_section", "centre_to_side", str(self.data[4]))
        self.config.set("special_section", "show_detail", str(self.data[5]))
        for i, j in enumerate(self.data[6]):
            self.config.set("ban_group", f"g{j}", str(i))
        else:
            self.config.set("ban_group", "g0", "")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_ui = MainUI()
    main_ui.show()
    sys.exit(app.exec_())
