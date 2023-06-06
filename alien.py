'''
# -*- coding: utf-8 -*-
@File    :   alien.py
@Time    :   2023/06/06 10:56:35
@Author  :   Jiabing SUN 
@Version :   1.0
@Contact :   Jiabingsun777@gmail.com
@Desc    :   None
'''

# here put the import lib
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类。"""
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并且设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都显示在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的精确位置
        self.x = float(self.rect.x)
