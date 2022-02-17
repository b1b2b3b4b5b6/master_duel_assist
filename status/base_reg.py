'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-02-17 21:07:14
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
from dict_recursive_update import recursive_update


class STATUS_BASE:
    PRI_TOP = float('inf')
    PRI_HIGH = 10
    PRI_MID = 5
    PRI_LOW = 0
    PRI_BOTTOM = -float('inf')

    def __init__(self):
        self.priority = self.PRI_MID
        self.transfer_dict = {}
        self.staimg_list = []


class STATUS_CONNECTING(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_HOME': tool.OperationDelay(delay=1)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/connecting.png')
        ]

        self.priority = self.PRI_HIGH


class STATUS_OK(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_HOME': tool.OperationClickOnImg('img/base/ok.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/ok.png')
        ]

        self.priority = self.PRI_HIGH


class STATUS_RETRY(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_HOME': tool.OperationClickOnImg('img/base/retry.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/retry.png')
        ]

        self.priority = self.PRI_TOP
