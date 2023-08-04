class Settings:
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1300 #1200改为130
        self.screen_height = 650 #800改为650
        self.bg_color = (230, 230, 230)
        #飞船的设置
        self.ship_speed = 6
        #子弹设置
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3


        