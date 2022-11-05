import sys

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

from datacheking import LoginCheker

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
        self.authorization_dialog.start_login_button.clicked.connect(self.login)
        self.authorization_dialog.start_regisration_button.clicked.connect(self.registration)

    def login(self):
        """Open login dialog window"""
        self.authorization_dialog.hide()
        self.login_dialog = uic.loadUi('ui/logining.ui')
        self.login_dialog.show()
        correct = LoginCheker()
        if correct:
            self.login_dialog.go_sistem_button_log.clicked.connect(self.sucsesfully_authorization)
        if not correct:
            self.registration_dialog.go_sistem_button_log.clicked.connect(self.error_authorization)

    def registration(self):
        """Open registration dialog window and hide authorization_dialog"""
        self.authorization_dialog.hide()
        self.registration_dialog = uic.loadUi('ui/registration.ui')
        self.registration_dialog.show()
        self.chek_corect_reg_data()
        if False:
            self.registration_dialog.go_sistem_button_reg.clicked.connect(self.sucsesfully_authorization)
        if True:
            self.registration_dialog.go_sistem_button_reg.clicked.connect(self.error_authorization)

    def sucsesfully_authorization(self):
        """Finsh sucsesfuly authorization process"""
        self.sucsesfuly_dialog = uic.loadUi('ui/sucsesfully.ui')
        self.sucsesfuly_dialog.show()
        if self.sender() == self.registration_dialog.go_sistem_button_reg:
            self.registration_dialog.hide()
        elif self.sender() == self.registration_dialog.go_sistem_button_log:
            self.login_dialog.hide()
        self.ending()

    def error_authorization(self):
        """Show error message"""
        self.sucsesfuly_dialog = uic.loadUi('ui/error.ui')
        self.sucsesfuly_dialog.show()

    def ending(self):
        """Finish authorization"""
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
