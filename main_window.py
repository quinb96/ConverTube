# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowFfYHzX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import asset_loader

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(782, 443)
        MainWindow.setMinimumSize(QSize(35, 5))
        MainWindow.setMaximumSize(QSize(16777215, 976))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolbar = QFrame(self.main_frame)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMinimumSize(QSize(150, 50))
        self.toolbar.setMaximumSize(QSize(16777215, 50))
        self.toolbar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.485, y1:0.415045, x2:0.480294, y2:0.932, stop:0 rgba(61, 255, 232, 255), stop:1 rgba(255, 255, 255, 255));")
        self.toolbar.setFrameShape(QFrame.StyledPanel)
        self.toolbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.toolbar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.hamburger_button = QPushButton(self.toolbar)
        self.hamburger_button.setObjectName(u"hamburger_button")
        self.hamburger_button.setMinimumSize(QSize(32, 32))
        self.hamburger_button.setMaximumSize(QSize(32, 32))
        self.hamburger_button.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/assets/hamburger_button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hamburger_button.setIcon(icon)
        self.hamburger_button.setIconSize(QSize(75, 75))
        self.hamburger_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.hamburger_button)

        self.minimize_button = QPushButton(self.toolbar)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(32, 32))
        self.minimize_button.setMaximumSize(QSize(32, 32))
        self.minimize_button.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/minimize_button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon1)
        self.minimize_button.setIconSize(QSize(20, 20))
        self.minimize_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.minimize_button, 0, Qt.AlignRight)

        self.maximize_button = QPushButton(self.toolbar)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setMinimumSize(QSize(32, 32))
        self.maximize_button.setMaximumSize(QSize(32, 32))
        self.maximize_button.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/maximize_button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(20, 20))
        self.maximize_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.maximize_button)

        self.exit_button = QPushButton(self.toolbar)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(32, 32))
        self.exit_button.setMaximumSize(QSize(32, 32))
        self.exit_button.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon3)
        self.exit_button.setIconSize(QSize(20, 20))
        self.exit_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.exit_button)


        self.verticalLayout_4.addWidget(self.toolbar)

        self.central_frame = QFrame(self.main_frame)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.central_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.central_frame)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(0, 380))
        self.left_menu.setMaximumSize(QSize(0, 380))
        self.left_menu.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.485, y1:0.415045, x2:0.480294, y2:0.932, stop:0 rgba(61, 255, 232, 255), stop:1 rgba(255, 255, 255, 255));")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settings_button = QPushButton(self.left_menu)
        self.settings_button.setObjectName(u"settings_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/settings_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon4)
        self.settings_button.setIconSize(QSize(20, 20))
        self.settings_button.setFlat(True)

        self.verticalLayout_2.addWidget(self.settings_button)

        self.help_button = QPushButton(self.left_menu)
        self.help_button.setObjectName(u"help_button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.help_button.setIcon(icon5)
        self.help_button.setIconSize(QSize(24, 24))
        self.help_button.setFlat(True)

        self.verticalLayout_2.addWidget(self.help_button)


        self.horizontalLayout.addWidget(self.left_menu)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 15, -1)
        self.url_2 = QLabel(self.central_frame)
        self.url_2.setObjectName(u"url_2")
        self.url_2.setMinimumSize(QSize(0, 30))
        self.url_2.setMaximumSize(QSize(16777215, 30))
        self.url_2.setPixmap(QPixmap(u":/icons/assets/URL_label.svg"))
        self.url_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.url_2, 1, 0, 1, 1)

        self.start_button1 = QPushButton(self.central_frame)
        self.start_button1.setObjectName(u"start_button1")
        self.start_button1.setMinimumSize(QSize(100, 30))
        self.start_button1.setMaximumSize(QSize(100, 30))
        self.start_button1.setToolTipDuration(-1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/start_button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_button1.setIcon(icon6)
        self.start_button1.setIconSize(QSize(150, 150))
        self.start_button1.setFlat(False)

        self.gridLayout.addWidget(self.start_button1, 0, 2, 1, 1, Qt.AlignHCenter)

        self.start_button3 = QPushButton(self.central_frame)
        self.start_button3.setObjectName(u"start_button3")
        self.start_button3.setMinimumSize(QSize(100, 30))
        self.start_button3.setMaximumSize(QSize(100, 30))
        self.start_button3.setIcon(icon6)
        self.start_button3.setIconSize(QSize(150, 150))

        self.gridLayout.addWidget(self.start_button3, 2, 2, 1, 1, Qt.AlignHCenter)

        self.url_textfield4 = QLineEdit(self.central_frame)
        self.url_textfield4.setObjectName(u"url_textfield4")

        self.gridLayout.addWidget(self.url_textfield4, 3, 1, 1, 1)

        self.url_textfield2 = QLineEdit(self.central_frame)
        self.url_textfield2.setObjectName(u"url_textfield2")

        self.gridLayout.addWidget(self.url_textfield2, 1, 1, 1, 1)

        self.url_5 = QLabel(self.central_frame)
        self.url_5.setObjectName(u"url_5")
        self.url_5.setMinimumSize(QSize(0, 30))
        self.url_5.setMaximumSize(QSize(16777215, 30))
        self.url_5.setPixmap(QPixmap(u":/icons/assets/URL_label.svg"))
        self.url_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.url_5, 4, 0, 1, 1)

        self.url_4 = QLabel(self.central_frame)
        self.url_4.setObjectName(u"url_4")
        self.url_4.setMinimumSize(QSize(0, 30))
        self.url_4.setMaximumSize(QSize(16777215, 30))
        self.url_4.setPixmap(QPixmap(u":/icons/assets/URL_label.svg"))
        self.url_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.url_4, 3, 0, 1, 1)

        self.url_textfield5 = QLineEdit(self.central_frame)
        self.url_textfield5.setObjectName(u"url_textfield5")

        self.gridLayout.addWidget(self.url_textfield5, 4, 1, 1, 1)

        self.start_button5 = QPushButton(self.central_frame)
        self.start_button5.setObjectName(u"start_button5")
        self.start_button5.setMinimumSize(QSize(100, 30))
        self.start_button5.setMaximumSize(QSize(100, 30))
        self.start_button5.setIcon(icon6)
        self.start_button5.setIconSize(QSize(150, 150))

        self.gridLayout.addWidget(self.start_button5, 4, 2, 1, 1)

        self.start_button2 = QPushButton(self.central_frame)
        self.start_button2.setObjectName(u"start_button2")
        self.start_button2.setMinimumSize(QSize(100, 30))
        self.start_button2.setMaximumSize(QSize(100, 30))
        self.start_button2.setIcon(icon6)
        self.start_button2.setIconSize(QSize(150, 150))

        self.gridLayout.addWidget(self.start_button2, 1, 2, 1, 1, Qt.AlignHCenter)

        self.url_3 = QLabel(self.central_frame)
        self.url_3.setObjectName(u"url_3")
        self.url_3.setMinimumSize(QSize(0, 30))
        self.url_3.setMaximumSize(QSize(16777215, 30))
        self.url_3.setPixmap(QPixmap(u":/icons/assets/URL_label.svg"))
        self.url_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.url_3, 2, 0, 1, 1)

        self.url_textfield3 = QLineEdit(self.central_frame)
        self.url_textfield3.setObjectName(u"url_textfield3")

        self.gridLayout.addWidget(self.url_textfield3, 2, 1, 1, 1)

        self.url_textfield1 = QLineEdit(self.central_frame)
        self.url_textfield1.setObjectName(u"url_textfield1")

        self.gridLayout.addWidget(self.url_textfield1, 0, 1, 1, 1)

        self.start_button4 = QPushButton(self.central_frame)
        self.start_button4.setObjectName(u"start_button4")
        self.start_button4.setMinimumSize(QSize(100, 30))
        self.start_button4.setMaximumSize(QSize(100, 30))
        self.start_button4.setIcon(icon6)
        self.start_button4.setIconSize(QSize(150, 150))

        self.gridLayout.addWidget(self.start_button4, 3, 2, 1, 1, Qt.AlignHCenter)

        self.url_1 = QLabel(self.central_frame)
        self.url_1.setObjectName(u"url_1")
        self.url_1.setMinimumSize(QSize(0, 30))
        self.url_1.setMaximumSize(QSize(16777215, 30))
        self.url_1.setPixmap(QPixmap(u":/icons/assets/URL_label.svg"))
        self.url_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.url_1, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.central_frame)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.start_button1, self.start_button2)
        QWidget.setTabOrder(self.start_button2, self.start_button3)
        QWidget.setTabOrder(self.start_button3, self.start_button4)
        QWidget.setTabOrder(self.start_button4, self.start_button5)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ConverTube", None))
#if QT_CONFIG(tooltip)
        self.hamburger_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Expand Menu</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hamburger_button.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Minimize Window (Ctrl+M)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_button.setText("")
#if QT_CONFIG(shortcut)
        self.minimize_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.maximize_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Expand Window (Ctrl+E)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_button.setText("")
#if QT_CONFIG(shortcut)
        self.maximize_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.exit_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Exit (Ctrl+Q)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exit_button.setText("")
#if QT_CONFIG(shortcut)
        self.exit_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.settings_button.setText("")
        self.help_button.setText("")
        self.url_2.setText("")
        self.start_button1.setText("")
        self.start_button3.setText("")
        self.url_5.setText("")
        self.url_4.setText("")
        self.start_button5.setText("")
        self.start_button2.setText("")
        self.url_3.setText("")
        self.start_button4.setText("")
        self.url_1.setText("")
    # retranslateUi

