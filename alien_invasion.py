import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''overall class to manage game assets and behavior.'''
    def __init__(self):
        '''initialize the game, and creat game resourses.'''
        pygame.init()     # initializes the background settings that
                          # Pygame needs to work properly
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")      
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def run_game(self):    # controls the game
        '''start the main loop for the game.'''
        while True:        
            # watch for keyword and mouse events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._create_fleet()
            self._update_screen()

    def _create_fleet(self):
        '''a method to create a fleet of aliens'''
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        available_space_X = (self.settings.screen_width) - (2 * alien_width)
        number_aliens_X = available_space_X // (2 * alien_width)

        # detremine the number of rows that the fleet can have
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height) - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        
        # create the first row of aliens
        for row_number in range (number_rows):
            alien.y = alien_height + 2 * alien_height * row_number
            for alien_number in range(number_aliens_X + 1):
                self._create_alien(alien_number, row_number)
            

    def _create_alien(self, alien_number, row_number):
        '''create an alien and put it in the row'''
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien) 
            
    
    def _update_bullets (self):
        self.bullets.update()
            #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            
    def _check_events(self):
            '''Respond to keypresses and mouse events.'''
            for event in pygame.event.get():     # it's an event loop
                if event.type == pygame.QUIT:    # event is an action that the user performs
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events (event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events (event)

    def _check_keydown_events (self, event):
        if event.key == pygame.K_RIGHT:
            # take the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # take the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events (self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''create a  new bullets and add it to the bullets's group'''
        if len(self.bullets) < self.settings.allowed_bullets:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        



    def _update_screen (self):
            """Update images on the screen, and flip to the new screen."""
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            # draw aleins to the screen
            self.aliens.draw(self.screen)

            # make the most recently drawn screen visible.
            pygame.display.flip()    # This will update the contents of the entire display


if __name__ == '__main__':
    # make a game instanse, and run the game.
    ai = AlienInvasion()
    ai.run_game()
