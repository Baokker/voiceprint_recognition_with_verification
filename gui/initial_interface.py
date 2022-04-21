# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initial_interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initial_interface(object):
    def setupUi(self, initial_interface):
        initial_interface.setObjectName("initial_interface")
        initial_interface.resize(400, 600)
        initial_interface.setMinimumSize(QtCore.QSize(400, 600))
        initial_interface.setMaximumSize(QtCore.QSize(400, 600))
        self.login_Label = QtWidgets.QLabel(initial_interface)
        self.login_Label.setGeometry(QtCore.QRect(40, 90, 320, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.login_Label.setFont(font)
        self.login_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.login_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_Label.setObjectName("login_Label")
        self.manage_pushbutton = QtWidgets.QPushButton(initial_interface)
        self.manage_pushbutton.setGeometry(QtCore.QRect(90, 230, 211, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.manage_pushbutton.setFont(font)
        self.manage_pushbutton.setObjectName("manage_pushbutton")
        self.verification_pushbutton = QtWidgets.QPushButton(initial_interface)
        self.verification_pushbutton.setGeometry(QtCore.QRect(90, 370, 211, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.verification_pushbutton.setFont(font)
        self.verification_pushbutton.setObjectName("verification_pushbutton")

        self.retranslateUi(initial_interface)
        QtCore.QMetaObject.connectSlotsByName(initial_interface)

    def retranslateUi(self, initial_interface):
        _translate = QtCore.QCoreApplication.translate
        initial_interface.setWindowTitle(_translate("initial_interface", "Voiceprint Recognition"))
        initial_interface.setWhatsThis(_translate("initial_interface", "<html><head/><body><p>声纹识别系统</p></body></html>"))
        self.login_Label.setText(_translate("initial_interface", "声纹识别系统"))
        self.manage_pushbutton.setText(_translate("initial_interface", "用户管理"))
        self.verification_pushbutton.setText(_translate("initial_interface", "身份验证"))
