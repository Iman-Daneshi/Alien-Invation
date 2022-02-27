import pygame


class Button:

    def __init__(self, ai_game, msg):
        
        pygame.init()
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # Set the dimensions and properties of the button.
        self.width , self.height = 200, 50
        self.msg = msg

        # set color of buttons
        self._set_button_color()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Calibri', 48, True)
        # Build the buttons'rect object.
        self.make_rect()
        # The button message needs to be prepped only once.
        self._prep_msg()

    def _set_button_color(self):
        '''set buttoms color '''
        if self.msg == 'Easy':
            self.button_color = (0,255,0)
        elif self.msg == 'Normal':
            self.button_color = (255,255,0)
        elif self.msg == 'Hard':
            self.button_color = (255,0,0)
        elif self.msg == 'Play':
            self.button_color = (0,0,0)
        


    def make_rect(self):
        '''place each button in a right place based on their color'''
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if self.msg == 'Normal':
            self.rect.center = self.screen_rect.center
            self.rect.centery = self.screen_rect.centery + self.rect.height + 10
        elif self.msg == 'Easy':
            self.rect.centerx = self.screen_rect.centerx - self.rect.width -10
            self.rect.centery = self.screen_rect.centery + self.rect.height + 10
        elif self.msg == 'Hard':
            self.rect.centerx = self.screen_rect.centerx + self.rect.width +10
            self.rect.centery = self.screen_rect.centery + self.rect.height + 10
        elif self.msg == 'Play':
            self.rect.center = self.screen_rect.center

        
        
    
    def _prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, 
                self.button_color)      # Boolean value to turn antialiasing on or off (antialiasing
                                        # makes the edges of the text smoother).
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
       
    
        
            
       
    def _draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        

    