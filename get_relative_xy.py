'''
Author: your name
Date: 2021-02-24 15:28:57
LastEditTime: 2022-02-17 20:20:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\get_xy.py
'''
import os
import time
import tool
import pyautogui as pag
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s][%(levelname)s]%(filename)s[%(lineno)d]:  %(message)s', datefmt='%d/%b/%Y %H:%M:%S')

time.sleep(2)
tool.init()

try:
    while True:
        print("按下Ctrl + C 结束程序")
        # pag.position()返回鼠标的坐标
        x, y = pag.position()

        print([x, y])
        print(
            f'[{[x - tool.g_resource.get_window_base_point()[0],y - tool.g_resource.get_window_base_point()[1]]}]')
        print(
            f'[{[x - tool.g_resource.get_base_point()[0],y - tool.g_resource.get_base_point()[1]]}]')
        time.sleep(0.1)
        # 清除屏幕
        os.system('cls')
# 捕获异常 KeyboardInterrupt:用户中断执行(通常是输入^C)
except KeyboardInterrupt:
    print('已退出')
