import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''overall class to manage game assets and behavior.'''
    def __init__(self):
        '''initialize the game, and creat game resourses.'''
        pygame.init()     # initializes the background settings that
                          # Pygame needs to work properly
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)) # to creat a 1200*600 display window
        pygame.display.set_caption("Alien Invasion")      # self.screen is called a "surface"
        self.ship = Ship(self)

    def run_game(self):    # controls the game
        '''start the main loop for the game.'''
        while True:        
            # watch for keyword and mouse events.
            self._check_events()
            self._update_screen()
            
    def _check_events(self):
            '''Respond to keypresses and mouse events.'''
            for event in pygame.event.get():     # it's an event loop
                if event.type == pygame.QUIT:    # event is an action that the user performs
                    sys.exit()

    def _update_screen (self):
            """Update images on the screen, and flip to the new screen."""
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make the most recently drawn screen visible.
            pygame.display.flip()    # This will update the contents of the entire display


if __name__ == '__main__':
    # make a game instanse, and run the game.
    ai = AlienInvasion()
    ai.run_game()
