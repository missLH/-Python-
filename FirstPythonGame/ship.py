#我们创建这个类用来管理和设置飞船的大部分行为
import pygame

class Ship():

    def __init__(self, screen):
        """ 初始化飞船并设置其初始位置 """
        self.screen = screen

        # 加载图片 并且 获得图片和游戏屏幕的外界矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 给飞船在屏幕定位，放在中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)
        
