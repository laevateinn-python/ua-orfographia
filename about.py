# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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

import res_rc

class Ui_About(object):
    def setupUi(self, About):
        if About.objectName():
            About.setObjectName(u"About")
        About.resize(695, 274)
        font = QFont()
        font.setFamily(u"Levenim MT")
        font.setPointSize(12)
        About.setFont(font)
        About.setCursor(QCursor(Qt.WhatsThisCursor))
        icon = QIcon()
        icon.addFile(u":/\u043d\u043e\u0432\u0438\u0439\u041f\u0440\u0435\u0444\u0456\u043a\u0441/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        About.setWindowIcon(icon)
        self.formLayout = QFormLayout(About)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(About)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(About)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setCursor(QCursor(Qt.ArrowCursor))
        self.label_2.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.label_2.setMargin(0)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(About)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("About", u"<html><head/><body><p><img src=\":/About/about.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("About", u"<html><head/><body><h3>\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u0430 \u0434\u043b\u044f \u0433\u0440\u0430\u043c\u0430\u0442\u0438\u0447\u043d\u043e\u0433\u043e \u0440\u043e\u0437\u0431\u043e\u0440\u0443 \u0441\u043b\u0456\u0432</h3><h3>\u0442\u0430 \u0432\u0438\u0440\u0456\u0448\u0443\u0432\u0430\u043d\u043d\u044f \u0442\u0435\u0441\u0442\u0456\u0432 </h3><p><a href=\"https://github.com/laevateinn-python/ua-orfographia\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub \u0440\u0435\u043f\u043e\u0437\u0438\u0442\u043e\u0440\u0456\u0439</span></a></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("About", u"<html><head/><body><p>\u0410\u0432\u0442\u043e\u0440: Vladyslav Chaliuk <a href=\"https://github.com/laevateinn-python\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a></p><p>Email: <a href=\"https://vladchaluk@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">vladchaluk@gmail.com</span></a></p><p>\u0412\u0438\u043a\u043e\u0440\u0438\u0441\u0442\u0430\u043d\u043d\u044f \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0456\u0432 \u0437 <a href=\"https://slovnyk.ua\"><span style=\" text-decoration: underline; color:#0000ff;\">slovnyk.ua</span></a></p><p>copyright@2020</p></body></html>", None))
    # retranslateUi

