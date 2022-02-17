'''
Author: your name
Date: 2022-01-06 01:48:04
LastEditTime: 2022-01-07 04:08:03
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \dllink_assist\edge.py
'''

import logging
import cv2
import numpy as np
import time
import os
import tool
from shapely import geometry


class EdgeDetectBase():
    gaussian_arg = None
    thresh = None
    window_name = None
    contours = None
    origin_img = None
    err_img_save = None

    def __init__(self, thresh, gaussion_arg=None, windos_name='EdgeDetectBase') -> None:
        self.gaussian_arg = gaussion_arg
        self.thresh = thresh
        self.err_img_save = tool.ErrorImgSave(windos_name)

    def action(self, img):
        if type(img) == str:
            img = cv2.imread(img)
        else:
            pass

        self.origin_img = img
        if self.gaussian_arg != None:
            img = cv2.GaussianBlur(img, *self.gaussian_arg)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
        self.contours, hierarchy = cv2.findContours(
            img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return self.contours

    def get_result(self):
        return None

    def get_show_img(self):
        out_img = self.origin_img
        for c in self.contours:
            cv2.drawContours(out_img, [c], -1, (0, 0, 255), 2)

            # 在图像上绘制轮廓及中心
            cv2.circle(out_img, tuple(self.get_contour_center(c)),
                       7, (0, 255, 0), -1)

        return out_img

    def show(self):
        cv2.imshow(self.window_name, self.get_show_img())
        cv2.waitKey(1)

    @staticmethod
    def get_coutour_xywh(contour):
        x, y, w, h = cv2.boundingRect(contour)
        return [x, y, w, h]

    @staticmethod
    def get_contour_center(contour):
        M = cv2.moments(contour)
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])
        return [x, y]


class BoxDetect(EdgeDetectBase):
    box_width_rate = 360/540
    box_width_offset = 0.01
    box_center_radius_rate = 100 / 540
    box_area_rate = 1/8

    def __init__(self, thresh=254, gaussion_arg=None, windos_name='BoxDetect') -> None:
        super().__init__(thresh, gaussion_arg=gaussion_arg, windos_name=windos_name)

    def action(self, img):
        super().action(img)

        out_contours = []
        for c in self.contours:
            _, _, w, h = tuple(self.get_coutour_xywh(c))

            # 弹出窗口的宽度是固定的
            app_w = tool.g_resource.env_info.app_img_wh[0]
            app_h = tool.g_resource.env_info.app_img_wh[1]
            if w < app_w * (self.box_width_rate - self.box_width_offset) or w > app_w * (self.box_width_rate + self.box_width_offset):
                continue

           # 弹出窗口大小有要求
            area = cv2.contourArea(c)
            if area / w*h < self.box_area_rate:
                continue

            # 弹出窗口的中心是固定的
            circ = geometry.Point(
                app_w//2, app_h//2).buffer(self.box_center_radius_rate * app_w)
            if circ.intersects(geometry.Point(*(self.get_contour_center(c)))) == False:
                continue

            out_contours.append(c)

        self.contours = out_contours

        if len(self.contours) > 1:
            logging.error('对话框识别存在有多个候选项')
            self.err_img_save.img(self.get_show_img(), 'multi_choose')

        return self.contours

    def get_result(self):
        if len(self.contours) == 0 or len(self.contours) > 1:
            return None
        else:
            x, y, w, h = tuple(self.get_coutour_xywh(self.contours[0]))
            return [[x, y], [x+w, y+h]]
