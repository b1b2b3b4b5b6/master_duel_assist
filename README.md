<!--
 * @Author: b1b2b3b4b5b6 a1439458305@163.com
 * @Date: 2022-05-05 17:39:09
 * @LastEditors: b1b2b3b4b5b6 a1439458305@163.com
 * @LastEditTime: 2022-06-12 09:14:07
 * @FilePath: \master_duel_assist\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# master_duel_assist

master duel  辅助挂机脚本，适用于steam版本程序, 脚本稳定性高, 几乎不会卡死
支持：活动挂机（卡组无手坑），每日任务自杀和自动领钻(自杀卡组，稳定拿120钻)，定时开启关闭游戏做任务

#### 环境要求

- steam版duel_master
- 游戏设置
  - 游戏语言英文
  - 窗口分辨率1280*720，高画质
  - 文本大小中等
![img](https://raw.githubusercontent.com/b1b2b3b4b5b6/pic/main/PicGo/202206120907523.png)
- 决斗设置
  - 设置自动选择卡片位置
  - 设置手牌被选中时，命令显示在怪兽区域上（决斗设置-倒数第二个，设为set）
  - 设置自动连锁
  - 关闭自我连锁
![img](https://raw.githubusercontent.com/b1b2b3b4b5b6/pic/main/PicGo/202206120907521.png)
![img](https://raw.githubusercontent.com/b1b2b3b4b5b6/pic/main/PicGo/202206120907520.png)
- 根据requirements.txt安装必要python库
- 推荐自杀卡组

![](https://raw.githubusercontent.com/b1b2b3b4b5b6/pic/main/PicGo/202206120858460.png)

#### 使用

- 登录steam
- 复制config.json.template到config.json, 修改定时和任务类型
- 运行main.py(当前时间在定时范围内才会启动游戏, 定时范围外启动游戏会被脚本杀掉)
