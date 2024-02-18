class Settings():
    def __init__(self,screen_width = 1200,
        screen_height = 800,
        bg_color = (0, 0, 0)):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg_color = bg_color
        # 飞船的设置
        self.ship_speed_factor = 1.5
        # 子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1