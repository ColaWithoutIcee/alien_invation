# -*- coding: utf-8 -*-
# @Time    : 2023/5/21 00:35
# @Author  : Jiabing SUN
# @Email   : jiabingsun777@gmail.com
# @File    : ship.py
# @Software: PyCharm
import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        # 初始化飞船并设置其初始位置
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 向右移动的标志
        self.moving_right = False
        # 向左移动的标志
        self.moving_left = False
        # 加载飞船图像并且获取其外接矩形
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        # 对于每艘新的飞船，都将这个飞船放在屏幕的中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        # self.x = self.rect.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """函数：用来更新飞船移动的位置"""
        # 这里用来直接更新飞船属性x的值，而不是更新ship.rect的x的值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x  # type: ignore


if __name__ == '__main__':
    print('Hello World!')
