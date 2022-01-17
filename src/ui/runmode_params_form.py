# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerCQTuzM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_runmode_params_widget(object):
    def setupUi(self, runmode_params_widget):
        if not runmode_params_widget.objectName():
            runmode_params_widget.setObjectName(u"runmode_params_widget")
        runmode_params_widget.resize(631, 481)
        self.groupBox_3 = QGroupBox(runmode_params_widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(290, 250, 281, 111))
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 20, 141, 16))
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 40, 131, 16))
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 60, 101, 16))
        self.LevMax_3 = QGroupBox(runmode_params_widget)
        self.LevMax_3.setObjectName(u"LevMax_3")
        self.LevMax_3.setGeometry(QRect(30, 210, 101, 151))
        self.lev_min_plus = QPushButton(self.LevMax_3)
        self.lev_min_plus.setObjectName(u"lev_min_plus")
        self.lev_min_plus.setGeometry(QRect(20, 30, 61, 41))
        self.lev_min_plus.setCheckable(False)
        self.lev_min_minus = QPushButton(self.LevMax_3)
        self.lev_min_minus.setObjectName(u"lev_min_minus")
        self.lev_min_minus.setGeometry(QRect(20, 90, 61, 41))
        self.groupBox_2 = QGroupBox(runmode_params_widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(140, 40, 81, 321))
        self.lcdNumber = QLCDNumber(self.groupBox_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(10, 20, 61, 31))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setProperty("value", 90.000000000000000)
        self.led_slider = QSlider(self.groupBox_2)
        self.led_slider.setObjectName(u"led_slider")
        self.led_slider.setGeometry(QRect(20, 70, 41, 231))
        self.led_slider.setMaximum(100)
        self.led_slider.setValue(89)
        self.led_slider.setOrientation(Qt.Vertical)
        self.LevMax = QGroupBox(runmode_params_widget)
        self.LevMax.setObjectName(u"LevMax")
        self.LevMax.setGeometry(QRect(30, 40, 101, 151))
        self.lev_max_plus = QPushButton(self.LevMax)
        self.lev_max_plus.setObjectName(u"lev_max_plus")
        self.lev_max_plus.setGeometry(QRect(20, 30, 61, 41))
        self.lev_max_plus.setCheckable(False)
        self.lev_max_minus = QPushButton(self.LevMax)
        self.lev_max_minus.setObjectName(u"lev_max_minus")
        self.lev_max_minus.setGeometry(QRect(20, 90, 61, 41))
        self.groupBox = QGroupBox(runmode_params_widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(290, 50, 281, 151))
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 20, 91, 16))
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 60, 161, 16))
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 30, 231, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_15.setFont(font1)
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 70, 231, 31))
        self.label_16.setFont(font1)
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 100, 161, 16))
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 110, 231, 31))
        self.label_18.setFont(font1)

        self.retranslateUi(runmode_params_widget)
        self.led_slider.sliderMoved.connect(self.lcdNumber.display)

        QMetaObject.connectSlotsByName(runmode_params_widget)
    # setupUi

    def retranslateUi(self, runmode_params_widget):
        runmode_params_widget.setWindowTitle(QCoreApplication.translate("runmode_params_widget", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("runmode_params_widget", u"Info in production", None))
        self.label_10.setText(QCoreApplication.translate("runmode_params_widget", u"Bottle per hours", None))
        self.label_11.setText(QCoreApplication.translate("runmode_params_widget", u"% bottle rejected", None))
        self.label_12.setText(QCoreApplication.translate("runmode_params_widget", u"Bottle counter", None))
        self.LevMax_3.setTitle(QCoreApplication.translate("runmode_params_widget", u"Lev Min", None))
        self.lev_min_plus.setText(QCoreApplication.translate("runmode_params_widget", u"+", None))
        self.lev_min_minus.setText(QCoreApplication.translate("runmode_params_widget", u"-", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("runmode_params_widget", u"LED", None))
        self.LevMax.setTitle(QCoreApplication.translate("runmode_params_widget", u"Lev Max", None))
        self.lev_max_plus.setText(QCoreApplication.translate("runmode_params_widget", u"+", None))
        self.lev_max_minus.setText(QCoreApplication.translate("runmode_params_widget", u"-", None))
        self.groupBox.setTitle(QCoreApplication.translate("runmode_params_widget", u"Model info", None))
        self.label_13.setText(QCoreApplication.translate("runmode_params_widget", u"Name model", None))
        self.label_14.setText(QCoreApplication.translate("runmode_params_widget", u"Based on bottle type:", None))
        self.label_15.setText(QCoreApplication.translate("runmode_params_widget", u"ETHEL SPUM V1", None))
        self.label_16.setText(QCoreApplication.translate("runmode_params_widget", u"ETHEL", None))
        self.label_17.setText(QCoreApplication.translate("runmode_params_widget", u"Based on led brightness:", None))
        self.label_18.setText(QCoreApplication.translate("runmode_params_widget", u"100%", None))
    # retranslateUi

