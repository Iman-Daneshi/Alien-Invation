class Settings:
    '''a class to store all settings for Alien Invasion.'''
    
    def __init__(self):
        '''initialize the game's settings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) 
        # ship settings
        self.ship_speed = 1.5
        self.ship_limits = 2
        # bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.allowed_bullets = 3
        # alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 100
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # how quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale