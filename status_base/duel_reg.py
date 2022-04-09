'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-04-10 01:01:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
import logging
from status_base.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_DUELNORMAL_BASE(STATUS_BASE):
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


class STATUS_DUEL_OPPONENTTURN(STATUS_DUELNORMAL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationDelay(delay=3)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/opponent_turn.png'),
            tool.ProofImg('img/duel/opponent_first.png', is_exist=False)
        ]


class STATUS_DUEL_OPPONENTFIRST(STATUS_DUELNORMAL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_SETUP': tool.OperationClickOnImg('img/duel/setup.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/opponent_first.png')
        ]


class STATUS_DUEL_SETUP(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_SURRENDER_ASK': tool.OperationClickOnImg('img/duel/surrender.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/setup_ing.png')
        ]


class STATUS_DUEL_SURRENDER_ASK(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_RESULT': tool.OperationClickOnImg('img/duel/surrender_yes.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/surrender_ask.png')
        ]


class STATUS_DUEL_MAIN1_BASE(STATUS_DUELNORMAL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/main1.png')
        ]


class STATUS_DUEL_DRAW(STATUS_DUELNORMAL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/draw.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/draw.png')
        ]


class STATUS_DUELPOINT_DISCARD_NOTSELECT(STATUS_DUELPOINT_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUELPOINT_DISCARD_SELECT': tool.OperationLeftClick([639, 580])
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/discard.png'),
            tool.ProofImg('img/duel/gou.png', is_exist=False),
        ]


class STATUS_DUELPOINT_DISCARD_SELECT(STATUS_DUELPOINT_BASE):
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


class STATUS_DUEL_CHANGEPHASE(STATUS_DUELNORMAL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_END': tool.OperationClickOnImg('img/duel/end_phase.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/end_phase.png')
        ]


class STATUS_DUEL_END(STATUS_DUELNORMAL_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_RESULT': tool.OperationClickOnImg('img/base/ok.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/duel_end.png')
        ]
