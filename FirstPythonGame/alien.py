# 进入第三部分 创建外星人类、

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        """ 初始化外星人 并设置其起始位置 """

        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #这里不懂得去查一下pygame Rect rect 这里设置每个外星人最初的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储 外星人的准确位置
        self.x = float(self.rect.x)

        self.alien_width = self.rect.width
        self.alien_height = self.rect.height

    def check_edges(self):
        """ 如果运动到了边缘就返回true """
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ 向左或向右 """

        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """ 在指定位置绘制alien """
        self.screen.blit(self.image, self.rect)
