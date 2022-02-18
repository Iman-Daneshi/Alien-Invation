import pygame.font

class ScoreBoard():
    '''a class to manage the game's scoreboard and keep the toppest score'''
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        # Font settings for scoring information.
        self.text_color = (60,60,60)
        self.font = pygame.font.SysFont(None,48)
        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_level(self):
        '''turn the game level into a rendered image'''
        level_str = str (self.stats.level)
        self.level_image = self.font.render(level_str,True,
                    self.text_color, self.settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.screen_rect.right - 10
        self.level_image_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = f"{rounded_high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, 
                        self.text_color, self.settings.bg_color)
        # place the high score at the top middle of the screen
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.midtop = self.screen_rect.midtop

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round (self.stats.score)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        '''display the score at the top right side of the screen '''
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top

    def show_score(self):
        '''draw the score to the screen.'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
    
    def check_high_score(self):
        if (self.stats.score >= self.stats.high_score):
            self.stats.high_score = self.stats.score
            self.prep_high_score()