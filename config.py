'''
Author: your name
Date: 2022-04-22 17:30:59
LastEditTime: 2022-04-22 17:40:03
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \master_duel_assist\config.py
'''
import json


class config():
    def __init__(self, json_file) -> None:
        config_str = open(json_file, 'r', encoding='utf-8').read()
        self.conf_dict = json.loads(config_str)

    def get_dict(self):
        return self.conf_dict
