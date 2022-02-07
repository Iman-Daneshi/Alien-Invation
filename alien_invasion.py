import sys
import pygame

class AlienInvasion:
    '''overall class to manage game assets and behavior.'''
    def __init__(self):
        '''initialize the game, and creat game resourses.'''
        pygame.init()     # initializes the background settings that
                          # Pygame needs to work properly
        self.screen = pygame.display.set_mode((1200,800)) # to creat a 1200*600 display window
        pygame.display.set_caption("Alien Invasion")      # self.screen is called a "surface"

    def run_game(self):    # controls the game
        '''start the main loop for the game.'''
        while True:        
            # watch for keyword and mouse events.
            for event in pygame.event.get():     # it's an event loop
                if event.type == pygame.QUIT:    # event is an action that the user performs
                    sys.exit()

            # make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instanse, and run the game.
    ai = AlienInvasion()
    ai.run_game()
