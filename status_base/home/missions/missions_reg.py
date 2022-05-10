'''
Author: your name
Date: 2022-04-09 23:34:32
LastEditTime: 2022-05-10 12:06:41
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \master_duel_assist\status_base\home\missions\home_reg.py
'''
'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-04-09 13:56:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''




import tool
import logging
from status_base.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update
class STATUS_MISSIONS(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_HOME': tool.OperationClickOnImg('img/base/back.png', is_cache=False),
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list += [
            tool.ProofImg('img/home/missions/ing.png')
        ]


# class STATUS_MISSIONS_HAVE_AWARDS(STATUS_MISSIONS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_MISSIONS_NO_AWARDS': tool.OperationLeftClick([1105, 664])
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list += [
#             tool.ProofImg('img/home/missions/have_awards.png')
#         ]


# class STATUS_MISSIONS_NO_AWARDS(STATUS_MISSIONS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_HOME': tool.OperationClickOnImg('img/base/back.png', is_cache=False),
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list += [
#             tool.ProofImg('img/home/missions/have_awards.png', is_exist=False)
#         ]
