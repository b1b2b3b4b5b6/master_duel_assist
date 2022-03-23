'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-03-23 20:50:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_DUELMENU(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_FESTIVAL_MYDECK': tool.OperationClickOnImg('img/festival/nr/enter.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/home/duel_menu/duel_menu.png')
        ]


class STATUS_DUEL_CHOOSESIDE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/going_first.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/going_first.png')
        ]


class STATUS_DUEL_RESULT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_HOME': tool.OperationClickOnImg('img/duel/duel_result.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/duel_result.png')
        ]
