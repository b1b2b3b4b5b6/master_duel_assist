'''
Author: your name
Date: 2022-03-27 19:01:42
LastEditTime: 2022-04-06 08:39:16
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \master_duel_assist\keep_wake.py
'''

import pykeyboard
import win32gui
import logging
import win32con
import time
import pyautogui
import pymouse
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s]%(filename)s[%(lineno)d]:  %(message)s', datefmt='%d/%b/%Y %H:%M:%S')

logging.info('finding game window')
hwnd = win32gui.FindWindow(None, "masterduel")
if hwnd == None:
    logging.error('can not find game window')
    assert(None)
while True:
    time.sleep(8)
    pymouse.PyMouse().click(500, 500, 1)
