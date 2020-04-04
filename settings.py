# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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

class Ui_Settings(object):
    def setupUi(self, Settings):
        if Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(461, 207)
        font = QFont()
        font.setFamily(u"Levenim MT")
        font.setPointSize(12)
        Settings.setFont(font)
        icon = QIcon()
        icon.addFile(u":/\u043d\u043e\u0432\u0438\u0439\u041f\u0440\u0435\u0444\u0456\u043a\u0441/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Settings.setWindowIcon(icon)
        self.formLayout = QFormLayout(Settings)
        self.formLayout.setObjectName(u"formLayout")
        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.buttonBox)

        self.groupBox = QGroupBox(Settings)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font1 = QFont()
        font1.setFamily(u"Levenim MT")
        font1.setPointSize(11)
        self.comboBox.setFont(font1)

        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(False)

        self.verticalLayout.addWidget(self.checkBox)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.groupBox)


        self.retranslateUi(Settings)
        self.buttonBox.accepted.connect(Settings.close)
        self.buttonBox.rejected.connect(Settings.close)
        self.horizontalSlider.valueChanged.connect(self.progressBar.setValue)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"\u041d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("Settings", u"\u041e\u0441\u043d\u043e\u0432\u043d\u0456", None))
        self.label.setText(QCoreApplication.translate("Settings", u"\u041c\u043e\u0432\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Settings", u"Ukranian", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Settings", u"Russian", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Settings", u"English", None))

        self.checkBox.setText(QCoreApplication.translate("Settings", u"\u0421\u0445\u043e\u0432\u0430\u0442\u0438\u0020\u043f\u0435\u0440\u0435\u0434\u0431\u0430\u0447\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"\u041f\u0440\u043e\u0441\u0442\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440)) ^ ", None))
    # retranslateUi
