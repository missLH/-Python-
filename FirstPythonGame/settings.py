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
        self.ship_speed_factor = 3

        # 子弹设置
        self.bullet_speed_factor = 29
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 20
