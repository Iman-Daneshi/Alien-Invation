import sys
from tkinter import S
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from game_stats import GameState
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import ScoreBoard

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
        # create an instance to store game statics
        self.stats = GameState(self)    
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # make the play button
        self.play_button = Button(self,"play")
        # Create an instance to store game statistics,
        # and create a scoreboard.
        self.sb = ScoreBoard(self)

    def run_game(self):    # controls the game
        '''start the main loop for the game.'''
        while True:        
            # watch for keyword and mouse events.
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _create_fleet(self):
        '''a method to create a fleet of aliens'''
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        available_space_X = (self.settings.screen_width) - (4 * alien_width)
        number_aliens_X = available_space_X // (2 * alien_width)

        # detremine the number of rows that the fleet can have
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height) - (3 * alien_height) - ship_height
        number_rows = available_space_y // (3 * alien_height)
        
        # create the first row of aliens
        for row_number in range (number_rows - 6):
            alien.y = alien_height + 3 * alien_height * row_number
            for alien_number in range(number_aliens_X + 1):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            

    def _create_alien(self, alien_number, row_number):
        '''create an alien and put it in the row'''
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        alien.x = 2 * alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = 2 * alien_height + 3 * alien_height * row_number
        self.aliens.add(alien) 

    def _update_aliens (self):
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        '''update the position of all aliens in the fleet'''
        self.aliens.update()
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):        
            self._ship_hit()
        # looking for aliens hitting the bottom
        self._check_aliens_bottom()
            
    def _ship_hit(self):
        '''response to the ship being hit by an alien'''
        if self.stats.ships_left > 0:
            #decrement ship_left
            self.stats.ships_left -= 1
            # get rid of any remaining aliens or bullets 
            self.bullets.empty()
            self.aliens.empty()
            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        '''check if any aliens reched the bottom'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # react as aliens collided with ship
                self._ship_hit()
                break
        

    def _update_bullets (self):
        self.bullets.update()
            #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                        self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len (aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
    def _check_events(self):
            '''Respond to keypresses and mouse events.'''
            for event in pygame.event.get():     # it's an event loop
                if event.type == pygame.QUIT:    # event is an action that the user performs
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events (event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events (event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        '''start a new game when the mouse click play button'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            # reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            #get rid of remained aliens' ships and bullets
            self.aliens.empty()
            self.bullets.empty()
            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            #make the mouse invisible
            pygame.mouse.set_visible(False)

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
            if not self.stats.game_active:
                self.play_button._draw_button()
            # Draw the score information.
            self.sb.show_score()
            # make the most recently drawn screen visible.
            pygame.display.flip()    # This will update the contents of the entire display

if __name__ == '__main__':
    # make a game instanse, and run the game.
    ai = AlienInvasion()
    ai.run_game()