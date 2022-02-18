'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-02-18 08:58:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_DUEL_FINDOPPONECTRETRY(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/find_opponent_retry.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/find_opponent_retry.png')
        ]

        self.priority = STATUS_BASE.PRI_HIGH


class STATUS_DUEL_NOTSELECT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_SELECT': tool.OperationLeftClick([639, 580])
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/not_select.png'),
            tool.ProofImg('img/duel/gou.png', typ='not_exist'),
        ]

        self.priority = STATUS_BASE.PRI_HIGH


class STATUS_DUEL_SELECT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/select.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/select.png'),
            tool.ProofImg('img/duel/gou.png'),
        ]

        self.priority = STATUS_BASE.PRI_HIGH


class STATUS_DUEL_CHOOSESIDE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/going_first.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/going_first.png')
        ]


class STATUS_DUEL_OPPONENTTURN(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationDelay(delay=3)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/opponent_turn.png')
        ]


class STATUS_DUEL_MAIN1(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_CHANGEPHASE': tool.OperationClickOnImg('img/duel/main1.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/main1.png')
        ]


class STATUS_DUEL_DRAW(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/draw.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/draw.png')
        ]


class STATUS_DUEL_CHANGEPHASE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_END': tool.OperationClickOnImg('img/duel/end_phase.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/end_phase.png')
        ]


class STATUS_DUEL_END(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_RESULT': tool.OperationClickOnImg('img/base/ok.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/duel_end.png')
        ]


class STATUS_DUEL_RESULT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_HOME': tool.OperationClickOnImg('img/duel/duel_result.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/duel/duel_result.png')
        ]
