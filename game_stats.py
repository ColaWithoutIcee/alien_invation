'''
# -*- coding: utf-8 -*-
@File    :   game_stats.py
@Time    :   2023/06/07 23:30:17
@Author  :   Jiabing SUN 
@Version :   1.0
@Contact :   Jiabingsun777@gmail.com
@Desc    :   None
'''

# here put the import lib
class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏刚刚启动时处于活动状态
        # self.game_active = True
        # 游戏刚刚运行时处于非活动状态，只有点击paly按钮才可以处于活动状态。
        self.game_active = False

        # 在任何状态下都不应该重置游戏的最高分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limits
        self.score = 0
        self.level = 1
