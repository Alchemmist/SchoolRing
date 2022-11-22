import time
from typing import NamedTuple

import schedule
from audioplayer import AudioPlayer

from base_of_data import DataBaseManager


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
        """Aggregator for streaming time tracking and call playback"""

        special_id = self.bd_manager.get_special_date_on_today()
        if special_id:
            self.today_sched = self.bd_manager.get_schedule_today(template_id=special_id)
            self.run_schedule()
        else:
            self.today_sched = self.bd_manager.get_default_schedule()
            self.run_schedule()


    def run_schedule(self):
        """Generates and runs a schedule for today"""
        print(self.today_sched)
        for i in self.today_sched:
            schedule.every().day.at(i[0]).do(ring, i[1])
        # test:
        # schedule.every(3).seconds.do(ring, 'kapla.mp3')
        while True:
            schedule.run_pending()


def ringsystem_power():
    """Generates and runs a schedule for today"""

    print('RUN')
    bd_manager = DataBaseManager()
    schedule.every(1).minute.do(lambda: check_default(bd_manager))
    rm = RingManager()
    rm.start_work()


def check_default(bd_manager: DataBaseManager):
    print('CHECK')
    key = bd_manager.check_udate_default()
    print(key)
    print(type(key))
    if 1 in key:
        print('СРАБОТАЛО')
        bd_manager.clear_changes()
        ringsystem_power()


def ring(name_music):
    """"Plays a melody"""

    AudioPlayer(f'music/{name_music}').play(block=True)


def serch_time_for_nearest_ring(schedule: list) -> time:
    """Determines the nearest ring"""

    a = time.ctime().split()[3].split(':')
    now = int(a[0]) * 60 + int(a[1])
    closeness = None
    music = ''
    for i in schedule:
        tm = int(i[0].split(':')[0]) * 60 + int(i[0].split(':')[1])
        difference = tm - now
        try:
            if difference > 0 and difference < closeness:
                closeness = difference
                music = i[1]
        except TypeError:
            closeness = difference
            music = i[1]
    return closeness, music
