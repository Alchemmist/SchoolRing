from typing import NamedTuple

from audioplayer import AudioPlayer

from datetime import time
from datetime import date
from datetime import datetime

import threading
from schedule import *

from bd_work import DataBaseManager


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
        self.bd_manager = DataBaseManager()

    def start_work(self):
        self.bd_manager.get_schedule_today()
        self.pars_shedule()
        self.create_schedule()

    def pars_schedule(self):
        pass

    def create_schedule(self):
        pass


def ringsystem_power():
    rm = RingManager()
    rm.start_work()
