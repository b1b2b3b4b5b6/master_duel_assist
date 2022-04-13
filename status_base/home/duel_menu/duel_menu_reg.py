'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-04-13 17:50:44
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
from status_base.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_DUELMENU(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_FESTIVAL_MYDECK': tool.OperationClickOnImg('img/festival/enter.png'),
            'STATUS_RANK_MYDECK': tool.OperationClickOnImg('img/rank/enter.png'),
            'STATUS_HOME': tool.OperationClickOnImg('img/base/back.png', is_cache=False),
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/home/duel_menu/duel_menu.png')
        ]


class STATUS_DUEL_FINDOPPONECTRETRY(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/find_opponent_retry.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/find_opponent_retry.png')
        ]

        self.priority = STATUS_BASE.PRI_HIGH


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
            'STATUS_DUELMENU': tool.OperationClickOnImg('img/duel/duel_result.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/duel_result.png')
        ]
