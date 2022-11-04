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
        # menu tub button connect
        self.init_menu_tub_button()
        # menu logining button connect
        self.init_logining_button()

        # can user edit data or not
        self.login

    def init_menu_tub_button(self):
        self.home_button.clicked.connect(self.go_home)
        self.timetable_button.clicked.connect(self.go_timetable)
        self.template_button.clicked.connect(self.go_template)

    def init_logining_button(self):
        self.login_button_cerkle.clicked.connect(self.start_login)
        self.login_button_text.clicked.connect(self.start_login)

    def go_home(self):
        self.stackedWidget.setCurrentIndex(0)

    def go_timetable(self):
        self.stackedWidget.setCurrentIndex(1)

    def go_template(self):
        self.stackedWidget.setCurrentIndex(2)

    def start_login(self):
        self.dialog = uic.loadUi('login.ui')
        self.dialog.go_button.clivked.connect(self.sucdesfuly_login)
        self.dialog.show()

    def sucdesfuly_login(self):
        # saving data
        self.user_login = self.dialog.lineEdit_login.text()
        self.user_password = self.dialog.lineEdit_passowrd.text()

        # hide dialog and
        self.dialog.hide()

        # edit programm funtions



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
