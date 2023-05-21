# -*- coding: utf-8 -*-
# @Time    : 2023/5/20 00:40
# @Author  : Jiabing SUN
# @Email   : jiabingsun777@gmail.com
# @File    : alien_invasion.py
# @Software: PyCharm
import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")
        # 设置背景色
        # self.bg_color = (230, 230, 230)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视鼠标和键盘事件
            self._check_event()
            self.ship.update()
            self._update_screen()
            # 让最近绘制的屏幕可见
            pygame.display.flip()

    def _check_event(self):
        """响应鼠标和键盘事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # self.ship.rect.x += 1
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并且切换到新的屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


if __name__ == '__main__':
    # 创建游戏示例并开始游戏
    ai = AlienInvasion()
    ai.run_game()
