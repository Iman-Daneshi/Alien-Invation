class Settings:
    '''a class to store all settings for Alien Invasion.'''
    
    def __init__(self):
        '''initialize the game's settings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) 
        # ship settings
        self.ship_speed = 5
        # bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.allowed_bullets = 5