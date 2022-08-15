# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'access_denied_error_windowtnMuEP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import asset_loader

class Ui_Access_Denied_Err_Window(object):
    def setupUi(self, Access_Denied_Err_Window):
        if not Access_Denied_Err_Window.objectName():
            Access_Denied_Err_Window.setObjectName(u"Access_Denied_Err_Window")
        Access_Denied_Err_Window.setWindowModality(Qt.ApplicationModal)
        Access_Denied_Err_Window.resize(528, 474)
        Access_Denied_Err_Window.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Access_Denied_Err_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolbar = QFrame(self.main_frame)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMinimumSize(QSize(0, 50))
        self.toolbar.setMaximumSize(QSize(16777215, 50))
        self.toolbar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.485, y1:0.415045, x2:0.480294, y2:0.932, stop:0 rgba(61, 255, 232, 255), stop:1 rgba(255, 255, 255, 255));")
        self.toolbar.setFrameShape(QFrame.StyledPanel)
        self.toolbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.toolbar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.toolbar)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(32, 32))
        self.minimize_button.setMaximumSize(QSize(32, 32))
        self.minimize_button.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/assets/minimize_button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(59, 130))
        self.minimize_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.minimize_button, 0, Qt.AlignRight)

        self.exit_button = QPushButton(self.toolbar)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(32, 32))
        self.exit_button.setMaximumSize(QSize(32, 32))
        self.exit_button.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QSize(256, 256))
        self.exit_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.exit_button)


        self.verticalLayout.addWidget(self.toolbar)

        self.central_frame = QFrame(self.main_frame)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.central_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 90, 374, 228))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.alert_icon = QLabel(self.layoutWidget)
        self.alert_icon.setObjectName(u"alert_icon")
        self.alert_icon.setPixmap(QPixmap(u":/icons/assets/alert-octagon.svg"))
        self.alert_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.alert_icon)

        self.error_text = QLabel(self.layoutWidget)
        self.error_text.setObjectName(u"error_text")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.error_text.setFont(font)
        self.error_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.error_text)

        self.error_text2 = QLabel(self.layoutWidget)
        self.error_text2.setObjectName(u"error_text2")
        self.error_text2.setFont(font)

        self.verticalLayout_2.addWidget(self.error_text2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.OK_button = QPushButton(self.layoutWidget)
        self.OK_button.setObjectName(u"OK_button")
        self.OK_button.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_2.addWidget(self.OK_button, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.central_frame)


        self.horizontalLayout.addWidget(self.main_frame)

        Access_Denied_Err_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Access_Denied_Err_Window)

        QMetaObject.connectSlotsByName(Access_Denied_Err_Window)
    # setupUi

    def retranslateUi(self, Access_Denied_Err_Window):
        Access_Denied_Err_Window.setWindowTitle(QCoreApplication.translate("Access_Denied_Err_Window", u"Settings", None))
        self.minimize_button.setText("")
        self.exit_button.setText("")
        self.alert_icon.setText("")
        self.error_text.setText(QCoreApplication.translate("Access_Denied_Err_Window", u"Unable to write config files.", None))
        self.error_text2.setText(QCoreApplication.translate("Access_Denied_Err_Window", u"Access Denied.", None))
        self.OK_button.setText(QCoreApplication.translate("Access_Denied_Err_Window", u"OK", None))
    # retranslateUi

