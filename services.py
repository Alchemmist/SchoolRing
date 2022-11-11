from typing import NamedTuple

from audioplayer import AudioPlayer

from datetime import time
from datetime import date
from datetime import datetime

import threading
import schedule

import base_of_data

from time import time, sleep

from threading import *

global today_sched
today_sched = 0


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
        self.bd_manager = base_of_data.DataBaseManager()

    def start_work(self):
        self.today_sched = self.bd_manager.get_schedule_today()
        today_sched = self.today_sched.copy()
        print(today_sched)
        self.go_schedule()

    def go_schedule(self):
        for i in self.today_sched:
            schedule.every().day.at(i[0]).do(ring, 'kapla.mp3')

        # test:
        # schedule.every(3).seconds.do(ring, 'kapla.mp3')

        while True:
            schedule.run_pending()


def ringsystem_power():
    rm = RingManager()
    rm.start_work()


def ring(name_music):
    AudioPlayer(f'music/{name_music}').play(block=True)
