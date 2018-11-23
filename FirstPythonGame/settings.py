#创建这个Settings类的原因是为了更加方便的修改游戏设置，
#如果你后面想更改游戏设置，就不必要去主程序上进行修改，找参数等都很花时间
#同时代价是你必须将此文件作为模块导入到主程序中，并且使用Settings类进行编码
class Settings():
    """ """

    def __init__(self):
        """ """
        # 窗口的数据
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船运动速度
        self.ship_speed_factor = 20

        # 子弹设置
        self.bullet_speed_factor = 1
        self.ship_limit = 3
        self.bullet_width = 2
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 80900

        # 外星人设置
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10
        # fleet_direction = 1 mean to right, -1 to left
        self.fleet_direction = 1

        # the speed rhythm
        self.speedup_scale = 1.3
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initialize the settings with the game change """
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 3


        self.fleet_direction = 1

        # count the score
        self.alien_points = 50

    def increase_speed(self):

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
