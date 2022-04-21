from PyQt5.QtWidgets import QDialog, QMainWindow

from gui import initial_interface
from main.user_manage import Manage, Register, Delete
from main.authenticate import Authenticate


class Initial(initial_interface.Ui_initial_interface, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initial = Initial()
        self.manage = Manage()
        self.register = Register()
        self.delete = Delete()
        self.authenticate = Authenticate()

        # connect
        self.initial.manage_pushbutton.clicked.connect(self.manage.show)
        self.initial.verification_pushbutton.clicked.connect(self.authenticate.show)

        self.manage.register_button.clicked.connect(self.register.show)
        self.manage.delete_button.clicked.connect(self.delete.show)
