# -*- coding: utf-8 -*-
# @Time    : 2023/5/20 00:40
# @Author  : Jiabing SUN
# @Email   : jiabingsun777@gmail.com
# @File    : alien_invasion.py
# @Software: PyCharm
import sys
import pygame


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视鼠标和键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # 让最近绘制的屏幕可见
                pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏示例并开始游戏
    ai = AlienInvasion()
    ai.run_game()
