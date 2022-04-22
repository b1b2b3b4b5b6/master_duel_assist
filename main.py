'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2022-04-22 19:42:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\main.py
'''


import logging
import time

from matplotlib.pyplot import contour
from config import config
import transfer
import schedule
import tool

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s]%(filename)s[%(lineno)d]:  %(message)s', datefmt='%d/%b/%Y %H:%M:%S')

conf = config('config.json')
conf_dict = conf.get_dict()
tool.GameControl.start()
tool.init(conf)
tool.GameControl.stop()

skip_duel_status_list = ['status_base', 'status_skip_duel']
killself_duel_status_list = ['status_base', 'status_killself_duel']


t = transfer.StatusControlThread(['status_base'])


def festival():
    if t.now_thread_status != t.THREAD_STATUS_RUN:
        time.sleep(5)
        return
    t.re_init(skip_duel_status_list)
    logging.info('do festival start')
    t.goto_status('STATUS_FESTIVAL_MYDECK', 0)
    t.goto_status('STATUS_DUEL_MAIN1', 0)
    t.goto_status('STATUS_HOME', 0)
    logging.info('do festival finished')


def rank():
    if t.now_thread_status != t.THREAD_STATUS_RUN:
        time.sleep(5)
        return
    t.re_init(killself_duel_status_list)
    logging.info('do rank start')
    t.goto_status('STATUS_RANK_MYDECK', 0)
    t.goto_status('STATUS_DUEL_MAIN1', 0)
    t.goto_status('STATUS_HOME', 0)
    logging.info('do rank finished')


def get_awards():
    if t.now_thread_status != t.THREAD_STATUS_RUN:
        time.sleep(5)
        return
    t.re_init(killself_duel_status_list)
    logging.info('do get_awards start')
    t.goto_status('STATUS_MISSIONS_NO_AWARDS', 0)
    t.goto_status('STATUS_HOME', 0)
    logging.info('do get_awards finished')


def start_game():
    tool.GameControl.start()
    t.goto_thread_status(t.THREAD_STATUS_RUN)


def stop_game():
    t.goto_thread_status(t.THREAD_STATUS_PAUSE)
    tool.GameControl.stop()


if(conf_dict['do_festival'] == True):
    schedule.every(1).seconds.do(festival)
    schedule.every(1).seconds.do(festival)
    print("do festival\n")

if(conf_dict['do_rank'] == True):
    j = schedule.every(1).seconds.do(rank)
    j = schedule.every(30).hours.do(get_awards)
    print("do rank\n")

schedule.every().day.at(conf_dict['start_time']).do(start_game)
schedule.every().day.at(conf_dict['stop_time']).do(stop_game)


t.start()
t.goto_thread_status(t.THREAD_STATUS_PAUSE)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    t.goto_thread_status(t.THREAD_STATUS_STOP)
    logging.info('已退出')
