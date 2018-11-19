#我们创建这个类用来管理和设置飞船的大部分行为
import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """ 初始化飞船并设置其初始位置 """
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图片 并且 获得图片和游戏屏幕的外界矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 给飞船在屏幕定位，放在中央
        self.rect.centerx = self.screen_rect.centerx

        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ 更具移动标志来更新飞船的位置，并且划定了飞船运动的范围 """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x +=  self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center_y -=  self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom >= 0:
            self.center_y += self.ai_settings.ship_speed_factor

        # 根据self.center更新self.rect对象
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y




    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)
