import os
import shutil

from PyQt5 import QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QDialog, QMessageBox

from gui import user_management, user_register, user_delete

from record_audio import record_with_pyaudio

class Manage(user_management.Ui_user_management, QDialog):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.back_pushbutton.clicked.connect(self.close)


class Register(user_register.Ui_user_register, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_pushbutton.clicked.connect(self.close)
        self.record_pushbutton.clicked.connect(self.record_data)

    def record_data(self):
        import os

        name = self.nameinput_lineedit.text()
        if len(name) == 0 or name.isspace():
            msg = QtWidgets.QMessageBox.information(self, '提示', '文本栏为空！\n请先输入用户名')
            return

        if not os.path.exists(os.path.join(os.curdir, "enroll")):
            os.makedirs(os.path.join(os.curdir, "enroll"))

        enroll_user_dir = os.path.join(os.curdir, "enroll", name)

        if not os.path.exists(enroll_user_dir):
            os.makedirs(enroll_user_dir)

        file1_name = name + '_record1.wav'
        file2_name = name + '_record2.wav'
        file3_name = name + '_record3.wav'

        if os.path.exists(os.path.join(enroll_user_dir, file3_name)):
            msg = QtWidgets.QMessageBox.information(self, '提示', '此用户已经收集数据完毕！')
            return
        elif os.path.exists(os.path.join(enroll_user_dir, file2_name)):
            msg = QtWidgets.QMessageBox.information(self, '提示', '按下OK开始录音!\n0 1 2 3 4 5 6 7 8 9')
            record_with_pyaudio(os.path.join(enroll_user_dir, file3_name))
            msg = QtWidgets.QMessageBox.information(self, '提示', '录音完成！')
        elif os.path.exists(os.path.join(enroll_user_dir, file1_name)):
            msg = QtWidgets.QMessageBox.information(self, '提示', '按下OK开始录音!\n0 1 2 3 4 5 6 7 8 9')
            record_with_pyaudio(os.path.join(enroll_user_dir, file2_name))
            msg = QtWidgets.QMessageBox.information(self, '提示', '录音完成！')
        else:
            msg = QtWidgets.QMessageBox.information(self, '提示', '按下OK开始录音!\n0 1 2 3 4 5 6 7 8 9')
            record_with_pyaudio(os.path.join(enroll_user_dir, file1_name))
            msg = QtWidgets.QMessageBox.information(self, '提示', '录音完成！')


class Delete(user_delete.Ui_user_register, QDialog):
    def __init__(self):
        super().__init__()
        self.qList = None
        self.setupUi(self)
        self.back_pushbutton.clicked.connect(self.close)
        self.listView.clicked.connect(self.delete_user)
        self.update_user()

    def update_user(self):
        # 实例化列表模型，添加数据
        slm = QStringListModel()
        users_path = os.path.join(os.curdir, "enroll")

        users = []
        if not os.path.exists(os.path.join(os.curdir, "enroll")):
            os.makedirs(os.path.join(os.curdir, "enroll"))

        for file in os.listdir(users_path):
            d = os.path.join(users_path, file)
            if os.path.isdir(d):
                users.append(os.path.basename(d))

        self.qList = users

        slm.setStringList(self.qList)
        self.listView.setModel(slm)

    def delete_user(self, qModelIndex):
        # 提示信息弹窗，你选择的信息
        ret = QMessageBox.question(self, '', "Are you sure to delete " + self.qList[qModelIndex.row()] + "?",
                                   QMessageBox.Yes | QMessageBox.No)

        if ret == QMessageBox.Yes:
            shutil.rmtree(os.path.join(os.curdir, "enroll", self.qList[qModelIndex.row()]))
            self.update_user()

    def show(self):
        self.update_user()
        super().show()
