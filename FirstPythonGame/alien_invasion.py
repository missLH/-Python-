import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    # 创建一个Settings实例
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于管理子弹的编组
    bullets = Group()
    # 创建一个外星人编组用于管理, 再创建一个群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 访问pygame检测到得事件,讲代码块封装到gf模块中，分离逻辑，使得主逻辑更清晰明了
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船位置
        ship.update()
        # 更新子弹位置 删除消失在屏幕外的子弹
        gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
        # 更新外星人群的位置
        gf.update_aliens(ai_settings, ship, aliens)
        #更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()
