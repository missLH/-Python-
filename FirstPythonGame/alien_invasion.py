import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from button import Button
from scoreborard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    # 创建一个Settings实例
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建paly按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # create a instance of Scoreborard
    sb = Scoreboard( ai_settings, screen, stats)
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
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 更新飞船位置
            ship.update()
            # 更新子弹位置 删除消失在屏幕外的子弹
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            # 更新外星人群的位置
            gf.update_aliens(ai_settings, stats, screen, ship, bullets, aliens)

        #更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)


run_game()
