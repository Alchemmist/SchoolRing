import sys

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow
)

from datacheking import LoginChecker, RegistrChecker
from services import LoginData, RegistrData


class Window(QMainWindow):
    def __init__(self):
        """Create mainwindow"""

        super().__init__()
        uic.loadUi('ui/main.ui', self)
        # button connect
        self.init_button()
        # can user edit data or not
        self.is_logined = False

    def init_button(self):
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
        self.login_dialog = uic.loadUi('ui/logining.ui')
        self.login_dialog.show()
        self.finish_authorization(LoginChecker(self.get_log_data()))

    def registring(self):
        """Open registration dialog window and hide authorization_dialog"""

        self.authorization_dialog.hide()
        self.registration_dialog = uic.loadUi('ui/registration.ui')
        self.registration_dialog.show()
        self.finish_authorization(RegistrChecker(self.get_reg_data()))

    def sucsesfully_authorization(self):
        """Finsh sucsesfuly authorization process"""

        self.sucsesfuly_dialog = uic.loadUi('ui/sucsesfully.ui')
        self.sucsesfuly_dialog.show()
        self.sucsesfuly_dialog.suc_button.clicked.connect(self.clozing_windows)

        # self.interface_change()
        self.is_logined = True

    def clozing_windows(self):
        if self.login_dialog.isHidden():
            self.registration_dialog.hide()
            self.sucsesfuly_dialog.hide()
        else:
            self.login_dialog.hide()
            self.sucsesfuly_dialog.hide()

    def error_authorization(self):
        """Show error message"""

        self.error_dialog = uic.loadUi('ui/error.ui')
        self.error_dialog.show()
        self.error_dialog.er_button.clicked.connect(self.error_dialog.hide)

    def finish_authorization(self, checker: LoginChecker | RegistrChecker):
        """Connect finfish-button for registr and login"""

        if type(checker) is RegistrChecker:
            if checker.status:
                self.registration_dialog.go_sistem_button_reg.clicked.connect(self.sucsesfully_authorization)
            else:
                self.registration_dialog.go_sistem_button_reg.clicked.connect(self.error_authorization)
        elif type(checker) is LoginChecker:
            if checker.status:
                self.login_dialog.go_sistem_button_log.clicked.connect(self.sucsesfully_authorization)
            else:
                self.login_dialog.go_sistem_button_log.clicked.connect(self.error_authorization)

    def get_log_data(self) -> LoginData:
        """Get user log-data for us checking"""

        return LoginData(
            self.login_dialog.login_lineEdit.text(),
            self.login_dialog.password_lineEdit.text()
        )

    def get_reg_data(self) -> RegistrData:
        """Get user reg-data for us checking"""

        return RegistrData(
            self.registration_dialog.FIO_lineEdit.text(),
            self.registration_dialog.login_lineEdit.text(),
            self.registration_dialog.concoct_pw_lineEdit.text(),
            self.registration_dialog.repeat_pw_lineEdit.text(),
            self.registration_dialog.school_num_lineEdit.text(),
            self.registration_dialog.building_num_lineEdit.text(),
            self.registration_dialog.phone_num_lineEdit.text()
        )

    def interface_change(self):
        self.chonge_login_button_text()
        self.chonge_login_button_cerkle()

    def chonge_login_button_text(self):
        self.login_button_text.setText()

    def chonge_login_button_cerkle(self):
        pass

    def save_registratin_data(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
