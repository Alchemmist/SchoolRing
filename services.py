import time
from typing import NamedTuple
from multiprocessing import Queue

import schedule
from audioplayer import AudioPlayer

import base_of_data


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
        """Aggregator for streaming time tracking and call playback"""

        special_id = self.serch_template_id_for_today()
        if special_id:
            self.today_sched = self.bd_manager.get_schedule_today(template_id=special_id)
            self.run_schedule()
        else:
            self.today_sched = self.bd_manager.get_default_schedule()
            self.run_schedule()

    def serch_template_id_for_today(self):
        pass

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
    RingManager().start_work()


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
