# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_register.ui'
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
        self.register_Label = QtWidgets.QLabel(user_register)
        self.register_Label.setGeometry(QtCore.QRect(80, 90, 220, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.register_Label.setFont(font)
        self.register_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.register_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.register_Label.setObjectName("register_Label")
        self.name_reminder_label = QtWidgets.QLabel(user_register)
        self.name_reminder_label.setGeometry(QtCore.QRect(60, 200, 111, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.name_reminder_label.setFont(font)
        self.name_reminder_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.name_reminder_label.setObjectName("name_reminder_label")
        self.nameinput_lineedit = QtWidgets.QLineEdit(user_register)
        self.nameinput_lineedit.setGeometry(QtCore.QRect(190, 220, 131, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.nameinput_lineedit.setFont(font)
        self.nameinput_lineedit.setObjectName("nameinput_lineedit")
        self.record_reminder_label = QtWidgets.QLabel(user_register)
        self.record_reminder_label.setGeometry(QtCore.QRect(50, 300, 271, 141))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.record_reminder_label.setFont(font)
        self.record_reminder_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.record_reminder_label.setWordWrap(True)
        self.record_reminder_label.setObjectName("record_reminder_label")
        self.record_pushbutton = QtWidgets.QPushButton(user_register)
        self.record_pushbutton.setGeometry(QtCore.QRect(170, 480, 60, 60))
        self.record_pushbutton.setObjectName("record_pushbutton")
        self.back_pushbutton = QtWidgets.QPushButton(user_register)
        self.back_pushbutton.setGeometry(QtCore.QRect(20, 20, 60, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.back_pushbutton.setFont(font)
        self.back_pushbutton.setObjectName("back_pushbutton")

        self.retranslateUi(user_register)
        QtCore.QMetaObject.connectSlotsByName(user_register)

    def retranslateUi(self, user_register):
        _translate = QtCore.QCoreApplication.translate
        user_register.setWindowTitle(_translate("user_register", "Voiceprint Recognition"))
        self.register_Label.setText(_translate("user_register", "用户注册"))
        self.name_reminder_label.setText(_translate("user_register", "请输入姓名："))
        self.nameinput_lineedit.setText(_translate("user_register", "your_name"))
        self.record_reminder_label.setText(_translate("user_register", "点击[录音]按钮后\n"
"\n"
"清晰读出0,1,2,3,4,5,6,7,8,9\n"
"\n"
"重复三遍后点击[保存]"))
        self.record_pushbutton.setText(_translate("user_register", "录音"))
        self.back_pushbutton.setText(_translate("user_register", "返回"))
