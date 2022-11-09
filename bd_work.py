import sqlite3
from services import RegistrData


class DataBaseManager:

    def __init__(self):
        pass

    def add_user(self, data: RegistrData):
        """Adds a new user to the system"""

        con = sqlite3.connect('data_base/schoolring.sqlite')
        cur = con.cursor()
        comand = f'INSERT INTO users (login, password, school_num, building_num, phone_num, name) ' \
                 f'VALUES ({data.repeat_password}, {data.school_num}, {data.login}, {data.repeat_password}, '\
                 f'{data.building_num}, {data.phone_num}, {data.FIO})'
        print(comand)
        cur.execute(comand).fetchall()
        con.commit()

    def get_user_name(self, id):
        pass
