import sys

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow
)

from datacheking import LoginChecker, RegistrChecker
from services import LoginData, RegistrData
from bd_work import DataBaseManager


class Window(QMainWindow):
    def __init__(self):
        """Create mainwindow"""

        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.login_window = uic.loadUi('ui/logining.ui')
        self.registration_window = uic.loadUi('ui/registration.ui')
        self.sucsesfuly_window = uic.loadUi('ui/sucsesfully.ui')
        self.error_window = uic.loadUi('ui/error.ui')

        self.connect_button()
        self.bd_manager = DataBaseManager()
        self.is_logined = False

    def connect_button(self):
        """Connect button in main window"""

        # menu tab
        self.home_button.clicked.connect(self.go_home)
        self.timetable_button.clicked.connect(self.go_timetable)
        self.template_button.clicked.connect(self.go_template)
        # authorization
        self.login_button_cerkle.clicked.connect(self.authorization)
        self.login_button_text.clicked.connect(self.authorization)

    def go_home(self):
        """Switching tub to Home page"""

        self.stackedWidget.setCurrentIndex(0)

    def go_timetable(self):
        """Switching tub to Timetable page"""

        self.stackedWidget.setCurrentIndex(1)

    def go_template(self):
        """Switching tub to Template page"""

        self.stackedWidget.setCurrentIndex(2)

    def authorization(self):
        """Open authorization dialog window"""

        self.authorization_dialog = uic.loadUi('ui/authorization.ui')
        self.authorization_dialog.show()
        self.authorization_dialog.start_login_button.clicked.connect(self.logining)
        self.authorization_dialog.start_regisration_button.clicked.connect(self.registring)

    def logining(self):
        """Open login dialog window"""

        self.authorization_dialog.hide()
        self.login_window.show()
        self.data = self.get_log_data()
        self.finish_authorization(LoginChecker(self.data))

    def registring(self):
        """Open registration dialog window and hide authorization_dialog"""

        self.authorization_dialog.hide()
        self.registration_window.show()
        self.data = self.get_reg_data()
        self.finish_authorization(RegistrChecker(self.data))

    def sucsesfully_authorization(self):
        """Finsh sucsesfuly authorization process"""

        self.sucsesfuly_window.show()
        self.sucsesfuly_window.suc_button.clicked.connect(self.closing_windows)
        self.bd_manager.add_user(self.data)
        self.is_logined = True

    def closing_windows(self):
        """Close login-window after authorization"""

        if self.login_window.isHidden():
            self.registration_window.hide()
            self.sucsesfuly_window.hide()
        else:
            self.login_window.hide()
            self.sucsesfuly_window.hide()

    def error_authorization(self):
        """Show error message"""

        self.error_window.show()
        self.error_window.er_button.clicked.connect(self.error_window.hide)

    def finish_authorization(self, checker: LoginChecker | RegistrChecker):
        """Connect finfish-button for registr and login"""

        if type(checker) is RegistrChecker:
            if checker.is_correct:
                self.registration_window.go_sistem_button_reg.clicked.connect(self.sucsesfully_authorization)
            else:
                self.registration_window.go_sistem_button_reg.clicked.connect(self.error_authorization)
        elif type(checker) is LoginChecker:
            if checker.is_correct:
                self.login_window.go_sistem_button_log.clicked.connect(self.sucsesfully_authorization)
            else:
                self.login_window.go_sistem_button_log.clicked.connect(self.error_authorization)

    def get_log_data(self) -> LoginData:
        """Get user log-data for us checking"""

        return LoginData(
            self.login_window.login_lineEdit.text(),
            self.login_window.password_lineEdit.text()
        )

    def get_reg_data(self) -> RegistrData:
        """Get user reg-data for us checking"""

        return RegistrData(
            self.registration_window.FIO_lineEdit.text(),
            self.registration_window.login_lineEdit.text(),
            self.registration_window.concoct_pw_lineEdit.text(),
            self.registration_window.repeat_pw_lineEdit.text(),
            self.registration_window.school_num_lineEdit.text(),
            self.registration_window.building_num_lineEdit.text(),
            self.registration_window.phone_num_lineEdit.text()
        )

    def interface_change(self):
        """Change login-interface after successful authorization"""

        if self.is_logined:
            user_name = self.bd_manager.get_user_name()
            self.chonge_login_button_text(user_name)
            self.chonge_login_button_circle(user_name)

    def chonge_login_button_text(self, user_name: str):
        """Change login text button after successful authorization"""

        if len(user_name) > 8:
            user_name = user_name[0:9] + '...'
        self.login_button_text.setText(user_name)

    def chonge_login_button_circle(self, user_name: str):
        """Change login circle button after successful authorization"""

        self.login_button_cerkle.setText(user_name[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
