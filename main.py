'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2022-05-18 20:16:23
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
Description: In User Settings Edit
FilePath: \挂机\main.py
'''


import datetime
import logging
import time
from tracemalloc import start

from matplotlib.pyplot import contour
from config import config
import transfer
import schedule
import tool

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s][%(levelname)s]%(filename)s[%(lineno)d]:  %(message)s', datefmt='%d/%b/%Y %H:%M:%S')

conf = config('config.json')
conf_dict = conf.get_dict()

start_time: str = conf_dict['start_time']
start_time = start_time.replace(':', '')
stop_time: str = conf_dict['stop_time']
stop_time = stop_time.replace(':', '')

tool.init(conf)

skip_duel_status_list = ['status_base', 'status_skip_duel']
killself_duel_status_list = ['status_base', 'status_killself_duel']


t = transfer.StatusControlThread(['status_base'])
t.start()


def festival():
    t.re_init(skip_duel_status_list)
    logging.info('do festival start')
    t.goto_status('STATUS_FESTIVAL_MYDECK', 0)
    t.goto_status('STATUS_DUEL_MAIN1', 0)
    t.goto_status('STATUS_HOME', 0)
    logging.info('do festival finished')


def rank():
    t.re_init(killself_duel_status_list)
    logging.info('do rank start')
    t.goto_status('STATUS_RANK_MYDECK', 0)
    t.goto_status('STATUS_DUEL_MAIN1', 0)
    t.goto_status('STATUS_HOME', 0)
    logging.info('do rank finished')


def get_awards():
    t.re_init(killself_duel_status_list)
    logging.info('do get_awards start')
    t.goto_status('STATUS_MISSIONS', 0)
    tool.OperationLeftClick([1105, 664], 2).action()
    tool.OperationLeftClick([1105, 664], 2).action()
    t.goto_status('STATUS_HOME', 0)
    logging.info('do get_awards finished')


def start_game():
    while(tool.GameControl.start() != True):
        pass
    t.goto_thread_status(t.THREAD_STATUS_RUN)


def stop_game():
    t.goto_thread_status(t.THREAD_STATUS_PAUSE)
    while(tool.GameControl.stop() != True):
        pass


if(conf_dict['do_festival'] == True):
    schedule.every(1).seconds.do(festival)
    print("do festival\n")

if(conf_dict['do_rank'] == True):
    schedule.every(1).seconds.do(rank)
    schedule.every(30).minutes.do(get_awards)
    print("do rank\n")


try:
    while True:
        time.sleep(1)
        now_time = datetime.datetime.strftime(
            datetime.datetime.now(), '%H%M')

        if int(now_time) >= int(start_time) and int(now_time) <= int(stop_time):
            start_game()
            schedule.run_pending()

        else:
            stop_game()


except KeyboardInterrupt:
    t.goto_thread_status(t.THREAD_STATUS_STOP)
    logging.info('已退出')
