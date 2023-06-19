# -*- coding: utf-8 -*-
# @Time    : 2023/5/21 00:15
# @Author  : Jiabing SUN
# @Email   : jiabingsun777@gmail.com
# @File    : settings.py
# @Software: PyCharm

class Settings:
    # 初始化所有的设置
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limits = 0
        
        # 子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3 # 限制子弹的数量

        # 外星人设置
        self.fleet_drop_speed = 100
        

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """初始化随游戏进行儿变化的位置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction为1表示向右移，-1表示向左移动
        self.fleet_direction = 1

        # 记分
        self.alien_point = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.score_scale)

if __name__ == '__main__':
    print('Hello World!')
