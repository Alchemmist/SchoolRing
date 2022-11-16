import datetime
import sys
import threading

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QGroupBox,
    QRadioButton,
    QVBoxLayout,
    QGridLayout,
    QFileDialog
)
from PyQt6 import QtGui, QtWidgets

from base_of_data import DataBaseManager

from datacheking import LoginChecker, RegistrChecker
from datacheking import PhoneError, PasswordError, FIOError, SchoolError, LoginError

from services import LoginData, RegistrData
from services import ringsystem_power, serch_time_for_nearest_ring

from time import sleep

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
        self.defoult_template = ''
        self.load_ui()

        self.connect_button()
        self.bd_manager = DataBaseManager()
        self.set_data_on_interface()

    def set_data_on_interface(self):
        """Displays all the necessary information, individually for the user"""

        self.set_items_to_home()
        self.set_item_to_template()
        self.set_item_to_timetable()

    def load_ui(self):
        """Loads and saves all dialogs in the application"""

        self.login_window = uic.loadUi('ui/logining.ui')
        self.registration_window = uic.loadUi('ui/registration.ui')
        self.sucsesfuly_window = uic.loadUi('ui/sucsesfully.ui')
        self.error_window = uic.loadUi('ui/error.ui')
        self.authorization_window = uic.loadUi('ui/authorization.ui')

        self.set_schedule_on_day_window = uic.loadUi('ui/set_schedul_on_day.ui')
        self.delete_schedule_on_day_window = uic.loadUi('ui/delete_schedul_on_day.ui')
        self.edit_schedule_on_day_window = uic.loadUi('ui/edit_schedul_on_day.ui')

        self.choose_defoult_template = uic.loadUi('ui/choose_defoult_templateui.ui')
        self.templ = uic.loadUi('ui/one_template.ui')
        self.add_templ = uic.loadUi('ui/add_template_frame.ui')
        self.active_schedule_window = uic.loadUi('ui/active_schedule.ui')
        self.naming_temp = uic.loadUi('ui/get_name_templ.ui')

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
        # self.edit_schedule_button.add_schedule_button.clicked.connect(self.add_special_day)
        # self.edit_schedule_on_day.add_schedule_button.clicked.connect(self.edit_special_day)
        # self.delete_schedule_on_day.ok_delete_button.clicked.connect(self.delete_special_day)
        # self.edit_schedule_button.clicked.connect(self.edit_schedule)
        # # template
        self.edit_defoult_button.clicked.connect(self.change_defoult_template)
        self.add_templ.new_template_button.clicked.connect(self.create_template)
        # self.add_template_button.clicked.connect(self.create_template)
        # self.???.clicked.connect(self.edit_template)

    def go_home(self):
        """Switching tub to Home page"""

        self.stackedWidget.setCurrentIndex(0)
        self._init_nearest_widget()

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

        try:
            self.data = self.get_reg_data()
            checker = RegistrChecker(self.data)
            print(checker.is_correct)
            if checker.is_correct:
                self.sucsesfully_registration()
        except PhoneError:
            self.error_authorization()
            self.error_window.message_label.setText('Please check if you have entered your phone number correctly')
        except PasswordError:
            self.error_window.message_label.setText("Please check if you have entered your password correctly")
            self.error_authorization()
        except FIOError:
            self.error_window.message_label.setText('Please check if you have entered your FIO correctly')
            self.error_authorization()
        except SchoolError:
            self.error_window.message_label.setText('Please check if you have entered your '
                                                    'school or building number correctly')
            self.error_authorization()
        except LoginError:
            self.error_window.message_label.setText('This login already used')
            self.error_authorization()

    def finish_login(self):
        """Verification of data and completion of authorization"""

        try:
            self.data = self.get_log_data()
            checker = LoginChecker(self.data)
            if checker.is_correct:
                self.sucsesfully_login()
        except LoginError:
            self.error_window.message_label.setText('Please check if you have entered your login correctly')
            self.error_authorization()
        except PasswordError:
            self.error_window.message_label.setText('Please check if you have entered your password correctly')
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

        self._init_homescroll()
        self._init_today_widget()
        self._init_nearest_widget()

    def _init_homescroll(self):
        """Displaying data to scrollarea on Home page"""

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

    def _init_today_widget(self):
        """Displaying data to status widget with date"""

        self.today_label.setText(
            f'{translator_of_weekday[datetime.datetime.today().weekday()]}\n'
            f'{datetime.date.today().strftime("%d-%m-%Y")}'
        )

    def _init_nearest_widget(self):
        """Displaying data to status widget with nearst ring"""

        tm, music = serch_time_for_nearest_ring(self.today_sched)
        self.nearest_label.setText(
            f'Через {tm} минут прозвенит {music[0:-4]}'
        )

    def set_item_to_timetable(self):
        """Displaying actual data on widgets on a timetable page"""

        self._init_list_special_day()
        self._init_edit_sched_window()

    def _init_list_special_day(self):
        templates = self.bd_manager.get_active_templates()
        layout = QVBoxLayout()
        for title, date in templates:
            widget = uic.loadUi('ui/active_schedule.ui')
            widget.title_label.setText(title)
            widget.date_label.setText(date)
            layout.addWidget(widget)
        group_box = QGroupBox()
        group_box.setStyleSheet(
            'border: 0px'
        )
        group_box.setLayout(layout)
        self.scrollArea_2.setWidget(group_box)
        self.scrollArea_2.setWidgetResizable(True)

    def _init_edit_sched_window(self):
        """Displaying actual data on widgets on a edit_schedule_window"""

        self.__fill_combobox()
        self.__init_taddy_date()

    def __fill_combobox(self):
        for i in self.bd_manager.get_list_template():
            self.set_schedule_on_day.templates_combobox.addItem(i[0])
        # self.set_schedule_on_day.templates_combobox.currentTextChanged.connect(self.chenge_tableitem_as_template)

    def __init_taddy_date(self):
        self.set_schedule_on_day.dateEdit.setDisplayFormat("dd-MM-yyyy")
        self.set_schedule_on_day.dateEdit.setDate(datetime.date.today())

    def add_special_day(self):
        self.set_schedule_on_day.show()
        self.set_schedule_on_day.add_schedule_button.clicked.connect(self.finish_adding_template)

    def finish_adding_template(self):
        template = self.set_schedule_on_day.templates_combobox.currentText()
        date = str(self.set_schedule_on_day.dateEdit.text())

        self._save_to_bd(template, date)
        self._init_list_special_day()
        self.set_schedule_on_day.hide()

    def _save_to_bd(self, template, date):
        self.bd_manager.add_special_date(template, date)

    def delete_special_day(self):
        pass

    def edit_special_day(self):
        self.edit_schedule_on_day.show()
        self.edit_schedule_on_day.add_schedule_button.clicked.connect(self.finish_editing_template())

    def finish_editing_template(self):
        template = self.edit_schedule_on_day.templates_combobox.currentText()
        date = str(self.edit_schedule_on_day.dateEdit.text())
        id = self.bd_manager.get_id_template(title=template, date=date)

        self._update_in_bd(template, date, id)
        self._init_list_special_day()
        self.edit_schedule_on_day.hide()

    def _update_in_bd(self, template, date, id):
        self.bd_manager.update_special_date(template, date, id)

    def add_row_to_schedule(self):
        currentRowCount = self.set_schedule_on_day.tableWidget.rowCount()
        self.set_schedule_on_day.tableWidget.insertRow(currentRowCount)
        # self.chenge_tableitem_as_template()

    def choosing_file(self):
        path = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Музыка (*.mp3);;Все файлы (*)')[0]
        file_name = path.split('/')[-1]
        return file_name

    def choose_music_file(self):
        file_name = self.choosing_file()
        self.set_schedule_on_day.file_name_edit.setText(file_name)
        self.set_schedule_on_day.hide()
        self.set_schedule_on_day.show()

    def chenge_tableitem_as_template(self):
        self.template = self.bd_manager.get_schedule(self.set_schedule_on_day.templates_combobox.currentText())
        self.set_schedule_on_day.tableWidget.setRowCount(len(self.template))
        for i, value in enumerate(self.template):
            self.set_schedule_on_day.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(value[0]))
            self.set_schedule_on_day.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(value[1]))
            self.set_schedule_on_day.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(value[2]))
        self.set_schedule_on_day.finish_creating_button.clicked.connect(self.finish_creating_schedule)

    def finish_creating_schedule(self):
        self.save_schedule()
        self.set_schedule_on_day.hide()
        # self.add_to_timetable()

    def save_schedule(self):
        rows = self.set_schedule_on_day.tableWidget.rowCount()
        cols = self.set_schedule_on_day.tableWidget.columnCount()
        for row in range(rows):
            finish = []
            for col in range(cols):
                try:
                    finish.append(self.set_schedule_on_day.tableWidget.item(row, col).text())
                except:
                    pass
            print(finish)
            self.bd_manager.save_shedule_row(finish)

    def change_defoult_template(self):
        self.choose_defoult_template.show()
        self.init_template_radiobutton()
        self.choose_defoult_template.finish_chiise_button.clicked.connect(self.save_defoult_template)

    def save_defoult_template(self):
        self.choose_defoult_template.hide()
        self.label.setText(f'По умолчанию - {self.defoult_template}')

    def init_template_radiobutton(self):
        templates = self.bd_manager.get_all_templates()
        layout = QVBoxLayout()
        for i in templates:
            widget = QRadioButton(i)
            widget.setStyleSheet('background-color: #0080ff;\nborder-radius: 10;\ncolor: white\n')
            widget.setGeometry(100, 100, 273, 35)
            widget.setFixedSize(273, 35)
            widget.toggled.connect(self.chanhged_defoult)
            layout.addWidget(widget)
        group_box = QGroupBox()
        group_box.setStyleSheet(
            'border: 0px'
        )
        group_box.setLayout(layout)
        self.choose_defoult_template.scrollArea.setWidget(group_box)
        self.choose_defoult_template.scrollArea.setWidgetResizable(True)

    def chanhged_defoult(self):
        self.defoult_template = self.sender().text()

    def set_item_to_template(self):
        templates = self.bd_manager.get_all_templates()
        layout = QGridLayout()
        for i in templates:
            widget = self.templ
            widget.title.setText(i)
            widget.edit_template.clicked.connect(self.refactor_template)
            layout.addWidget(widget)
        position = [(i, j) for i in range(5) for j in range(4)]
        layout.addWidget(self.add_templ)
        self.scrollArea_5.setLayout(layout)
        # self.choose_defoult_template.scrollArea.setWidget(group_box)
        self.scrollArea_5.setWidgetResizable(True)
        # https://zetcode.com/pyqt6/layout/

    def refactor_template(self):
        pass

    def create_template(self):
        self.set_schedule_on_day.show()
        self._fill_combobox()
        self._init_taddy_date()
        self.naming_template()
        # code

    def naming_template(self):
        self.naming_temp.show()
        self.naming_temp.finish_naming_button.clicked.connect(self.finish_neming)

    def finish_neming(self):
        self.title_for_new_templ = self.naming_temp.name_lineEdit.text()
        self.set_schedule_on_day.templates_combobox.addItem(self.title_for_new_templ)
        self.naming_temp.hide()


def window_power():
    """Starts a thread with an image of a windowed application"""

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    vew_window = threading.Thread(target=window_power)
    ring_power = threading.Thread(target=ringsystem_power)

    ring_power.start()
    vew_window.start()
    vew_window.join()
    ring_power.join()
