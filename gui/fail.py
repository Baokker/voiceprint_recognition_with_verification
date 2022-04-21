# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fail.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fail(object):
    def setupUi(self, fail):
        fail.setObjectName("fail")
        fail.resize(400, 600)
        fail.setMinimumSize(QtCore.QSize(400, 600))
        fail.setMaximumSize(QtCore.QSize(400, 600))
        self.result_label = QtWidgets.QLabel(fail)
        self.result_label.setGeometry(QtCore.QRect(90, 80, 220, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.result_label.setFont(font)
        self.result_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.result_label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        self.fail_label = QtWidgets.QLabel(fail)
        self.fail_label.setGeometry(QtCore.QRect(70, 200, 251, 171))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.fail_label.setFont(font)
        self.fail_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fail_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fail_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fail_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fail_label.setWordWrap(True)
        self.fail_label.setObjectName("fail_label")
        self.back_pushbutton = QtWidgets.QPushButton(fail)
        self.back_pushbutton.setGeometry(QtCore.QRect(160, 440, 60, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.back_pushbutton.setFont(font)
        self.back_pushbutton.setObjectName("back_pushbutton")

        self.retranslateUi(fail)
        QtCore.QMetaObject.connectSlotsByName(fail)

    def retranslateUi(self, fail):
        _translate = QtCore.QCoreApplication.translate
        fail.setWindowTitle(_translate("fail", "Voiceprint Recognition"))
        self.result_label.setText(_translate("fail", "识别结果"))
        self.fail_label.setText(_translate("fail", "对不起\n"
"\n"
"非注册用户"))
        self.back_pushbutton.setText(_translate("fail", "返回"))
