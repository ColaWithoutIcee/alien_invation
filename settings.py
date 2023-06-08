# -*- coding: utf-8 -*-
# @Time    : 2023/5/21 00:15
# @Author  : Jiabing SUN
# @Email   : jiabingsun777@gmail.com
# @File    : settings.py
# @Software: PyCharm

class Settings:
    # 初始化所有的设置
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_speed = 2
        self.ship_limits = 2
        self.bg_color = (230, 230, 230)
        # 子弹设置
        self.bullet_speed = 3.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3 # 限制子弹的数量
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 60
        # fleet_direction为1表示向右移，-1表示向左移动
        self.fleet_direction = 1

if __name__ == '__main__':
    print('Hello World!')
