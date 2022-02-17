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