# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(628, 506)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.teContent = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.teContent.setFont(font)
        self.teContent.setObjectName("teContent")
        self.verticalLayout.addWidget(self.teContent)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbOpen = QtWidgets.QPushButton(Form)
        self.pbOpen.setObjectName("pbOpen")
        self.horizontalLayout.addWidget(self.pbOpen)
        self.pbSave = QtWidgets.QPushButton(Form)
        self.pbSave.setObjectName("pbSave")
        self.horizontalLayout.addWidget(self.pbSave)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Secret Editor"))
        self.pbOpen.setText(_translate("Form", "Open secret"))
        self.pbSave.setText(_translate("Form", "Save secret"))


