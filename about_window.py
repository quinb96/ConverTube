# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_windowVzgqRP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import asset_loader

class Ui_About_Window(object):
    def setupUi(self, About_Window):
        if not About_Window.objectName():
            About_Window.setObjectName(u"About_Window")
        About_Window.setWindowModality(Qt.ApplicationModal)
        About_Window.resize(708, 455)
        About_Window.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(About_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.485, y1:0.415045, x2:0.480294, y2:0.932, stop:0 rgba(61, 255, 232, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.frame_2)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(32, 32))
        self.minimize_button.setMaximumSize(QSize(32, 32))
        self.minimize_button.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/assets/minimize_button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(20, 20))
        self.minimize_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.minimize_button, 0, Qt.AlignRight)

        self.exit_button = QPushButton(self.frame_2)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(32, 32))
        self.exit_button.setMaximumSize(QSize(32, 32))
        self.exit_button.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QSize(20, 20))
        self.exit_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.exit_button)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(700, 200))
        self.label_2.setMaximumSize(QSize(700, 200))
        font = QFont()
        font.setPointSize(5)
        self.label_2.setFont(font)
        self.label_2.setPixmap(QPixmap(u":/icons/assets/ConverTube_Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.OK_button = QPushButton(self.frame_3)
        self.OK_button.setObjectName(u"OK_button")
        self.OK_button.setMinimumSize(QSize(50, 0))
        self.OK_button.setMaximumSize(QSize(50, 16777215))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.OK_button.setFont(font1)

        self.gridLayout.addWidget(self.OK_button, 7, 0, 1, 1, Qt.AlignHCenter)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 100))
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1, Qt.AlignHCenter)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        About_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(About_Window)

        QMetaObject.connectSlotsByName(About_Window)
    # setupUi

    def retranslateUi(self, About_Window):
        About_Window.setWindowTitle(QCoreApplication.translate("About_Window", u"Settings", None))
        self.linkTemplate = "<a href={0}>{1}</a>"
        self.minimize_button.setText("")
        self.exit_button.setText("")
        self.label_2.setText("")
        self.OK_button.setText(QCoreApplication.translate("About_Window", u"OK", None))
        self.label.setText(QCoreApplication.translate("About_Window", u"Made by Quin Brown", None))
        self.label_4.setText(QCoreApplication.translate("About_Window", u"v1.0", None))
        self.label_3.setText(QCoreApplication.translate("About_Window", u"A GUI YouTube video downloader and converter.", None))
        self.label_5.setText(self.linkTemplate.format("https://github.com/sketchyboi14/ConverTube/issues", "Report Issues"))
    # retranslateUi

