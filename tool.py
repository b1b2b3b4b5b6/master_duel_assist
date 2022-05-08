'''
Author: your name
Date: 2021-02-21 02:27:24
LastEditTime: 2022-05-08 19:18:32
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
Description: In User Settings Edit
FilePath: \挂机\findpic.py
'''

from random import randint, random
from cv2 import randn
import pyautogui
import pymouse
import pykeyboard
import cv2 as cv
import logging
import time
import subprocess
import os
import threading
import pathlib
import requests
import numpy
import win32gui
import win32con

from config import config


class ImgHandle():
    def __init__(self) -> None:
        pass

    @staticmethod
    def find_img(background, template_object, similarity=0.95):
        # 用于读取原生图片,现省略
        # if isinstance(template, str):
        #     template = cv.imread(template)
        result = cv.matchTemplate(
            background, template_object, cv.TM_CCOEFF_NORMED)
        start_point = cv.minMaxLoc(result)[3]
        end_point = [start_point[0] + template_object.shape[1],
                     start_point[1] + template_object.shape[0]]

        if cv.minMaxLoc(result)[1] < similarity:
            return None
        else:
            return [start_point, end_point]

    @staticmethod
    def get_center_point(xy):
        center = [sum(t) // 2 for t in zip(xy[0], xy[1])]
        return center

    @staticmethod
    def get_left_lower_point(xy):
        left_lower = [xy[0][0], xy[1][1]]
        return left_lower

    @staticmethod
    def get_right_upper_point(xy):
        right_upper = [xy[0][1], xy[1][0]]
        return right_upper


class EnvInfo():
    allow_platform = ['pc', 'android']

    def __init__(self, conf: config):
        d = conf.get_dict()

        self.platform = d['platform']
        self.resurce_root = self.platform + '/'
        self.app_img_offset = d['app_img_offset']
        self.app_img_wh = d['app_img_wh']
        self.ft_url_prefix = d['ft_url_prefix']

        if self.platform not in self.allow_platform:
            logging.error(f'platform[{self.platform} is not illegal]')
            assert(None)

        logging.info(f'{self}')

    def __str__(self) -> str:
        return f'platform[{self.platform}] resurce_root[{self.resurce_root}] app_img_offset[{self.app_img_offset} app_img_xy[{self.app_img_wh} ft_url[{self.ft_url_prefix}]]'.strip()

    def get_path_by_key(self, key):
        out_path = pathlib.PurePosixPath(
            pathlib.Path(os.path.join(self.resurce_root, key))).__str__()

        if False == os.path.exists(out_path):
            logging.error(f'path[{out_path} not exist]')
            assert(None)

        return out_path


class Resource():
    env_info: EnvInfo = None
    resource_obj = None
    screenshot = None
    screenshot_lock = threading.Lock()
    base_point = None

    def __init__(self, env_info: EnvInfo) -> None:
        self.env_info = env_info
        self.resource_obj = {}
        self.reset_base_point()
        # for root, dirs, files in os.walk(self.env_info.resurce_root):
        #     for file in files:
        #         file_path = pathlib.PurePosixPath(
        #             pathlib.Path(os.path.join(root, file))).__str__()
        #         key = file_path[len(self.env_info.resurce_root):]
        #         self.resource_obj[key] = cv.imread(file_path)
        #         logging.debug(
        #             f'read img obj[{key}] complete')

    def register_resource(self, key: str, object):
        if key not in self.resource_obj:
            self.resource_obj[key] = object

        logging.debug(f'resource[{key}] register')

    def get_resource_obj(self, key: str):
        if key not in self.resource_obj:
            logging.error(f'key[{key}] not in resource_obj')
            assert(None)
        return self.resource_obj[key]

    def refresh_screenshot(self):
        self.screenshot_lock.acquire()
        # x,y,w,h
        img = pyautogui.screenshot()

        self.screenshot = cv.cvtColor(numpy.array(img), cv.COLOR_RGB2BGR)
        self.screenshot_lock.release()

    def get_screenshot(self, refresh=False):
        if refresh == True:
            self.refresh_screenshot()

        return self.screenshot

    def get_appshot(self, refresh=False):
        if refresh == True:
            self.refresh_screenshot()

        return self.screenshot[self.get_base_point()[1]:(self.get_base_point()[1] + self.env_info.app_img_wh[1]),
                               self.get_base_point()[0]:(self.get_base_point()[0] + self.env_info.app_img_wh[0])]

    def reset_base_point(self):

        # logging.info('finding game window')
        # hwnd = GameControl.find()
        # if hwnd == 0:
        #     logging.error('can not find game window')
        #     assert(None)

        # win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        # win32gui.SetForegroundWindow(hwnd)
        # win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0,
        #                       0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

        self.base_point = [8 + self.env_info.app_img_offset[0],
                           31 + self.env_info.app_img_offset[1]]

        logging.info(f'base point is {self.base_point}')

    def get_base_point(self):
        # if self.base_point == None:
        #     self.reset_base_point()
        return self.base_point

    def get_window_base_point(self):
        # if self.base_point == None:
        #     self.reset_base_point()
        return [self.base_point[0] - self.env_info.app_img_offset[0], self.base_point[1] - self.env_info.app_img_offset[1]]


g_resource: Resource = None
# 资源初始化


def init(conf: config):
    global g_resource

    g_resource = Resource(EnvInfo(conf))


class OperationBase:

    def __init__(self, ope_name, delay=0) -> None:
        self.ope_name = ope_name
        self.delay = delay

    def action(self):
        time.sleep(self.delay)
        pymouse.PyMouse().move(
            *map(sum, zip([2, 2],  g_resource.get_base_point())))

    def __str__(self):
        return f'ope_name[{self.ope_name}] delay[{self.delay}]'.strip()


class OperationDelay(OperationBase):
    def __init__(self, delay=0.8) -> None:
        super().__init__('delay', delay)

    def __str__(self):
        return f'{super().__str__()}'.strip()

    def action(self):
        super().action()


class OperationRightClick(OperationBase):

    def __init__(self, xy, delay=0.8) -> None:
        super().__init__('right_click', delay)
        self.xy = xy

    def __str__(self):
        return f'{super().__str__()} | xy[{self.xy}]'.strip()

    def action(self):
        pymouse.PyMouse().click(*map(sum, zip(self.xy, g_resource.get_base_point())), 2)

        super().action()


class OperationLeftClick(OperationBase):

    def __init__(self, xy, delay=0.8) -> None:
        super().__init__('click', delay)
        self.xy = xy

    def __str__(self):
        return f'{super().__str__()} | xy[{self.xy}]'.strip()

    def action(self):
        pymouse.PyMouse().click(*map(sum, zip(self.xy, g_resource.get_base_point())), 1)

        super().action()


class OperationChanceList(OperationBase):
    def __init__(self,  ope_list: list, times_list: list) -> None:
        super().__init__('chance')
        self.ope_list = ope_list
        self.times_list = times_list
        if len(self.ope_list) != len(self.times_list):
            logging.error(f'ope[{self}] illegal')
            assert(None)

    def __str__(self):
        return f'{super().__str__()} | ope_list[{self.ope_list}] times_list[{self.times_list}]'.strip()

    def action(self):
        s = sum(self.times_list)
        a = randint(1, s)
        s = 0
        for n in range(len(self.times_list)):
            s += self.times_list[n]
            if s >= a:
                ope: OperationBase = self.ope_list[n]
                ope.action()
                break

        super().action()


class OperationClickOnImg(OperationBase):
    img_key = None
    is_cache = None
    last_xy = None

    def __init__(self, img_key, is_cache=True, delay=0.8) -> None:
        super().__init__('click_on_img', delay)
        self.img_key = img_key
        self.is_cache = is_cache
        g_resource.register_resource(img_key, cv.imread(
            g_resource.env_info.get_path_by_key(img_key)))

    def __str__(self):
        return f'{super().__str__()} | img[{self.img_key}] is_cache[{self.is_cache}]'.strip()

    def action(self):
        if self.is_cache == True and self.last_xy != None:
            pass
        else:
            res = ImgHandle.find_img(
                g_resource.get_appshot(), g_resource.get_resource_obj(self.img_key))
            if res == None:
                logging.error(
                    f'can not action click on img_key[{self.img_key}], pass this action')
                return
            else:
                self.last_xy = ImgHandle.get_center_point(res)

        pymouse.PyMouse().click(*map(sum, zip(self.last_xy, g_resource.get_base_point())), 1)

        super().action()


class OperationSlide(OperationBase):
    xy_start = None
    xy_stop = None

    def __init__(self, xy_start, xy_stop, delay=0) -> None:
        super().__init__('slide', delay)
        self.xy_start = xy_start
        self.xy_stop = xy_stop

    def __str__(self):
        return f'{super().__str__()} | xy_start[{self.xy_start}] xy_stop[{self.xy_stop}]'.strip()

    def action(self):
        pymouse.PyMouse().press(*map(sum, zip(self.xy_start, g_resource.get_base_point())))
        pyautogui.moveTo(
            *map(sum, zip(self.xy_stop,  g_resource.get_base_point())), 0.3)
        pymouse.PyMouse().release(*map(sum, zip(self.xy_stop,  g_resource.get_base_point())))
        super().action()


g_proof_cache: dict = {}


class Proof():

    def __init__(self) -> None:
        pass

    def get_result() -> bool:
        return True

    def __str__(self) -> str:
        return ''

    @staticmethod
    def reset_cache():
        global g_proof_cache
        g_proof_cache = {}

    @staticmethod
    def get_cache(key: str):
        if key in g_proof_cache:
            return g_proof_cache[key]
        else:
            return None

    @staticmethod
    def set_cache(key: str, status: bool):
        g_proof_cache[key] = status


class ProofImg(Proof):

    def __init__(self, img_key, is_exist=True, bg_app=True) -> None:
        super().__init__()
        self.img_key = img_key
        self.is_exist = is_exist
        self.bg_app = bg_app

        g_resource.register_resource(img_key, cv.imread(
            g_resource.env_info.get_path_by_key(img_key)))

    def __str__(self) -> str:
        return f'{super().__str__()} | ProofImg: img_key[{self.img_key}] '.strip()

    def get_result(self) -> bool:
        if None == self.get_cache(self.img_key):
            if self.bg_app == True:
                bg = g_resource.get_appshot()
            else:
                bg = g_resource.get_screenshot()

            xy = ImgHandle.find_img(
                bg, g_resource.get_resource_obj(self.img_key))

            if xy != None:
                logging.debug(
                    f'{self} | can proof]')

            self.set_cache(self.img_key, xy != None)

        return self.get_cache(self.img_key) == self.is_exist


class ProofImgOR(Proof):
    def __init__(self, proof_list: list, ) -> None:
        super().__init__()
        self.proof_list = proof_list

    def __str__(self) -> str:
        return f'{super().__str__()} | ProofImgOR: proof_list[{self.proof_list}] '.strip()

    def get_result(self) -> bool:
        for p in self.proof_list:
            if p.get_result() == True:
                return True
        return False


def retry(func, count=1, delay=0):
    if count == 0:
        logging.error(f'retry count can not[{count}] < 0')
        assert(None)

    for n in range(count):
        if func() == True:
            return True
        time.sleep(delay)
    return False


class ErrorImgSave():
    prefix = None
    save_dir = None

    def __init__(self, prefix='default', root_dir='err_img') -> None:
        self.save_dir = root_dir+'/'+prefix
        os.makedirs(self.save_dir, exist_ok=True)

    def get_save_file_path(self, info='') -> str:
        return os.path.join(self.save_dir, time.strftime(
            f'%m%d%H%M%S_{info}.png', time.localtime()))

    def screen(self):
        img = pyautogui.screenshot()  # x,y,w,h
        img.save(self.get_save_file_path())

    def img(self, img, info=''):
        if type(img) == str:
            img = cv.imread(img)
        else:
            pass

        cv.imwrite(self.get_save_file_path(info), img)


def kick_ass():
    k = pykeyboard.PyKeyboard()
    k.tap_key(k.control_key)


# 点击一个无关紧要的地方
def kick_all():
    logging.info('need final solution')
    ErrorImgSave('kick_all').screen()
    xy = g_resource.env_info.app_img_wh
    for x in range(1, xy[0]-1, xy[0] // 9):
        for y in range(1, xy[1]-1, xy[1] // 16):
            OperationLeftClick([x, y], delay=0.01).action()
    logging.info('final solution complete')


def push_cloud(msg):
    url_prefix = g_resource.env_info.ft_url_prefix
    if url_prefix != None:
        url = url_prefix + msg
        try:
            requests.get(url)
        except BaseException:
            logging.error(f'push cloud faild[{url}]')


def get_all_modules(dir_name):
    modules = []
    for root, _, fs in os.walk(dir_name):
        for f in fs:
            if f.startswith('__') or f.endswith('.pyc'):
                continue
            fullname = os.path.join(root, f)
            fullname = fullname.replace('.py', '')
            fullname = fullname.replace('\\', '.')
            modules.append(fullname)
    return modules


# 视平台而定,以下仅适用于雷电模拟器
# class SwitchApp():
#     def game(self):
#         logging.info('switch to game')
#         g_resource.refresh_screenshot()
#         Operation(Operation.CLICK_ON_IMG,
#                   img='img/base/game_ico.png', bg_app=False).action('screen')

#     def home(self):
#         logging.info('switch to home')
#         g_resource.refresh_screenshot()
#         Operation(Operation.CLICK_ON_IMG,
#                   img='img/base/head.png', bg_app=False).action('screen')


class GameControl():
    @staticmethod
    def stop() -> bool:
        logging.info('stop game')
        if GameControl.find() != 0:
            win32gui.PostMessage(GameControl.find(), win32con.WM_CLOSE, 0, 0)
            time.sleep(5)
            if GameControl.find() != 0:
                logging.error("can not stop game")
                return False

        logging.info('stop game success')
        return True

    @staticmethod
    def start() -> bool:
        logging.info('start game')
        if GameControl.find() == 0:
            os.system('Start steam://rungameid/1449850')
            time.sleep(5)
            if GameControl.find() == 0:
                logging.error("can not start game")
                return False

        win32gui.ShowWindow(GameControl.find(), win32con.SW_SHOWNORMAL)
        # win32gui.SetForegroundWindow(GameControl.find())
        win32gui.SetWindowPos(GameControl.find(), win32con.HWND_TOPMOST, 0, 0,
                              0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

        logging.info('start game success')
        return True

    @staticmethod
    def find():
        hwnd = win32gui.FindWindow(None, "masterduel")
        return hwnd


# 暂无断网功能
class Internet():
    def open(self):
        logging.info('internet open')
        subprocess.call('NetDisabler_x64.exe /E')

    def close(self):
        logging.info('internet close')
        subprocess.call('NetDisabler_x64.exe /D')

    def reboot(self, time_s):
        logging.info(f'internet will reboot[{time_s}]')
        self.close()
        time.sleep(time_s)
        self.open()
