import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    # 创建一个Settings实例
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于管理子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 访问pygame检测到得事件,讲代码块封装到gf模块中，分离逻辑，使得主逻辑更清晰明了
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船位置
        ship.update()
        # 更新子弹位置
        bullets.update()
        #更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
