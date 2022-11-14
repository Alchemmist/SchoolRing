import datetime
import sys
import threading

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QGroupBox
)
from PyQt6 import QtGui, QtWidgets

from base_of_data import DataBaseManager
from datacheking import LoginChecker, RegistrChecker
from services import LoginData, RegistrData
from services import ringsystem_power, serch_time_for_nearest_ring

# Encoding for the time module with days of the week
translator_of_weekday = {
    0: 'Понедельник',
    1: 'Вторник',
    2: 'Среда',
    3: 'Четверг',
    4: 'Пятница',
    5: 'Суббота',
    6: 'Воскресенье',
}


class Window(QMainWindow):
    """Main user interaction window"""

    def __init__(self):
        """Create mainwindow"""

        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.initUI()

    def initUI(self):
        """Program initialization"""

        uic.loadUi('ui/main.ui', self)
        self.is_logined = False
        self.load_ui()

        self.connect_button()
        self.bd_manager = DataBaseManager()
        self.set_data_on_interface()

    def set_data_on_interface(self):
        """Displays all the necessary information, individually for the user"""

        self.set_items_to_scrolarea()
        self.set_item_to_today_widget()
        self.set_item_to_nearest_widget()

    def load_ui(self):
        """Loads and saves all dialogs in the application"""

        self.login_window = uic.loadUi('ui/logining.ui')
        self.registration_window = uic.loadUi('ui/registration.ui')
        self.sucsesfuly_window = uic.loadUi('ui/sucsesfully.ui')
        self.error_window = uic.loadUi('ui/error.ui')
        self.authorization_window = uic.loadUi('ui/authorization.ui')
        self.create_schedule_window = uic.loadUi('ui/create_schedule.ui')

    def connect_button(self):
        """Connect button in main window"""

        # menu tab
        self.home_button.clicked.connect(self.go_home)
        self.timetable_button.clicked.connect(self.go_timetable)
        self.template_button.clicked.connect(self.go_template)
        # authorization
        self.login_button_cerkle.clicked.connect(self.authorization)
        self.login_button_text.clicked.connect(self.authorization)
        # timetable
        self.create_schedule_button.clicked.connect(self.create_schedule)
        # self.edit_schedule_button.clicked.connect(self.edit_schedule)
        # # template
        # self.add_template_button.clicked.connect(self.create_template)
        # self.???.clicked.connect(self.edit_template)

    def go_home(self):
        """Switching tub to Home page"""

        self.stackedWidget.setCurrentIndex(0)
        self.set_item_to_nearest_widget()

    def go_timetable(self):
        """Switching tub to Timetable page"""

        self.stackedWidget.setCurrentIndex(1)

    def go_template(self):
        """Switching tub to Template page"""

        self.stackedWidget.setCurrentIndex(2)

    def authorization(self):
        """Open authorization dialog window"""

        self.authorization_window.show()
        self.authorization_window.start_login_button.clicked.connect(self.logining)
        self.authorization_window.start_regisration_button.clicked.connect(self.registring)

    def logining(self):
        """Open login dialog window"""

        self.authorization_window.hide()
        self.login_window.show()
        # self.try_logining()
        self.login_window.go_sistem_button_log.clicked.connect(self.finish_login)

    def registring(self):
        """Open registration dialog window and hide authorization_dialog"""

        self.authorization_window.hide()
        self.registration_window.show()
        self.registration_window.go_sistem_button_reg.clicked.connect(self.finish_registration)

    def sucsesfully_login(self):
        """Defines the program's actions after successful authorization"""

        self.sucsesfuly_window.show()
        self.sucsesfuly_window.suc_button.clicked.connect(self.closing_windows)
        self.is_logined = True
        self.change_interface(self.bd_manager.get_FIO(self.data.login)[0])

    def sucsesfully_registration(self):
        """Finsh sucsesfuly authorization process"""

        self.sucsesfuly_window.show()
        self.sucsesfuly_window.suc_button.clicked.connect(self.closing_windows)
        self.bd_manager.add_user(self.data)
        self.is_logined = True
        self.change_interface(self.data.FIO)

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

    def finish_registration(self):
        """Connect finfish-button for registr and login"""

        self.data = self.get_reg_data()
        checker = RegistrChecker(self.data)
        if checker.is_correct:
            self.sucsesfully_registration()
        else:
            self.error_authorization()

    def finish_login(self):
        """Verification of data and completion of authorization"""

        self.data = self.get_log_data()
        checker = LoginChecker(self.data)
        if checker.is_correct:
            self.sucsesfully_login()
        else:
            self.error_authorization()

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

    def change_interface(self, FIO: str):
        """Change interface after successful authorization"""
        name = FIO.strip().split()[1]
        if len(name) > 8:
            name = name[0:7] + '...'
        self.login_button_text.setText(name)
        self.login_button_cerkle.setText(name[0])

    def set_items_to_home(self):
        """Displaying actual data on widgets on a home page"""

        self.set_items_to_scrolarea()
        self.set_item_to_widget()

    def set_items_to_scrolarea(self):
        """Displaying data to scrollarea"""

        self.today_sched = self.bd_manager.get_schedule_today()
        self.today_sched = sorted(self.today_sched, key=lambda x: x[0])
        layout = QHBoxLayout()
        for i in self.today_sched:
            widget = uic.loadUi('ui/frame_for_home.ui')
            widget.title.setText(i[2])
            widget.time.setText(i[0])
            widget.music.setText(i[1])
            layout.addWidget(widget)
        group_box = QGroupBox()
        group_box.setStyleSheet(
            'border: 0px'
        )
        group_box.setLayout(layout)
        self.scrollArea.setWidget(group_box)
        self.scrollArea.setWidgetResizable(True)

    def set_item_to_today_widget(self):
        """Displaying data to status widget with date"""

        self.today_label.setText(
            f'{translator_of_weekday[datetime.datetime.today().weekday()]}\n'
            f'{datetime.date.today().strftime("%d-%m-%Y")}'
        )

    def set_item_to_nearest_widget(self):
        """Displaying data to status widget with nearst ring"""

        tm, music = serch_time_for_nearest_ring(self.today_sched)
        self.nearest_label.setText(
            f'Через {tm} минут прозвенит {music[0:-4]}'
        )

    def create_schedule(self):
        self.create_schedule_window.show()
        self.fill_combobox()
        self.set_date()

    def fill_combobox(self):
        for i in self.bd_manager.get_list_template():
            self.create_schedule_window.templates_combobox.addItem(i[0])
        self.create_schedule_window.templates_combobox.currentTextChanged.connect(self.chenge_tableitem_as_template)

    def set_date(self):
        self.create_schedule_window.dateEdit.setDisplayFormat("dd-MM-yyyy")
        self.create_schedule_window.dateEdit.setDate(datetime.date.today())

    def chenge_tableitem_as_template(self):
        self.template = self.bd_manager.get_schedule(self.create_schedule_window.templates_combobox.currentText())
        self.create_schedule_window.tableWidget.setRowCount(len(self.template))
        for i, value in enumerate(self.template):
            self.create_schedule_window.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(value[0]))
            self.create_schedule_window.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(value[1]))
            self.create_schedule_window.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(value[2]))
        self.create_schedule_window.finish_creating_button.clicked.connect(self.finish_creating_schedule)

    def finish_creating_schedule(self):
        self.save_schedule()
        self.create_schedule_window.hide()
        # self.add_to_timetable()

    def save_schedule(self):
        rows = self.create_schedule_window.tableWidget.rowCount()
        cols = self.create_schedule_window.tableWidget.columnCount()
        for row in range(rows):
            finish = []
            for col in range(cols):
                try:
                    finish.append(self.create_schedule_window.tableWidget.item(row, col).text())
                except:
                    pass
            print(finish)
            self.bd_manager.save_shedule_row(finish)


def windiw_power():
    """Starts a thread with an image of a windowed application"""

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    vew_window = threading.Thread(target=windiw_power)
    ring_power = threading.Thread(target=ringsystem_power)

    ring_power.start()
    vew_window.start()
    vew_window.join()
    ring_power.join()
