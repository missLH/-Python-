import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ 响应按键事件 """
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True

    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE or event.key == pygame.K_j:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    # 按下空格键--创建了一颗子弹--加入编组bullets进行管理
    # 并对同时可以在屏幕上出现的子弹数量进行限制
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydup_events(event, ship):
    """ 响应松开按键事件 """
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 开始写驾驶飞船的代码 --按键控制左右
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keydup_events(event, ship)

def update_bullets(bullets):
    """ 重构函数，讲主程序子弹的管理代码封装到模块部分， 使得主程序简明 """
    bullets.update()

    for bullet in bullets.copy():
        #这里的top,bottom,left,right其实就是rect的边缘位置
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        #print(len(bullets))


def update_screen(ai_settings, screen, ship, bullets):
    """ 更新屏幕图像，并切换到新屏幕 这里需要传入参数，不然代码块中得新变量会显示未定义 """
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 在屏幕上更新子弹位置
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 更新飞船位置
    ship.blitme()

    # 让最近绘制的屏幕可见，每次执行while循环时都绘制一个空屏幕并擦去旧的，起到不断更新屏幕的作用
    pygame.display.flip()
