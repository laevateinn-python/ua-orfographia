# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_answer.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(855, 706)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 20, 711, 611))
        font = QFont()
        font.setFamily(u"Levenim MT")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(12)
        self.groupBox.setFont(font)
        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 20, 641, 461))
        self.toolBox = QToolBox(self.groupBox)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(10, 20, 681, 571))
        self.retranslateUi(Form)

        self.toolBox.setCurrentIndex(0)



        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0412\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c", None))
    # retranslateUi
