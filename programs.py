# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'programs.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from PySide2.QtCore import (QCoreApplication,QFile, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *

DATA_DIR = os.path.join(os.path.dirname(__file__),'data_dir')







class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(997, 702)
        MainWindow.setDocumentMode(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.actionTXT = QAction(MainWindow)
        self.actionTXT.setObjectName(u"actionTXT")
        self.actionJSON = QAction(MainWindow)
        self.actionJSON.setObjectName(u"actionJSON")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(70, 80, 871, 371))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAutoFillBackground(True)
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 181, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_number_of_words = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_number_of_words.setObjectName(u"lineEdit_number_of_words")

        self.gridLayout.addWidget(self.lineEdit_number_of_words, 1, 1, 1, 1)

        self.lineEdit_number_of_row = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_number_of_row.setObjectName(u"lineEdit_number_of_row")

        self.gridLayout.addWidget(self.lineEdit_number_of_row, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_rid = QRadioButton(self.gridLayoutWidget)
        self.radioButton_rid.setObjectName(u"radioButton_rid")
        self.radioButton_rid.setChecked(False)

        self.verticalLayout_2.addWidget(self.radioButton_rid)

        self.radioButton_chislo = QRadioButton(self.gridLayoutWidget)
        self.radioButton_chislo.setObjectName(u"radioButton_chislo")

        self.verticalLayout_2.addWidget(self.radioButton_chislo)

        self.radioButton_vidminok = QRadioButton(self.gridLayoutWidget)
        self.radioButton_vidminok.setObjectName(u"radioButton_vidminok")

        self.verticalLayout_2.addWidget(self.radioButton_vidminok)

        self.radioButton_vidmina = QRadioButton(self.gridLayoutWidget)
        self.radioButton_vidmina.setObjectName(u"radioButton_vidmina")

        self.verticalLayout_2.addWidget(self.radioButton_vidmina)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.pushButton_solve = QPushButton(self.groupBox_2)
        self.pushButton_solve.setObjectName(u"pushButton_solve")
        self.pushButton_solve.setGeometry(QRect(20, 260, 181, 71))
        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(260, 10, 611, 361))
        font = QFont()
        font.setFamily(u"Levenim MT")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 20, 441, 281))
        self.groupBox_predict = QGroupBox(self.groupBox)
        self.groupBox_predict.setObjectName(u"groupBox_predict")
        self.groupBox_predict.setEnabled(True)
        self.groupBox_predict.setGeometry(QRect(460, 20, 141, 281))
        self.groupBox_predict.setMinimumSize(QSize(0, 0))
        self.groupBox_predict.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_predict.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox_predict.setMouseTracking(False)
        self.groupBox_predict.setFocusPolicy(Qt.NoFocus)
        self.groupBox_predict.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.groupBox_predict.setAcceptDrops(False)
        self.groupBox_predict.setToolTipDuration(-4)
        self.groupBox_predict.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_predict.setAutoFillBackground(True)
        self.gridLayoutWidget_3 = QWidget(self.groupBox_predict)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 20, 121, 251))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_vidmina = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_vidmina.setObjectName(u"groupBox_vidmina")
        self.groupBox_vidmina.setEnabled(False)
        self.checkBox_vidm_1 = QCheckBox(self.groupBox_vidmina)
        self.checkBox_vidm_1.setObjectName(u"checkbox_vidm_1")
        self.checkBox_vidm_1.setGeometry(QRect(10, 20, 91, 17))
        self.checkBox_vidm_2 = QCheckBox(self.groupBox_vidmina)
        self.checkBox_vidm_2.setObjectName(u"checkbox_vidm_2")
        self.checkBox_vidm_2.setGeometry(QRect(10, 40, 91, 17))
        self.checkBox_vidm_3 = QCheckBox(self.groupBox_vidmina)
        self.checkBox_vidm_3.setObjectName(u"checkbox_vidm_3")
        self.checkBox_vidm_3.setGeometry(QRect(50, 20, 91, 17))
        self.checkBox_vidm_4 = QCheckBox(self.groupBox_vidmina)
        self.checkBox_vidm_4.setObjectName(u"checkbox_vidm_4")
        self.checkBox_vidm_4.setGeometry(QRect(50, 40, 91, 17))

        self.gridLayout_3.addWidget(self.groupBox_vidmina, 2, 0, 1, 1)

        self.groupBox_chislo = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_chislo.setObjectName(u"groupBox_chislo")
        self.groupBox_chislo.setEnabled(False)
        self.radioButton_5 = QRadioButton(self.groupBox_chislo)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(10, 20, 91, 17))
        self.radioButton_6 = QRadioButton(self.groupBox_chislo)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(10, 40, 81, 17))

        self.gridLayout_3.addWidget(self.groupBox_chislo, 1, 0, 1, 1)

        self.groupBox_rid = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_rid.setObjectName(u"groupBox_rid")
        self.groupBox_rid.setEnabled(False)
        self.checkBox_2 = QCheckBox(self.groupBox_rid)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 20, 91, 17))
        self.checkBox_3 = QCheckBox(self.groupBox_rid)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 40, 101, 17))
        self.checkBox_4 = QCheckBox(self.groupBox_rid)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(10, 60, 91, 17))

        self.gridLayout_3.addWidget(self.groupBox_rid, 0, 0, 1, 1)

        self.checkBox_predict = QCheckBox(self.groupBox_2)
        self.checkBox_predict.setObjectName(u"checkBox_predict")
        self.checkBox_predict.setGeometry(QRect(10, 190, 158, 17))
        self.checkBox_predict.setChecked(True)
        self.checkBox_predict.setTristate(False)

        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)

        self.msg.setStandardButtons(QMessageBox.Ok)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 997, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_3 = QMenu(self.menu)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action_6)
        self.menu_3.addAction(self.actionTXT)
        self.menu_3.addAction(self.actionJSON)
        self.menu_2.addAction(self.action)
        self.menu_2.addAction(self.action_about)
        self.menu_2.addSeparator()

        self.retranslateUi(MainWindow)
        self.radioButton_rid.toggled.connect(self.groupBox_rid.setEnabled)
        self.radioButton_chislo.toggled.connect(self.groupBox_chislo.setEnabled)
        self.radioButton_vidmina.toggled.connect(self.groupBox_vidmina.setEnabled)
        self.checkBox_predict.toggled.connect(self.groupBox_predict.setVisible)
        self.action_6.triggered.connect(MainWindow.close)


        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0406\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0456\u044f", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.actionTXT.setText(QCoreApplication.translate("MainWindow", u"TXT", None))
        self.actionJSON.setText(QCoreApplication.translate("MainWindow", u"JSON", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0445\u0456\u0434", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0434\u044c\u043b\u0430\u0441\u043a\u0430 \u0432\u0432\u0435\u0434\u0456\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u044f\u0434\u043a\u0456\u0432", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0441\u043b\u0456\u0432 \u0443 \u0440\u044f\u0434\u043a\u0443", None))
        self.radioButton_rid.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0456\u0434", None))
        self.radioButton_chislo.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e", None))
        self.radioButton_vidminok.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043c\u0456\u043d\u043e\u043a", None))
        self.radioButton_vidmina.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0430", None))
        self.pushButton_solve.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0440\u0456\u0448\u0438\u0442\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u044f\u0434\u043a\u0438 \u0456\u0437 \u0437\u0430\u0432\u0434\u0430\u043d\u043d\u044f", None))
        self.groupBox_predict.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0438\u043a\u0442\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.groupBox_vidmina.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0430", None))

        self.groupBox_chislo.setTitle(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043d\u043e\u0436\u0438\u043d\u0430", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0434\u043d\u0438\u043d\u0430", None))
        self.groupBox_rid.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0456\u0434", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0456\u043d\u043e\u0447\u0438\u0439", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u0427\u043e\u043b\u043e\u0432\u0456\u0447\u0438\u0439", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0435\u0434\u043d\u0456\u0439", None))
        self.checkBox_predict.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0438\u043a\u0442\u0443\u0432\u0430\u0442\u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442?", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0415\u043a\u0441\u043f\u043e\u0440\u0442\u0443\u0432\u0430\u0442\u0438", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0406\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0456\u044f", None))

        self.checkBox_vidm_1.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.checkBox_vidm_2.setText(QCoreApplication.translate("MainWindow", u"II", None))
        self.checkBox_vidm_3.setText(QCoreApplication.translate("MainWindow", u"III", None))
        self.checkBox_vidm_4.setText(QCoreApplication.translate("MainWindow", u"IV", None))
    # retranslateUi
