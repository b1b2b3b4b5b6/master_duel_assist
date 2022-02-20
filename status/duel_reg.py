'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-02-20 18:45:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_DUEL_BASE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/ing.png'),
            tool.ProofImg('img/duel/blue_arrow.png', is_exist=False)
        ]


class STATUS_DUELPOINT_BASE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/ing.png'),
            tool.ProofImg('img/duel/blue_arrow.png')
        ]


class STATUS_DUEL_FINDOPPONECTRETRY(STATUS_DUEL_BASE):
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


class STATUS_DUEL_OPPONENTTURN(STATUS_DUEL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationDelay(delay=3)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/opponent_turn.png')
        ]


class STATUS_DUEL_MAIN1(STATUS_DUEL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_CHANGEPHASE': tool.OperationClickOnImg('img/duel/main1.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/main1.png')
        ]


class STATUS_DUEL_DRAW(STATUS_DUEL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/draw.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/draw.png')
        ]


class STATUS_DUEL_CHANGEPHASE(STATUS_DUEL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_END': tool.OperationClickOnImg('img/duel/end_phase.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/end_phase.png')
        ]


class STATUS_DUEL_END(STATUS_DUEL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_RESULT': tool.OperationClickOnImg('img/base/ok.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/duel_end.png')
        ]


class STATUS_DUELPOINT_NOTSELECT(STATUS_DUELPOINT_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUELPOINT_SELECT': tool.OperationLeftClick([639, 580])
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/not_select.png'),
            tool.ProofImg('img/duel/gou.png', is_exist=False),
        ]


class STATUS_DUELPOINT_SELECT(STATUS_DUELPOINT_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/select.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/select.png'),
            tool.ProofImg('img/duel/gou.png'),
        ]


class STATUS_DUELPOINT_CANCLE(STATUS_DUELPOINT_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/cancle.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/cancle.png')
        ]


class STATUS_DUELPOINT_NO(STATUS_DUELPOINT_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/no.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/no.png')
        ]
