import sys

import pygame
from bullet import Bullet
from alien import Alien

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
    # 方便退出游戏-快捷键
    elif event.key == pygame.K_q:
        sys.exit()

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

def update_bullets(ai_settings, screen, ship, bullets, aliens):
    """ 重构函数，讲主程序子弹的管理代码封装到模块部分， 使得主程序简明 """
    bullets.update()

    for bullet in bullets.copy():
        #这里的top,bottom,left,right其实就是rect的边缘位置
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        #print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)

def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens):
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def create_fleet_x(ai_settings, screen, aliens, row_number):
    """ 这里不打算重构，会变得更复杂 """
    alien = Alien(ai_settings, screen)
    number_alien_x =int((ai_settings.screen_width - (2 * alien.alien_width)) / (2 * alien.alien_width))

    for alien_number in range(number_alien_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien.alien_width + 2 * alien.alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.alien_height + 2 * alien.alien_height * row_number
        aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """ """
    alien = Alien(ai_settings, screen)
    number_rows = int((ai_settings.screen_height - (3 * alien.alien_height) - ship.ship_height) / (2 * alien.alien_height))

    for row_number in range(number_rows):
        create_fleet_x(ai_settings, screen, aliens, row_number)

def check_fleet_edges(ai_settings, aliens):
    """ 在外星人到达边缘时发生的行为 """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            # 这个break非常重要不能遗漏， 表示只有在下一次的碰壁时才会触发，不然在for循环中，change_fleet_direction会一直执行。fleet_direction会一直改变
            break

def change_fleet_direction(ai_settings, aliens):
    """ 讲外星人群整体向下拉，然后改变方向 """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, ship, aliens):
    """ 更新外星人群的位置 """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        print('You lost one chance.')

def update_screen(ai_settings, screen, ship, bullets, aliens):
    """ 更新屏幕图像，并切换到新屏幕 这里需要传入参数，不然代码块中得新变量会显示未定义 """
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 在屏幕上更新子弹位置
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 更新飞船位置
    ship.blitme()
    #
    aliens.draw(screen)

    # 让最近绘制的屏幕可见，每次执行while循环时都绘制一个空屏幕并擦去旧的，起到不断更新屏幕的作用
    pygame.display.flip()
