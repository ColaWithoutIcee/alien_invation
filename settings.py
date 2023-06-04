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
        self.bg_color = (230, 230, 230)
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

if __name__ == '__main__':
    print('Hello World!')
