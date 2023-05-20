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
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并且获取其外接矩形
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新的飞船，都将这个飞船放在屏幕的中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    print('Hello World!')
