import sqlite3
from services import RegistrData


class DataBaseManager:

    def __init__(self):
        pass

    def add_user(self, data: RegistrData):
        """Adds a new user to the system"""

        pass
        # con = sqlite3.connect('schoolring.sqlite')
        # cur = con.cursor()
        # cur.execute(f'INSERT INTO ' +
        #             f'users(login,password,school_num,building_num) ' +
        #             f'VALUES ' +
        #             f'({data.login},{data.repeat_password},{data.school_num},' +
        #             f'{data.building_num},{data.phone_num})').fetchall()
        # con.commit()

    def get_user_name(self, id):
        pass
