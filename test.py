'''
Author: your name
Date: 2022-01-02 05:48:09
LastEditTime: 2022-01-07 03:58:35
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \dllink_assist\test.py
'''
from shapely import geometry
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s][%(levelname)s]%(filename)s[%(lineno)d]:  %(message)s', datefmt='%d/%b/%Y %H:%M:%S')
logging.debug('asdf')

circ = geometry.Point(
    100, 100).buffer(100)
print(circ)
print(circ.intersects(geometry.Point(201, 100)))
