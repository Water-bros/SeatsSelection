from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        font.setPointSize(10)
        icon = QtGui.QIcon()
        icon.addFile("./icons/icon.png", QtCore.QSize(), QtGui.QIcon.Normal,
                     QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(0.98)
        MainWindow.setStyleSheet(
            """
            QPushButton {
                border-radius: 10px;
                width: 150px;
                height: 75px;
                background-color: rgb(222, 255, 255);
                font: 57 12pt "OPlusSans 3.0";
            }
            
            QPushButton:hover {
                background-color: rgb(185, 255, 255)
            }
            
            QMainWindow {
                background-color: rgb(239, 255, 248)
            }
            
            QComboBox {
                border-radius: 10px;
                background-color: rgb(229, 229, 229);
                height: 50px;
                font: 57 12pt "OPlusSans 3.0";
            }
            
            QMenuBar {
                background-color: rgb(255, 249, 255);
                font: 57 12pt "OPlusSans 3.0";
            }
            
            QTableWidget {
                border-radius: 10px;
            }
            
            QWidget#widget {
                border: 5px solid black;
            }
            
            QWidget#widget>QLabel {
                border: 3px solid black;
                font: 57 15pt "OPlusSans 3.0";
            }
            """)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 0, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_5.addWidget(self.comboBox, 1, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_5.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 146, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu_3)
        self.menu_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menu_3)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.actionGitee = QtWidgets.QAction(MainWindow)
        self.actionGitee.setObjectName("actionGitee")
        self.actionEmail = QtWidgets.QAction(MainWindow)
        self.actionEmail.setObjectName("actionEmail")
        self.actiond = QtWidgets.QAction(MainWindow)
        self.actiond.setObjectName("actiond")
        self.action01 = QtWidgets.QAction(MainWindow)
        self.action01.setObjectName("action01")
        self.action02 = QtWidgets.QAction(MainWindow)
        self.action02.setObjectName("action02")
        self.action03 = QtWidgets.QAction(MainWindow)
        self.action03.setObjectName("action03")
        self.action04 = QtWidgets.QAction(MainWindow)
        self.action04.setObjectName("action04")
        self.action05 = QtWidgets.QAction(MainWindow)
        self.action05.setObjectName("action05")
        self.action06 = QtWidgets.QAction(MainWindow)
        self.action06.setObjectName("action06")
        self.action07 = QtWidgets.QAction(MainWindow)
        self.action07.setObjectName("action07")
        self.action08 = QtWidgets.QAction(MainWindow)
        self.action08.setObjectName("action08")
        self.action09 = QtWidgets.QAction(MainWindow)
        self.action09.setObjectName("action09")
        self.action010 = QtWidgets.QAction(MainWindow)
        self.action010.setObjectName("action010")
        self.action11 = QtWidgets.QAction(MainWindow)
        self.action11.setObjectName("action11")
        self.action13 = QtWidgets.QAction(MainWindow)
        self.action13.setObjectName("action13")
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.menu.addAction(self.action01)
        self.menu.addAction(self.action02)
        self.menu.addSeparator()
        self.menu.addAction(self.action03)
        self.menu_2.addAction(self.action_help)
        self.menu_4.addAction(self.actionGithub)
        self.menu_4.addAction(self.actionGitee)
        self.menu_5.addAction(self.action11)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.action06)
        self.menu_5.addAction(self.action07)
        self.menu_5.addAction(self.action08)
        self.menu_5.addAction(self.action09)
        self.menu_5.addAction(self.action010)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.action13)
        self.menu_3.addAction(self.actiond)
        self.menu_3.addAction(self.menu_4.menuAction())
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "座位随机生成器 v2.0"))
        self.pushButton_2.setText(_translate("MainWindow", "随机选择"))
        self.pushButton.setText(_translate("MainWindow", "重置"))
        self.pushButton_3.setText(_translate("MainWindow", "撤销"))
        self.pushButton_4.setText(_translate("MainWindow", "还原"))
        self.menu.setTitle(_translate("MainWindow", "配置"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu_3.setTitle(_translate("MainWindow", "更多"))
        self.menu_4.setTitle(_translate("MainWindow", "开源信息"))
        self.menu_5.setTitle(_translate("MainWindow", "意见与反馈"))
        self.action_help.setText(_translate("MainWindow", "使用说明"))
        self.actionGithub.setText(_translate("MainWindow", "Github"))
        self.actionGitee.setText(_translate("MainWindow", "Gitee"))
        self.actionEmail.setText(_translate("MainWindow", "Email"))
        self.actiond.setText(_translate("MainWindow", "联系作者"))
        self.action01.setText(_translate("MainWindow", "导入座位表"))
        self.action02.setText(_translate("MainWindow", "导出座位表"))
        self.action03.setText(_translate("MainWindow", "自定义"))
        self.action04.setText(_translate("MainWindow", "要是连这个都不会做"))
        self.action05.setText(_translate("MainWindow", "那就没题可做了"))
        self.action06.setText(_translate("MainWindow", "说说个事"))
        self.action07.setText(_translate("MainWindow", "我一看"))
        self.action08.setText(_translate("MainWindow", "废掉了"))
        self.action09.setText(_translate("MainWindow", "要是连这个都不会做"))
        self.action010.setText(_translate("MainWindow", "那就没题可做了"))
        self.action11.setText(_translate("MainWindow", "彩蛋"))
        self.action13.setText(_translate("MainWindow", "别点我"))
