'''
Author: your name
Date: 2021-03-04 21:33:52
LastEditTime: 2022-02-17 21:07:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\pvp_reg.py
'''

import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_XYZ_LOANER(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_XYZ_MYDECK': tool.OperationClickOnImg('img/activity/xyz/my_deck_off.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/activity/xyz/loaner_on.png')
        ]


class STATUS_XYZ_MYDECK(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/activity/xyz/start_duel.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/activity/xyz/my_deck_on.png')
        ]
