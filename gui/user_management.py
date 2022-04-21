# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_management.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_management(object):
    def setupUi(self, user_management):
        user_management.setObjectName("user_management")
        user_management.resize(400, 600)
        user_management.setMinimumSize(QtCore.QSize(400, 600))
        user_management.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setPointSize(11)
        user_management.setFont(font)
        self.user_manage_label = QtWidgets.QLabel(user_management)
        self.user_manage_label.setGeometry(QtCore.QRect(80, 90, 220, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.user_manage_label.setFont(font)
        self.user_manage_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.user_manage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_manage_label.setObjectName("user_manage_label")
        self.back_pushbutton = QtWidgets.QPushButton(user_management)
        self.back_pushbutton.setGeometry(QtCore.QRect(20, 20, 60, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.back_pushbutton.setFont(font)
        self.back_pushbutton.setObjectName("back_pushbutton")
        self.register_button = QtWidgets.QPushButton(user_management)
        self.register_button.setGeometry(QtCore.QRect(100, 220, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.register_button.setFont(font)
        self.register_button.setIconSize(QtCore.QSize(27, 27))
        self.register_button.setObjectName("register_button")
        self.delete_button = QtWidgets.QPushButton(user_management)
        self.delete_button.setGeometry(QtCore.QRect(100, 350, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")

        self.retranslateUi(user_management)
        QtCore.QMetaObject.connectSlotsByName(user_management)

    def retranslateUi(self, user_management):
        _translate = QtCore.QCoreApplication.translate
        user_management.setWindowTitle(_translate("user_management", "Voiceprint Recognition"))
        self.user_manage_label.setText(_translate("user_management", "用户管理"))
        self.back_pushbutton.setText(_translate("user_management", "返回"))
        self.register_button.setText(_translate("user_management", "注册用户"))
        self.delete_button.setText(_translate("user_management", "用户删除"))
