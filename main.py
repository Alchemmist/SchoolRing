import sys

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QStackedLayout,
    QInputDialog
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.number = ''
        uic.loadUi('mu_ui_test.ui', self)
        self.QInputDialog = uic.loadUi('mu_ui_sest_dialog_login.ui', self)

        # menu tub button connect
        self.init_menu_tub_button()
        # menu logining button connect
        self.init_logining_button()

    def init_menu_tub_button(self):
        self.home_button.clicked.connect(self.go_home)
        self.timetable_button.clicked.connect(self.go_timetable)
        self.timetable_button.clicked.connect(self.go_timetable)

    def init_logining_button(self):
        self.login_button_cerkle.clicked.connect(self.start_login)
        self.login_button_text.clicked.connect(self.start_login)

    def go_home(self):
        self.tabs.setCurrentIndex(self.label.page - 1)

    def go_timetable(self):
        self.tabs.setCurrentIndex(self.comboBox.page - 1)

    def go_template(self):
        self.tabs.setCurrentIndex(self.pushButton_2.page - 1)

    def start_login(self):
        self.QInputDialog.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
