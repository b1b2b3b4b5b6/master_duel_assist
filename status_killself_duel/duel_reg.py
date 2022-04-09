'''
Author: your name
Date: 2022-04-09 17:18:02
LastEditTime: 2022-04-10 00:52:18
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \master_duel_assist\status_killself_duel\duel_reg.py
'''
'''
Author: your name
Date: 2022-04-09 13:58:58
LastEditTime: 2022-04-09 15:04:56
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \master_duel_assist\status_skip_duel\duel_reg.py
'''
'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-04-09 13:56:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''




import tool
from dict_recursive_update import recursive_update
from status_base.duel_reg import STATUS_DUEL_MAIN1_BASE, STATUS_DUELPOINT_BASE
from status_base.duel_reg import STATUS_DUELNORMAL_BASE
class STATUS_DUEL_MAIN1(STATUS_DUEL_MAIN1_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_CHANGEPHASE': tool.OperationChanceList([tool.OperationLeftClick([690, 670]), tool.OperationClickOnImg('img/duel/main1.png')], [5, 1])
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/hand_activate.png', is_exist=False),
            tool.ProofImg('img/duel/hand_set.png', is_exist=False),
            tool.ProofImg('img/duel/hand_summon.png', is_exist=False),
            tool.ProofImg('img/duel/hand_special_summon.png', is_exist=False),
            tool.ProofImg('img/duel/faceup.png', is_exist=False),

        ]


class STATUS_DUEL_HNAD_ACTIVATE(STATUS_DUEL_MAIN1_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/hand_activate.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/hand_activate.png')
        ]


class STATUS_DUEL_HNAD_SET(STATUS_DUEL_MAIN1_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/hand_set.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/hand_set.png'),
            tool.ProofImg('img/duel/hand_activate.png', is_exist=False),
            tool.ProofImg('img/duel/hand_summon.png', is_exist=False),
            tool.ProofImg('img/duel/hand_special_summon.png', is_exist=False)

        ]


class STATUS_DUEL_HAND_SUMMON(STATUS_DUEL_MAIN1_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/hand_summon.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/hand_summon.png')
        ]


class STATUS_DUEL_HAND_SPECIAL_SUMMON(STATUS_DUEL_MAIN1_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/hand_special_summon.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/hand_special_summon.png')
        ]


class STATUS_DUEL_SUMMON_FACEUP(STATUS_DUEL_MAIN1_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/faceup.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/faceup.png')
        ]


class STATUS_DUELPOINT_YES(STATUS_DUELPOINT_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/yes.png', is_cache=False)
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/duel/yes.png')
        ]


class STATUS_DUELPOINT_ASK_ACTIVATE_NOT_SELECT(STATUS_DUELPOINT_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUELPOINT_ASK_ACTIVATE_SELECT': tool.OperationLeftClick([639, 580])
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImgOR([tool.ProofImg('img/duel/ask_activate.png'),
                             tool.ProofImg('img/duel/chain_ask_activate.png')]),
            tool.ProofImg('img/duel/gou.png', is_exist=False)
        ]


class STATUS_DUELPOINT_ASK_ACTIVATE_SELECT(STATUS_DUELPOINT_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/duel/active_select.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImgOR([tool.ProofImg('img/duel/ask_activate.png'),
                             tool.ProofImg('img/duel/chain_ask_activate.png')]),
            tool.ProofImg('img/duel/gou.png')
        ]
