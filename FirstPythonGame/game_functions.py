import sys

import pygame

def check_keydown_events(event, ship):
    """ 响应按键事件 """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keydup_events():
    """ 响应松开按键事件 """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(ship):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 开始写驾驶飞船的代码 --按键控制左右
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keydup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """ 更新屏幕图像，并切换到新屏幕 这里需要传入参数，不然代码块中得新变量会显示未定义 """
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见，每次执行while循环时都绘制一个空屏幕并擦去旧的，起到不断更新屏幕的作用
    pygame.display.flip()
