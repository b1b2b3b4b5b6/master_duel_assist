'''
Author: your name
Date: 2022-01-06 02:24:28
LastEditTime: 2022-01-08 19:44:46
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \dllink_assist\show_edge_test.py
'''
import edge

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
    box = edge.BoxDetect()
    while True:
        img = tool.g_resource.get_appshot(True)
        box.action(img)
        box.show()

# 捕获异常 KeyboardInterrupt:用户中断执行(通常是输入^C)
except KeyboardInterrupt:
    print('已退出')
