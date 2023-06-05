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
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion")
        # 设置背景色
        # self.bg_color = (230, 230, 230)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视鼠标和键盘事件
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            # 让最近绘制的屏幕可见
            


    def _check_event(self):
        """响应鼠标和键盘事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _update_screen(self):
        """更新屏幕上的图像，并且切换到新的屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE: 
            self._fire_bullet()

    def _check_keyup_event(self, event):
        """按键松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入到编组bullet中"""
        if len(self.bullets) < self.settings.bullet_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """更新子弹的位置并且删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))  # 测试子弹是否真的飞出屏幕。

if __name__ == '__main__':
    # 创建游戏示例并开始游戏
    ai = AlienInvasion()
    ai.run_game()
