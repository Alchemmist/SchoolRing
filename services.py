import datetime
import time
from typing import NamedTuple

import schedule
from audioplayer import AudioPlayer

from base_of_data import DataBaseManager

# used_template = []


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

        # global used_template
        # clean_used_template()

        self.delete_old_special()
        special_id = self.bd_manager.get_special_date_on_today()
        print('специальный айди ------>', special_id)

        # print(special_id in used_template)
        if special_id:
            new_special_id = self.bd_manager.get_perents_tempolate_id(special_id)
            self.today_sched = self.bd_manager.get_schedule_today(template_id=new_special_id)
            date = self.bd_manager.get_date_by_id(special_id)

            # self.bd_manager.clear_changes_default()
            # self.bd_manager.was_used(special_id)
            # used_template.append(special_id)
            # print(schedule.jobs)
            # print(used_template)
            self.run_special_schedule(date)
        else:
            self.today_sched = self.bd_manager.get_default_schedule()
            self.bd_manager.clear_changes_default()
            self.run_deafault_schedule()

    def delete_old_special(self):
        nd, nm, ny = str(datetime.date.today().strftime("%d-%m-%Y")).split('-')
        for i in self.bd_manager.get_active_templates():
            d, m, y = i[1].split('.')
            if y < ny or (y == ny and m < nm) or (y == ny and m == nm and d < nd):
                self.bd_manager.delete_special_date(template=i[0], date=i[1])

    def run_deafault_schedule(self):
        """Generates and runs a schedule for today"""

        for i in self.today_sched:
            schedule.every().day.at(i[0]).do(ring, i[1])
        # test:
        # schedule.every(3).seconds.do(ring, 'kapla.mp3')

    def run_special_schedule(self, date):
        for i in self.today_sched:
            date_time = f'{date} {i[0]}'
            print(date_time)
            schedule.every(1).hour.until(date_time).do(ring, i[1])
        # test:
        # schedule.every(3).seconds.do(ring, 'kapla.mp3')


def ringsystem_power():
    """Generates and runs a schedule for today"""

    print('RUN')
    bd_manager = DataBaseManager()
    rm = RingManager()
    rm.start_work()


def check_default(bd_manager: DataBaseManager):
    print('CHECK')
    default_key = bd_manager.check_udate_default()
    special_key = bd_manager.get_special_date_on_today()
    if 1 in default_key:
        print('СРАБОТАЛО default')
        ringsystem_power()
    if special_key:
        print('СРАБОТАЛО special')
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


# def clean_used_template():
#     active = DataBaseManager().get_active_templates()
#     for i in used_template:
#         if i not in active:
#             used_template.remove(i)
