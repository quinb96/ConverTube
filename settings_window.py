# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_windowrewblU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import asset_loader

class Ui_Settings_Window(object):
    def setupUi(self, Settings_Window):
        if not Settings_Window.objectName():
            Settings_Window.setObjectName(u"Settings_Window")
        Settings_Window.setWindowModality(Qt.ApplicationModal)
        Settings_Window.resize(708, 455)
        Settings_Window.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Settings_Window)
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
        self.video_save_path = QLineEdit(self.frame_3)
        self.video_save_path.setObjectName(u"video_save_path")

        self.gridLayout.addWidget(self.video_save_path, 0, 1, 1, 1)

        self.video_save_location_label = QLabel(self.frame_3)
        self.video_save_location_label.setObjectName(u"video_save_location_label")
        self.video_save_location_label.setPixmap(QPixmap(u":/icons/assets/video_save_location_text.svg"))
        self.video_save_location_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.video_save_location_label, 0, 0, 1, 1)

        self.audio_save_location_label = QLabel(self.frame_3)
        self.audio_save_location_label.setObjectName(u"audio_save_location_label")
        self.audio_save_location_label.setPixmap(QPixmap(u":/icons/assets/audio_save_location_text.svg"))
        self.audio_save_location_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.audio_save_location_label, 1, 0, 1, 1)

        self.video_save_button = QPushButton(self.frame_3)
        self.video_save_button.setObjectName(u"video_save_button")
        self.video_save_button.setMinimumSize(QSize(100, 30))
        self.video_save_button.setMaximumSize(QSize(100, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/save_text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.video_save_button.setIcon(icon2)
        self.video_save_button.setIconSize(QSize(150, 150))
        self.video_save_button.setFlat(False)

        self.gridLayout.addWidget(self.video_save_button, 0, 3, 1, 1)

        self.audio_save_path = QLineEdit(self.frame_3)
        self.audio_save_path.setObjectName(u"audio_save_path")

        self.gridLayout.addWidget(self.audio_save_path, 1, 1, 1, 1)

        self.audio_save_button = QPushButton(self.frame_3)
        self.audio_save_button.setObjectName(u"audio_save_button")
        self.audio_save_button.setMinimumSize(QSize(100, 30))
        self.audio_save_button.setMaximumSize(QSize(100, 30))
        self.audio_save_button.setIcon(icon2)
        self.audio_save_button.setIconSize(QSize(150, 150))

        self.gridLayout.addWidget(self.audio_save_button, 1, 3, 1, 1)

        self.vidlocbrowser_button = QPushButton(self.frame_3)
        self.vidlocbrowser_button.setObjectName(u"vidlocbrowser_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vidlocbrowser_button.setIcon(icon3)

        self.gridLayout.addWidget(self.vidlocbrowser_button, 0, 2, 1, 1)

        self.audlocbrowser_button = QPushButton(self.frame_3)
        self.audlocbrowser_button.setObjectName(u"audlocbrowser_button")
        self.audlocbrowser_button.setIcon(icon3)

        self.gridLayout.addWidget(self.audlocbrowser_button, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        Settings_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings_Window)

        QMetaObject.connectSlotsByName(Settings_Window)
    # setupUi

    def retranslateUi(self, Settings_Window):
        Settings_Window.setWindowTitle(QCoreApplication.translate("Settings_Window", u"Settings", None))
        self.minimize_button.setText("")
        self.exit_button.setText("")
        self.video_save_location_label.setText("")
        self.audio_save_location_label.setText("")
        self.video_save_button.setText("")
        self.audio_save_button.setText("")
        self.vidlocbrowser_button.setText("")
        self.audlocbrowser_button.setText("")
    # retranslateUi

