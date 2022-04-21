# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_delete.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_register(object):
    def setupUi(self, user_register):
        user_register.setObjectName("user_register")
        user_register.resize(400, 600)
        user_register.setMinimumSize(QtCore.QSize(400, 600))
        user_register.setMaximumSize(QtCore.QSize(400, 600))
        self.delete_label = QtWidgets.QLabel(user_register)
        self.delete_label.setGeometry(QtCore.QRect(80, 80, 220, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.delete_label.setFont(font)
        self.delete_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.delete_label.setAlignment(QtCore.Qt.AlignCenter)
        self.delete_label.setObjectName("delete_label")
        self.back_pushbutton = QtWidgets.QPushButton(user_register)
        self.back_pushbutton.setGeometry(QtCore.QRect(20, 20, 60, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.back_pushbutton.setFont(font)
        self.back_pushbutton.setObjectName("back_pushbutton")
        self.listView = QtWidgets.QListView(user_register)
        self.listView.setGeometry(QtCore.QRect(40, 240, 301, 291))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(user_register)
        self.label.setGeometry(QtCore.QRect(100, 170, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(user_register)
        QtCore.QMetaObject.connectSlotsByName(user_register)

    def retranslateUi(self, user_register):
        _translate = QtCore.QCoreApplication.translate
        user_register.setWindowTitle(_translate("user_register", "Voiceprint Recognition"))
        self.delete_label.setText(_translate("user_register", "删除用户"))
        self.back_pushbutton.setText(_translate("user_register", "返回"))
        self.label.setText(_translate("user_register", "点击即可删除"))
