from typing import NamedTuple

from audioplayer import AudioPlayer

from datetime import time
from datetime import date
from datetime import datetime


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


class RingManager:

    def __init__(self):
        pass

    def ring(self):
        pass


class Rings:

    def __init__(self):
        pass

    def play(self, music):
        pass
