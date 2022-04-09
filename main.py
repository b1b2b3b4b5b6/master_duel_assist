'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2022-04-10 01:05:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\main.py
'''
import logging
import time

from matplotlib.pyplot import contour
import transfer
import schedule
import tool

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s]%(filename)s[%(lineno)d]:  %(message)s', datefmt='%d/%b/%Y %H:%M:%S')

skip_duel_status_list = ['status_base', 'status_skip_duel']
killself_duel_status_list = ['status_base', 'status_killself_duel']


def festival(control: transfer.StatusControlThread):
    control.re_init(skip_duel_status_list)
    logging.info('do festival start')
    control.goto_status('STATUS_FESTIVAL_MYDECK', 0)
    control.goto_status('STATUS_DUEL_MAIN1', 0)
    logging.info('do festival finished')


def rank(control: transfer.StatusControlThread):
    control.re_init(killself_duel_status_list)
    logging.info('do rank start')
    control.goto_status('STATUS_RANK_MYDECK', 0)
    control.goto_status('STATUS_DUEL_MAIN1', 0)
    logging.info('do rank finished')


def get_awards(control: transfer.StatusControlThread):
    control.re_init(killself_duel_status_list)
    logging.info('do get_awards start')
    control.goto_status('STATUS_MISSIONS', 0)
    control.goto_status('STATUS_HOME', 0)
    logging.info('do get_awards finished')


tool.init()
t = transfer.StatusControlThread(['status_base'])
t.start()

schedule.every(1).seconds.do(rank, t)
schedule.every(1).hours.do(get_awards, t)
schedule.run_all()

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    t.set_thead_status('stop')
    logging.info('已退出')
