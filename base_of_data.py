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
                 f'VALUES("{data.login}", "{data.repeat_password}", "{int(data.school_num)}", "{int(data.building_num)}", ' \
                 f'"{data.phone_num}", "{data.FIO}")'

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
        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'SELECT play_time, music, title FROM schedule WHERE template=2'
        return cur.execute(comand).fetchall()
