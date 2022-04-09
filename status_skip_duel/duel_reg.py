'''
Author: your name
Date: 2022-04-09 13:58:58
LastEditTime: 2022-04-09 17:41:49
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
class STATUS_DUEL_MAIN1(STATUS_DUEL_MAIN1_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_CHANGEPHASE': tool.OperationClickOnImg('img/duel/main1.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
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
