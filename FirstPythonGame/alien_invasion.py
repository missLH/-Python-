import sys
import pygame

from settings import Settings

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    # 创建一个Settings实例
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height ))
    pygame.display.set_caption('Alien Invasion')



    # 开始游戏的主循环
    while True:
        # 访问pygame检测到得事件，使用方法pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都重新绘制屏幕
        screen.fill(ai_settings.bg_color)

        # 让最近绘制的屏幕可见，每次执行while循环时都绘制一个空屏幕并擦去旧的，起到不断更新屏幕的作用
        pygame.display.flip()

run_game()
