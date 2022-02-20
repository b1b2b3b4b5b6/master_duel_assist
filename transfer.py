'''
Author: your name
Date: 2021-02-24 06:17:11
LastEditTime: 2022-02-20 15:33:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\transfer.py
'''


from gettext import find
import inspect

from networkx.readwrite.json_graph import tree
from win32con import CB_INITSTORAGE
from status.base_reg import STATUS_BASE
import tool
import sys
import networkx as nx
import matplotlib.pyplot as plt
import logging
import threading
import time
from dict_recursive_update import recursive_update
import collections
import cv2 as cv
import importlib
import duel
from pathlib import Path

duel_list = ['STATUS_PVP_DUEL', 'STATUS_GATE_DUEL']


class StatusControlThread(threading.Thread):

    now_status = 'STATUS_BASE'
    target_status = 'STATUS_BASE'
    next_status = 'STATUS_BASE'
    status_dict = d1 = collections.OrderedDict()
    G = nx.DiGraph()
    short_path_dict = {}
    thread_status = 'run'
    # last_ms_stamp = 0
    last_success_ms_stamp = float('INF')
    search_status_retry = 0

    def __init__(self):
        super().__init__()

        for mn in tool.get_all_modules('status'):
            importlib.import_module(mn)
            for name, class_ in inspect.getmembers(sys.modules[mn], inspect.isclass):
                self.status_dict[name] = class_()
                for k, _ in self.status_dict[name].transfer_dict.items():
                    self.G.add_edge(name, k)

        for key in list(self.status_dict.keys()):
            if key[-5:] == '_BASE':
                self.status_dict.pop(key)

        z = list(zip(self.status_dict.keys(), self.status_dict.values()))
        z = sorted(z, key=lambda x: x[1].priority, reverse=True)
        self.status_dict = dict(z)

        self.short_path_dict = dict(nx.all_pairs_shortest_path(self.G))
        # 初始时打印状态转移图
        # self.show_map()

    def __str__(self):
        return f'now[{self.now_status}] next[{self.next_status}] target[{self.target_status}]'

    def wait_for_status(self, status, delay_s=0):
        logging.info(f'wait for status[{status}]')
        if self.now_status == status:
            return True

        m_delay = delay_s
        if delay_s == 0:
            while self.now_status != status:
                time.sleep(1)
        else:
            while m_delay > 0 and self.now_status != status:
                time.sleep(1)
                m_delay -= 1

        if self.now_status == status:
            return True
        else:
            return False

    def goto_status(self, status, delay_s=0):
        logging.info(f'start go to status[{status}]')
        self.set_target_status(status)

        if self.wait_for_status(status, delay_s):
            logging.info(f'go to status[{status}] success')
            return True
        else:
            logging.warn(f'go to status[{status}] fail')
            return False

    def transfer(self, status):
        next_status_dict = self.status_dict[self.now_status].transfer_dict
        ope = next_status_dict[status]
        if isinstance(ope, list) == True:
            ope_list = ope
            for ope in ope_list:
                if ope != None:
                    ope.action()
        else:
            if ope != None:
                ope.action()

    def run(self):  # 必须有的函数
        self.thread_close_flag = False
        while True:
            time.sleep(0.01)

            if self.thread_status == 'run':
                pass
            elif self.thread_status == 'stop':
                exit()
            elif self.thread_status == 'pause':
                continue

            if self.search_status() == False:
                continue

            if self.target_status == 'STATUS_BASE':
                continue

            if self.now_status != self.target_status:
                if self.target_status not in self.short_path_dict[self.now_status]:
                    logging.error(f'can not reach targer status, {self}')
                    assert(None)
                self.next_status = self.short_path_dict[self.now_status][self.target_status][1]
                logging.info(f'start transfer, {self}')
                self.transfer(self.next_status)
                continue

    def show_map(self):
        for k, v in self.short_path_dict.items():
            print(k)
            print(v)
        nx.draw(self.G, with_labels=True, edge_color='b',
                node_color='g', node_size=1000)
        plt.show()

    def check_status(self, expect_status):

        cs = self.status_dict[expect_status]

        res = True
        for p in cs.staimg_list:
            if p.get_result() == False:
                res = False
                break
        if len(cs.staimg_list) == 0:
            res = False
        return res

    def search_status(self):

        def check():
            self.search_status_retry += 1
            tool.g_resource.refresh_screenshot()
            for s in self.status_dict.keys():
                if self.check_status(s) == True:
                    self.now_status = s
                    return True

            self.now_status = 'STATUS_BASE'
            tool.kick_ass()
            return False

        tool.Proof.reset_cache()
        if check() == True:
            self.reset_kick_all()
            logging.debug(f'search status finished, {self}')
            return True
        else:
            self.handle_kick_all()
            return False

    def handle_kick_all(self):
        now_ms_stamp = (int(round(time.time() * 1000)))
        if now_ms_stamp - self.last_success_ms_stamp > 30*1000 and self.search_status_retry > 30:
            self.reset_kick_all()
            tool.push_cloud('search_status_error, use kick all')
            tool.kick_all()
            return True
        else:
            return False

    def reset_kick_all(self):
        now_ms_stamp = (int(round(time.time() * 1000)))
        self.last_success_ms_stamp = now_ms_stamp
        self.search_status_retry = 0

    def set_target_status(self, expect_status):
        self.target_status = expect_status
        logging.info(f'set target[{expect_status}]')

    def set_thread_status(self, status):
        logging.info(f'set thread status[{status}]')
        self.last_success_ms_stamp = (int(round(time.time() * 1000)))
        self.thread_status = status
        if status == 'stop':
            self.join()
