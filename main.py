import sys

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        # button connect
        self.init_button()

        # can user edit data or not
        self.is_logined = False

    def init_button(self):
        # menu tab
        self.home_button.clicked.connect(self.go_home)
        self.timetable_button.clicked.connect(self.go_timetable)
        self.template_button.clicked.connect(self.go_template)
        # authorization
        self.login_button_cerkle.clicked.connect(self.authorization)
        self.login_button_text.clicked.connect(self.authorization)

    def go_home(self):
        self.stackedWidget.setCurrentIndex(0)

    def go_timetable(self):
        self.stackedWidget.setCurrentIndex(1)

    def go_template(self):
        self.stackedWidget.setCurrentIndex(2)

    def authorization(self):
        self.authorization_dialog = uic.loadUi('authorization.ui')
        self.authorization_dialog.show()
        self.authorization_dialog.start_login_button.clicked.connect(self.login)
        self.authorization_dialog.start_regisration_button.clicked.connect(self.registration)

    def login(self):
        self.authorization_dialog.hide()
        self.login_dialog = uic.loadUi('logining.ui')
        self.login_dialog.show()
        self.login_dialog.go_sistem_button_log.clicked.connect(self.sucdesfuly_authorization)

    def registration(self):
        self.authorization_dialog.hide()
        self.registration_dialog = uic.loadUi('registration.ui')
        self.registration_dialog.show()
        self.registration_dialog.go_sistem_button_reg.clicked.connect(self.sucdesfuly_authorization)

    def sucdesfuly_authorization(self):
        if self.login_dialog.isHidden():
            self.registration_dialog.hide()
        elif self.registration_dialog.isHidden():
            self.login_dialog.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
