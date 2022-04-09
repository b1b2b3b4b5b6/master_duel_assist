'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-04-09 23:51:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
import logging
from status_base.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_HOME(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUELMENU': tool.OperationClickOnImg('img/home/duel_enter.png'),
            'STATUS_MISSIONS': tool.OperationLeftClick([957, 33])
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/home/duel_enter.png')
        ]
