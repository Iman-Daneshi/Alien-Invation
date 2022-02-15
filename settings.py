class Settings:
    '''a class to store all settings for Alien Invasion.'''
    
    def __init__(self):
        '''initialize the game's settings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) 
        # ship settings
        self.ship_speed = 10
        # bullet settings
        self.bullet_speed = 20
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.allowed_bullets = 5
        # alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1