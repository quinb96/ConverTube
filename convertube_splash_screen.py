# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convertube_splash_screenZCHqPq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import asset_loader

class Ui_Splash_Window(object):
    def setupUi(self, Splash_Window):
        if not Splash_Window.objectName():
            Splash_Window.setObjectName(u"Splash_Window")
        Splash_Window.resize(800, 600)
        self.centralwidget = QWidget(Splash_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.transparent_frame = QFrame(self.centralwidget)
        self.transparent_frame.setObjectName(u"transparent_frame")
        self.transparent_frame.setGeometry(QRect(70, 90, 651, 381))
        font = QFont()
        font.setFamily(u"Inconsolata")
        font.setBold(True)
        font.setWeight(75)
        self.transparent_frame.setFont(font)
        self.transparent_frame.setStyleSheet(u"image: url(:/icons/assets/ConverTube_Logo.png);")
        self.transparent_frame.setFrameShape(QFrame.NoFrame)
        self.transparent_frame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.transparent_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(120, 243, 421, 23))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.progressBar.setFont(font1)
        self.progressBar.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(76, 214, 207, 255), stop:1 rgba(79, 181, 214, 255));")
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.splash_frame = QFrame(self.centralwidget)
        self.splash_frame.setObjectName(u"splash_frame")
        self.splash_frame.setGeometry(QRect(140, 210, 511, 211))
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        self.splash_frame.setFont(font2)
        self.splash_frame.setStyleSheet(u"border: 5px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(76, 214, 207, 255), stop:1 rgba(79, 181, 214, 255));\n"
"border-radius: 20px;")
        self.splash_frame.setFrameShape(QFrame.Box)
        self.splash_frame.setFrameShadow(QFrame.Raised)
        self.status_text = QLabel(self.centralwidget)
        self.status_text.setObjectName(u"status_text")
        self.status_text.setGeometry(QRect(192, 313, 171, 20))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.status_text.setFont(font3)
        self.author_text = QLabel(self.centralwidget)
        self.author_text.setObjectName(u"author_text")
        self.author_text.setGeometry(QRect(192, 370, 161, 31))
        self.author_text.setFont(font3)
        self.version_text = QLabel(self.centralwidget)
        self.version_text.setObjectName(u"version_text")
        self.version_text.setGeometry(QRect(617, 377, 31, 51))
        self.version_text.setFont(font3)
        Splash_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash_Window)

        QMetaObject.connectSlotsByName(Splash_Window)
    # setupUi

    def retranslateUi(self, Splash_Window):
        Splash_Window.setWindowTitle(QCoreApplication.translate("Splash_Window", u"MainWindow", None))
        self.status_text.setText(QCoreApplication.translate("Splash_Window", u"<html><head/><body><p>Querying YouTube...</p></body></html>", None))
        self.author_text.setText(QCoreApplication.translate("Splash_Window", u"Designed by Quin Brown", None))
        self.version_text.setText(QCoreApplication.translate("Splash_Window", u"v1.0", None))
    # retranslateUi

