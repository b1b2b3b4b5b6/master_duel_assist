'''
Author: your name
Date: 2022-04-09 15:12:49
LastEditTime: 2022-04-10 01:43:33
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \master_duel_assist\status_base\rank\festival_reg.py
'''
'''
Author: your name
Date: 2021-03-04 21:33:52
LastEditTime: 2022-04-09 13:56:18
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\pvp_reg.py
'''




import tool
import logging
from status_base.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update
class STATUS_RANK_MYDECK(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_DUEL_MAIN1': tool.OperationClickOnImg('img/rank/start_duel.png'),
            'STATUS_HOME': tool.OperationClickOnImg('img/base/back.png', is_cache=False),
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/rank/ing.png')
        ]
