from typing import NamedTuple


class LoginData(NamedTuple):
    """Named tuple with fields for authorization data"""
    login: str
    password: str


class RegistrData(NamedTuple):
    """Named tuple with fields for authorization data"""
    FIO: str
    login: str
    concoct_password: str
    repeat_password: str
    school_num: int
    building_num: int
    phone_num: str

    def pars_fio(self):
        """Getting a name, surname, patronymic from a full name"""
        self.name, self.surname, self.patronymic = self.FIO.strip().split()
