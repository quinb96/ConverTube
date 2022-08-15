# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thumbnail_preview_windowvIRLBa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import asset_loader

class Ui_Thumbnail_Preview_Window(object):
    def setupUi(self, Thumbnail_Preview_Window):
        if not Thumbnail_Preview_Window.objectName():
            Thumbnail_Preview_Window.setObjectName(u"Thumbnail_Preview_Window")
        Thumbnail_Preview_Window.setWindowModality(Qt.ApplicationModal)
        Thumbnail_Preview_Window.resize(528, 474)
        Thumbnail_Preview_Window.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Thumbnail_Preview_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setAutoFillBackground(False)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.toolbar = QFrame(self.main_frame)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setGeometry(QRect(2, 2, 521, 50))
        self.toolbar.setMinimumSize(QSize(0, 50))
        self.toolbar.setMaximumSize(QSize(16777215, 50))
        self.toolbar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.485, y1:0.415045, x2:0.480294, y2:0.932, stop:0 rgba(61, 255, 232, 255), stop:1 rgba(255, 255, 255, 255));")
        self.toolbar.setFrameShape(QFrame.StyledPanel)
        self.toolbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.toolbar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.toolbar)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(32, 32))
        self.exit_button.setMaximumSize(QSize(32, 32))
        self.exit_button.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/assets/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QSize(20, 20))
        self.exit_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.exit_button, 0, Qt.AlignRight)

        self.central_frame = QFrame(self.main_frame)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setGeometry(QRect(2, 58, 521, 341))
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.central_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.thumbnail_preview = QLabel(self.central_frame)
        self.thumbnail_preview.setObjectName(u"thumbnail_preview")

        self.gridLayout.addWidget(self.thumbnail_preview, 0, 0, 1, 1)

        self.format_selector = QComboBox(self.main_frame)
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.addItem("")
        self.format_selector.setObjectName(u"format_selector")
        self.format_selector.setGeometry(QRect(2, 400, 87, 32))
        self.format_selector.setAutoFillBackground(False)
        self.download_button = QPushButton(self.main_frame)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(220, 430, 84, 34))
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/download_button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.download_button.setIcon(icon1)
        self.download_button.setIconSize(QSize(125, 125))
        self.resolution_selector = QComboBox(self.main_frame)
        self.resolution_selector.setObjectName(u"resolution_selector")
        self.resolution_selector.setGeometry(QRect(440, 400, 87, 32))

        self.horizontalLayout.addWidget(self.main_frame)

        Thumbnail_Preview_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Thumbnail_Preview_Window)

        QMetaObject.connectSlotsByName(Thumbnail_Preview_Window)
    # setupUi

    def retranslateUi(self, Thumbnail_Preview_Window):
        Thumbnail_Preview_Window.setWindowTitle(QCoreApplication.translate("Thumbnail_Preview_Window", u"Settings", None))
        self.exit_button.setText("")
        self.thumbnail_preview.setText("")
        self.format_selector.setItemText(0, QCoreApplication.translate("Thumbnail_Preview_Window", u"mp4", None))
        self.format_selector.setItemText(1, QCoreApplication.translate("Thumbnail_Preview_Window", u"aac", None))
        self.format_selector.setItemText(2, QCoreApplication.translate("Thumbnail_Preview_Window", u"flac", None))
        self.format_selector.setItemText(3, QCoreApplication.translate("Thumbnail_Preview_Window", u"aiff", None))
        self.format_selector.setItemText(4, QCoreApplication.translate("Thumbnail_Preview_Window", u"m4a", None))
        self.format_selector.setItemText(5, QCoreApplication.translate("Thumbnail_Preview_Window", u"wav", None))
        self.format_selector.setItemText(6, QCoreApplication.translate("Thumbnail_Preview_Window", u"mov", None))
        self.format_selector.setItemText(7, QCoreApplication.translate("Thumbnail_Preview_Window", u"wmv", None))
        self.format_selector.setItemText(8, QCoreApplication.translate("Thumbnail_Preview_Window", u"wma", None))
        self.format_selector.setItemText(9, QCoreApplication.translate("Thumbnail_Preview_Window", u"mp3", None))
        self.format_selector.setItemText(10, QCoreApplication.translate("Thumbnail_Preview_Window", u"flv", None))
        self.format_selector.setItemText(11, QCoreApplication.translate("Thumbnail_Preview_Window", u"avi", None))
        self.format_selector.setItemText(12, QCoreApplication.translate("Thumbnail_Preview_Window", u"mkv", None))

        self.download_button.setText("")
    # retranslateUi

