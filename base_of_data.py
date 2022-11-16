import sqlite3
from services import RegistrData


class DataBaseManager:

    def __init__(self):
        pass

    def add_user(self, data: RegistrData):
        """Adds a new user to the system"""

        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'INSERT INTO users(login, password, school_num, building_num, phone_num, FIO) ' \
                 f'VALUES("{data.login}", "{data.repeat_password}", "{int(data.school_num)}", ' \
                 f'"{int(data.building_num)}", "{data.phone_num}", "{data.FIO}")'

        cur.execute(comand).fetchall()
        con.commit()

    def get_user_name(self, id):
        pass

    def serch_logins(self, login) -> list:
        """Get a list of logins of all existing users"""

        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT login FROM users WHERE login="{login}"'
        logins = [i[0] for i in cur.execute(comand).fetchall()]
        return logins

    def get_FIO(self, login):
        """Getting a full name from the lign database"""

        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT FIO FROM users WHERE login="{login}"'
        FIO = [i[0] for i in cur.execute(comand).fetchall()]
        return FIO

    def get_password(self, login):
        """Finds the user's password by login"""

        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT password FROM users WHERE login="{login}"'
        return cur.execute(comand).fetchall()

    def get_schedule_today(self):
        """Gets the call schedule for today"""

        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT play_time, music, title FROM schedule WHERE template=2'
        return cur.execute(comand).fetchall()

    def get_list_template(self):
        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT title FROM template'
        return cur.execute(comand).fetchall()

    def get_schedule(self, template):
        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        template_id = cur.execute(f'SELECT id FROM template WHERE title="{template}"').fetchall()[0][0]
        comand = f'SELECT title, play_time, music FROM schedule WHERE template = "{template_id}"'
        return cur.execute(comand).fetchall()

    def save_shedule_row(self, data: list):
        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'INSERT INTO schedule(title, play_time, music) ' \
                 f'VALUES("{data[0]}", "{data[1]}", "{data[2]}")'
        cur.execute(comand).fetchall()
        con.commit()

    def get_all_templates(self):
        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        templates = cur.execute(f'SELECT title FROM template').fetchall()
        finish_lst = [i[0] for i in templates]
        return finish_lst

    def get_active_templates(self):
        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        templates = cur.execute(f'SELECT title, date FROM template WHERE date').fetchall()
        return templates

    def get_id_template(self, title, date):
        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        templates = cur.execute(f'SELECT id FROM template WHERE title="{title}" AND date="{date}"').fetchall()
        return templates[0]

    def add_special_date(self, template, date):
        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'INSERT INTO template(title, date) ' \
                 f'VALUES("{template}", "{date}")'
        cur.execute(comand).fetchall()
        con.commit()

    def update_special_date(self, template, date, id):
        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'UPDATE template(title, date) ' \
                 f'SET("{template}", "{date}")' \
                 f'WHERE id="{id}"'
        cur.execute(comand).fetchall()
        con.commit()
