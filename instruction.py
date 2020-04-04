# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instruction.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(982, 768)
        font = QFont()
        font.setFamily(u"Levenim MT")
        font.setPointSize(11)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/\u043d\u043e\u0432\u0438\u0439\u041f\u0440\u0435\u0444\u0456\u043a\u0441/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.formLayout_3 = QFormLayout(Dialog)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.buttonBox)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout = QFormLayout(self.tab)
        self.formLayout.setObjectName(u"formLayout")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setAutoFillBackground(True)
        self.tabWidget_2.setTabPosition(QTabWidget.West)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.tab_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 787, 993))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_2 = QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_2 = QScrollArea(self.tab_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setAutoFillBackground(True)
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -345, 787, 1020))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 4, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 5, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_3 = QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_3 = QScrollArea(self.tab_5)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setAutoFillBackground(True)
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 787, 995))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_15 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAutoFillBackground(False)

        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_18 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_3.addWidget(self.label_18)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_3.addWidget(self.label_19)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 4, 0, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 5, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.scrollArea_3)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_4 = QVBoxLayout(self.tab_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_4 = QScrollArea(self.tab_6)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setAutoFillBackground(True)
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setFrameShadow(QFrame.Plain)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, -335, 787, 1010))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_22 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAutoFillBackground(False)

        self.gridLayout_5.addWidget(self.label_23, 1, 0, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_5.addWidget(self.label_24, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_25 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_4.addWidget(self.label_25)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_4.addWidget(self.label_26)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 4, 0, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 5, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_4.addWidget(self.scrollArea_4)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.tabWidget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayout_2 = QFormLayout(self.tab_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setAutoFillBackground(True)
        self.tabWidget_3.setTabPosition(QTabWidget.West)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_5 = QVBoxLayout(self.tab_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_5 = QScrollArea(self.tab_7)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setAutoFillBackground(True)
        self.scrollArea_5.setFrameShape(QFrame.NoFrame)
        self.scrollArea_5.setFrameShadow(QFrame.Plain)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -452, 810, 2195))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_35 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 12, 0, 1, 1)

        self.label_62 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_6.addWidget(self.label_62, 7, 0, 1, 1)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_6.addWidget(self.label_34, 11, 0, 1, 1)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_6.addWidget(self.label_31, 9, 0, 1, 1)

        self.label_61 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_6.addWidget(self.label_61, 4, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_32 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_5.addWidget(self.label_32)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_5.addWidget(self.label_33)


        self.gridLayout_6.addLayout(self.horizontalLayout_5, 10, 0, 1, 1)

        self.label_59 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_6.addWidget(self.label_59, 2, 0, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_6.addWidget(self.label_29, 5, 0, 1, 1)

        self.label_58 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_6.addWidget(self.label_58, 1, 0, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.label_30, 6, 0, 1, 1)

        self.label_60 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_6.addWidget(self.label_60, 3, 0, 1, 1)

        self.label_57 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_6.addWidget(self.label_57, 0, 0, 1, 1)

        self.label_63 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_6.addWidget(self.label_63, 8, 0, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_5.addWidget(self.scrollArea_5)

        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_6 = QVBoxLayout(self.tab_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_6 = QScrollArea(self.tab_8)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setAutoFillBackground(True)
        self.scrollArea_6.setFrameShape(QFrame.NoFrame)
        self.scrollArea_6.setFrameShadow(QFrame.Plain)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 810, 2219))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_43 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_8.addWidget(self.label_43, 12, 0, 1, 1)

        self.label_71 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_8.addWidget(self.label_71, 7, 0, 1, 1)

        self.label_44 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_8.addWidget(self.label_44, 11, 0, 1, 1)

        self.label_45 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_8.addWidget(self.label_45, 9, 0, 1, 1)

        self.label_72 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_8.addWidget(self.label_72, 4, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_46 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_7.addWidget(self.label_46)

        self.label_47 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_7.addWidget(self.label_47)


        self.gridLayout_8.addLayout(self.horizontalLayout_7, 10, 0, 1, 1)

        self.label_73 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_8.addWidget(self.label_73, 2, 0, 1, 1)

        self.label_48 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_8.addWidget(self.label_48, 5, 0, 1, 1)

        self.label_74 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_8.addWidget(self.label_74, 1, 0, 1, 1)

        self.label_49 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAutoFillBackground(False)

        self.gridLayout_8.addWidget(self.label_49, 6, 0, 1, 1)

        self.label_75 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_8.addWidget(self.label_75, 3, 0, 1, 1)

        self.label_76 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_8.addWidget(self.label_76, 0, 0, 1, 1)

        self.label_77 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_8.addWidget(self.label_77, 8, 0, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_6.addWidget(self.scrollArea_6)

        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_7 = QVBoxLayout(self.tab_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_7 = QScrollArea(self.tab_9)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setAutoFillBackground(True)
        self.scrollArea_7.setFrameShape(QFrame.NoFrame)
        self.scrollArea_7.setFrameShadow(QFrame.Plain)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 787, 2204))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_50 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_9.addWidget(self.label_50, 12, 0, 1, 1)

        self.label_78 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_9.addWidget(self.label_78, 7, 0, 1, 1)

        self.label_51 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_9.addWidget(self.label_51, 11, 0, 1, 1)

        self.label_52 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_9.addWidget(self.label_52, 9, 0, 1, 1)

        self.label_79 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_9.addWidget(self.label_79, 4, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_53 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_8.addWidget(self.label_53)

        self.label_54 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_8.addWidget(self.label_54)


        self.gridLayout_9.addLayout(self.horizontalLayout_8, 10, 0, 1, 1)

        self.label_80 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_9.addWidget(self.label_80, 2, 0, 1, 1)

        self.label_55 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_9.addWidget(self.label_55, 5, 0, 1, 1)

        self.label_81 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_9.addWidget(self.label_81, 1, 0, 1, 1)

        self.label_56 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAutoFillBackground(False)

        self.gridLayout_9.addWidget(self.label_56, 6, 0, 1, 1)

        self.label_82 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_9.addWidget(self.label_82, 3, 0, 1, 1)

        self.label_83 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_9.addWidget(self.label_83, 0, 0, 1, 1)

        self.label_84 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_9.addWidget(self.label_84, 8, 0, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_7.addWidget(self.scrollArea_7)

        self.tabWidget_3.addTab(self.tab_9, "")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.tabWidget_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.formLayout_4 = QFormLayout(self.tab_10)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_85 = QLabel(self.tab_10)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout.addWidget(self.label_85, 0, 0, 1, 1)

        self.label_86 = QLabel(self.tab_10)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout.addWidget(self.label_86, 1, 0, 1, 1)

        self.label_87 = QLabel(self.tab_10)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout.addWidget(self.label_87, 2, 0, 1, 1)


        self.formLayout_4.setLayout(0, QFormLayout.LabelRole, self.gridLayout)

        self.tabWidget.addTab(self.tab_10, "")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.tabWidget)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.close)
        self.buttonBox.rejected.connect(Dialog.close)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(3)
        self.tabWidget_3.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0406\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0456\u044f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"1 \u0429\u043e\u0431 \u0437\u043d\u0430\u0439\u0442\u0438 \u0440\u0456\u0434, \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0438\u0431\u0440\u0430\u0442\u0438 \u0446\u0435\u0439 \u043f\u0443\u043d\u043a\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/1.png\"/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u" \u0432\u0432\u0435\u0441\u0442\u0438 \u0440\u044f\u0434\u043a\u0438 \u0437 \u0437\u0430\u0432\u0434\u0430\u043d\u043d\u044f \u0442\u0430 \u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u044f\u0434\u043a\u0456\u0432 \u0437\u0456 \u0441\u043b\u043e\u0432\u0430\u043c\u0438 \u0432 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u043d\u0456 \u043f\u043e\u043b\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/text.png\"/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/row_cow.png\"/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0456 \u043d\u0430\u0442\u0438\u0441\u043d\u0456\u0442\u044c \"\u0412\u0438\u0440\u0456\u0448\u0438\u0442\u0438\" \u0442\u0430 \u0447\u0435\u043a\u0430\u0439\u0442\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442(~4\u0441.)", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/solve.png\"/></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"\u0420\u0456\u0434", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"1 \u0429\u043e\u0431 \u0437\u043d\u0430\u0439\u0442\u0438 \u0447\u0438\u0441\u043b\u043e, \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0438\u0431\u0440\u0430\u0442\u0438 \u0446\u0435\u0439 \u043f\u0443\u043d\u043a\u0442", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/2.png\"/></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u" \u0432\u0432\u0435\u0441\u0442\u0438 \u0440\u044f\u0434\u043a\u0438 \u0437 \u0437\u0430\u0432\u0434\u0430\u043d\u043d\u044f \u0442\u0430 \u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u044f\u0434\u043a\u0456\u0432 \u0437\u0456 \u0441\u043b\u043e\u0432\u0430\u043c\u0438 \u0432 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u043d\u0456 \u043f\u043e\u043b\u044f", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/text.png\"/></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/row_cow.png\"/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0456 \u043d\u0430\u0442\u0438\u0441\u043d\u0456\u0442\u044c \"\u0412\u0438\u0440\u0456\u0448\u0438\u0442\u0438\" \u0442\u0430 \u0447\u0435\u043a\u0430\u0439\u0442\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442(~4\u0441.)", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/solve.png\"/></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"\u0427\u0438\u0441\u043b\u043e", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"1 \u0429\u043e\u0431 \u0437\u043d\u0430\u0439\u0442\u0438 \u0412\u0456\u0434\u043c\u0456\u043d\u043e\u043a, \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0438\u0431\u0440\u0430\u0442\u0438 \u0446\u0435\u0439 \u043f\u0443\u043d\u043a\u0442", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/3.png\"/></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u" \u0432\u0432\u0435\u0441\u0442\u0438 \u0440\u044f\u0434\u043a\u0438 \u0437 \u0437\u0430\u0432\u0434\u0430\u043d\u043d\u044f \u0442\u0430 \u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u044f\u0434\u043a\u0456\u0432 \u0437\u0456 \u0441\u043b\u043e\u0432\u0430\u043c\u0438 \u0432 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u043d\u0456 \u043f\u043e\u043b\u044f", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/text.png\"/></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/row_cow.png\"/></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0456 \u043d\u0430\u0442\u0438\u0441\u043d\u0456\u0442\u044c \"\u0412\u0438\u0440\u0456\u0448\u0438\u0442\u0438\" \u0442\u0430 \u0447\u0435\u043a\u0430\u0439\u0442\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442(~4\u0441.)", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/solve.png\"/></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Dialog", u"\u0412\u0456\u0434\u043c\u0456\u043d\u043e\u043a", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"1 \u0429\u043e\u0431 \u0437\u043d\u0430\u0439\u0442\u0438 \u0412\u0456\u0434\u043c\u0456\u043d\u0443, \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0438\u0431\u0440\u0430\u0442\u0438 \u0446\u0435\u0439 \u043f\u0443\u043d\u043a\u0442", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/4.png\"/></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u" \u0432\u0432\u0435\u0441\u0442\u0438 \u0440\u044f\u0434\u043a\u0438 \u0437 \u0437\u0430\u0432\u0434\u0430\u043d\u043d\u044f \u0442\u0430 \u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u044f\u0434\u043a\u0456\u0432 \u0437\u0456 \u0441\u043b\u043e\u0432\u0430\u043c\u0438 \u0432 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u043d\u0456 \u043f\u043e\u043b\u044f", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/text.png\"/></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/row_cow.png\"/></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0456 \u043d\u0430\u0442\u0438\u0441\u043d\u0456\u0442\u044c \"\u0412\u0438\u0440\u0456\u0448\u0438\u0442\u0438\" \u0442\u0430 \u0447\u0435\u043a\u0430\u0439\u0442\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442(~4\u0441.)", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/solve.png\"/></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("Dialog", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\u0417\u0432\u0438\u0447\u0430\u0439\u043d\u0438\u0439 \u0440\u0435\u0436\u0438\u043c", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/solve.png\"/></p></body></html>", None))
        self.label_62.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0442\u0456\u043c \u0432\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u043d\u0430 \u043f\u0430\u043d\u0435\u043b\u0456 \u043f\u0435\u0440\u0435\u0434\u0431\u0430\u0447\u0435\u043d\u043d\u044f \u0442\u0456 \u043f\u0443\u043d\u043a\u0442\u0438 \u044f\u043a\u0456 \u0432\u0430\u043c \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u0456", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0456 \u043d\u0430\u0442\u0438\u0441\u043d\u0456\u0442\u044c \"\u0412\u0438\u0440\u0456\u0448\u0438\u0442\u0438\" \u0442\u0430 \u0447\u0435\u043a\u0430\u0439\u0442\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442(~4\u0441.)", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u" \u0432\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u044f\u0434\u043a\u0438 \u0437 \u0437\u0430\u0432\u0434\u0430\u043d\u043d\u044f \u0442\u0430 \u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u044f\u0434\u043a\u0456\u0432 \u0437\u0456 \u0441\u043b\u043e\u0432\u0430\u043c\u0438 \u0432 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u043d\u0456 \u043f\u043e\u043b\u044f", None))
        self.label_61.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/predict_box2.png\"/></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/text.png\"/></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/row_cow.png\"/></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/predict_box.png\"/></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u0446\u0435\u0439 \u043f\u0443\u043d\u043a\u0442 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u043d\u0456\u0439 \u043f\u0430\u043d\u0435\u043b\u0456", None))
        self.label_58.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0432\u0456\u043c\u043a\u043d\u0443\u0442\u0438 \u0440\u0435\u0436\u0438\u043c \u043f\u0435\u0440\u0435\u0434\u0431\u0430\u0447\u0435\u043d\u043d\u044f", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/1.png\"/></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("Dialog", u"\u0422\u043e\u0434\u0456 \u0437'\u044f\u0432\u0438\u0442\u044c\u0441\u044f \u0446\u044f \u043f\u0430\u043d\u0435\u043b\u044c:", None))
        self.label_57.setText(QCoreApplication.translate("Dialog", u"\u042f\u043a\u0449\u043e \u0432\u0430\u043c \u043d\u0430\u043f\u0440\u0438\u043a\u043b\u0430\u0434 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0438\u0431\u0440\u0430\u0442\u0438 \u0440\u044f\u0434\u043e\u043a \u0432 \u044f\u043a\u043e\u043c\u0443 \u0432\u0441\u0456 \u0441\u043b\u043e\u0432\u0430 \u0436\u0456\u043d\u043e\u0447\u043e\u0433\u043e \u0442\u0430 \u0441\u0435\u0440\u0435\u0434\u043d\u044c\u043e\u0433\u043e \u0440\u043e\u0434\u0443", None))
        self.label_63.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/pre_1.png\"/></p></body></html>", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("Dialog", u"\u0420\u0456\u0434", None))
        self.label_43.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/solve.png\"/></p></body></html>", None))
        self.label_71.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0442\u0456\u043c \u0432\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u043d\u0430 \u043f\u0430\u043d\u0435\u043b\u0456 \u043f\u0435\u0440\u0435\u0434\u0431\u0430\u0447\u0435\u043d\u043d\u044f \u0442\u0456 \u043f\u0443\u043d\u043a\u0442\u0438 \u044f\u043a\u0456 \u0432\u0430\u043c \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u0456", None))
        self.label_44.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0456 \u043d\u0430\u0442\u0438\u0441\u043d\u0456\u0442\u044c \"\u0412\u0438\u0440\u0456\u0448\u0438\u0442\u0438\" \u0442\u0430 \u0447\u0435\u043a\u0430\u0439\u0442\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442(~4\u0441.)", None))
        self.label_45.setText(QCoreApplication.translate("Dialog", u" \u0432\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u044f\u0434\u043a\u0438 \u0437 \u0437\u0430\u0432\u0434\u0430\u043d\u043d\u044f \u0442\u0430 \u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u044f\u0434\u043a\u0456\u0432 \u0437\u0456 \u0441\u043b\u043e\u0432\u0430\u043c\u0438 \u0432 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u043d\u0456 \u043f\u043e\u043b\u044f", None))
        self.label_72.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/predict_box2.png\"/></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/text.png\"/></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/row_cow.png\"/></p></body></html>", None))
        self.label_73.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/predict_box.png\"/></p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u0446\u0435\u0439 \u043f\u0443\u043d\u043a\u0442 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u043d\u0456\u0439 \u043f\u0430\u043d\u0435\u043b\u0456", None))
        self.label_74.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0432\u0456\u043c\u043a\u043d\u0443\u0442\u0438 \u0440\u0435\u0436\u0438\u043c \u043f\u0435\u0440\u0435\u0434\u0431\u0430\u0447\u0435\u043d\u043d\u044f", None))
        self.label_49.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/2.png\"/></p></body></html>", None))
        self.label_75.setText(QCoreApplication.translate("Dialog", u"\u0422\u043e\u0434\u0456 \u0437'\u044f\u0432\u0438\u0442\u044c\u0441\u044f \u0446\u044f \u043f\u0430\u043d\u0435\u043b\u044c:", None))
        self.label_76.setText(QCoreApplication.translate("Dialog", u"\u042f\u043a\u0449\u043e \u0432\u0430\u043c \u043d\u0430\u043f\u0440\u0438\u043a\u043b\u0430\u0434 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0438\u0431\u0440\u0430\u0442\u0438 \u0440\u044f\u0434\u043e\u043a \u0432 \u044f\u043a\u043e\u043c\u0443 \u0432\u0441\u0456 \u0441\u043b\u043e\u0432\u0430 \u0432 \u043c\u043d\u043e\u0436\u0438\u043d\u0456", None))
        self.label_77.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/pre_2.png\"/></p></body></html>", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("Dialog", u"\u0427\u0438\u0441\u043b\u043e", None))
        self.label_50.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/solve.png\"/></p></body></html>", None))
        self.label_78.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0442\u0456\u043c \u0432\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u043d\u0430 \u043f\u0430\u043d\u0435\u043b\u0456 \u043f\u0435\u0440\u0435\u0434\u0431\u0430\u0447\u0435\u043d\u043d\u044f \u0442\u0456 \u043f\u0443\u043d\u043a\u0442\u0438 \u044f\u043a\u0456 \u0432\u0430\u043c \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u0456", None))
        self.label_51.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043b\u0456 \u043d\u0430\u0442\u0438\u0441\u043d\u0456\u0442\u044c \"\u0412\u0438\u0440\u0456\u0448\u0438\u0442\u0438\" \u0442\u0430 \u0447\u0435\u043a\u0430\u0439\u0442\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442(~4\u0441.)", None))
        self.label_52.setText(QCoreApplication.translate("Dialog", u" \u0432\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u044f\u0434\u043a\u0438 \u0437 \u0437\u0430\u0432\u0434\u0430\u043d\u043d\u044f \u0442\u0430 \u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u044f\u0434\u043a\u0456\u0432 \u0437\u0456 \u0441\u043b\u043e\u0432\u0430\u043c\u0438 \u0432 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u043d\u0456 \u043f\u043e\u043b\u044f", None))
        self.label_79.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/predict_box2.png\"/></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/text.png\"/></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/row_cow.png\"/></p></body></html>", None))
        self.label_80.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/predict_box.png\"/></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u0446\u0435\u0439 \u043f\u0443\u043d\u043a\u0442 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u043d\u0456\u0439 \u043f\u0430\u043d\u0435\u043b\u0456", None))
        self.label_81.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0432\u0456\u043c\u043a\u043d\u0443\u0442\u0438 \u0440\u0435\u0436\u0438\u043c \u043f\u0435\u0440\u0435\u0434\u0431\u0430\u0447\u0435\u043d\u043d\u044f", None))
        self.label_56.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/4.png\"/></p></body></html>", None))
        self.label_82.setText(QCoreApplication.translate("Dialog", u"\u0422\u043e\u0434\u0456 \u0437'\u044f\u0432\u0438\u0442\u044c\u0441\u044f \u0446\u044f \u043f\u0430\u043d\u0435\u043b\u044c:", None))
        self.label_83.setText(QCoreApplication.translate("Dialog", u"\u042f\u043a\u0449\u043e \u0432\u0430\u043c \u043d\u0430\u043f\u0440\u0438\u043a\u043b\u0430\u0434 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0438\u0431\u0440\u0430\u0442\u0438 \u0440\u044f\u0434\u043e\u043a \u0432 \u044f\u043a\u043e\u043c\u0443 \u0432\u0441\u0456 \u0441\u043b\u043e\u0432\u0430 \u0432 1 \u0442\u0430 4 \u0432\u0456\u0434\u043c\u0456\u043d\u0456", None))
        self.label_84.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/pre_4.png\"/></p></body></html>", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("Dialog", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\u0420\u0435\u0436\u0438\u043c \u043f\u0440\u0435\u0434\u0431\u0430\u0447\u0435\u043d\u043d\u044f", None))
        self.label_85.setText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u044f \u0442\u043e\u0433\u043e \u0449\u043e\u0431 \u0435\u043a\u0441\u043f\u043e\u0440\u0442\u0443\u0432\u0430\u0442\u0438 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e", None))
        self.label_86.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0439\u0442\u0438 \u0432 \"\u0424\u0430\u0439\u043b\" -> \"\u0415\u043a\u0441\u043f\u043e\u0440\u0442\u0443\u0432\u0430\u0442\u0438\"", None))
        self.label_87.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/instruction/export.png\"/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("Dialog", u"\u0415\u043a\u0441\u043f\u043e\u0440\u0442", None))
    # retranslateUi
