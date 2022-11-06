from typing import NamedTuple


class LoginData(NamedTuple):
    login: str
    password: str


class RegistrData(NamedTuple):
    FIO: str
    login: str
    concoct_password: str
    repeat_password: str
    school_number: int
    building_number: int
    phone_number: str
