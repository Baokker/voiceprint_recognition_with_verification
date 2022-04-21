# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_success(object):
    def setupUi(self, success):
        success.setObjectName("success")
        success.resize(400, 600)
        success.setMinimumSize(QtCore.QSize(400, 600))
        success.setMaximumSize(QtCore.QSize(400, 600))
        self.result_label = QtWidgets.QLabel(success)
        self.result_label.setGeometry(QtCore.QRect(90, 80, 220, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.result_label.setFont(font)
        self.result_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        self.success_Label = QtWidgets.QLabel(success)
        self.success_Label.setGeometry(QtCore.QRect(60, 190, 271, 171))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.success_Label.setFont(font)
        self.success_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.success_Label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.success_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.success_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.success_Label.setWordWrap(True)
        self.success_Label.setObjectName("success_Label")
        self.back_pushbutton = QtWidgets.QPushButton(success)
        self.back_pushbutton.setGeometry(QtCore.QRect(160, 440, 60, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.back_pushbutton.setFont(font)
        self.back_pushbutton.setObjectName("back_pushbutton")

        self.retranslateUi(success)
        QtCore.QMetaObject.connectSlotsByName(success)

    def retranslateUi(self, success):
        _translate = QtCore.QCoreApplication.translate
        success.setWindowTitle(_translate("success", "Voiceprint Recognition"))
        self.result_label.setText(_translate("success", "识别结果"))
        self.success_Label.setText(_translate("success", "识别成功\n"
"\n"
"门已自动打开"))
        self.back_pushbutton.setText(_translate("success", "返回"))
