'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2022-02-20 15:09:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\main.py
'''
import logging
import time
import transfer
import schedule
import tool

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s]%(filename)s[%(lineno)d]:  %(message)s', datefmt='%d/%b/%Y %H:%M:%S')


def xyz(control: transfer.StatusControlThread):
    logging.info('do xyz start')
    control.goto_status('STATUS_XYZ_MYDECK', 0)
    control.goto_status('STATUS_DUEL_MAIN1', 0)
    logging.info('do xyz finished')


tool.init()
t = transfer.StatusControlThread()
t.start()

schedule.every(1).seconds.do(xyz, t)
schedule.run_all()

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    t.set_thead_status('stop')
    logging.info('已退出')
