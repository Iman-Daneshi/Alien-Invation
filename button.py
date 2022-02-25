import pygame


class Button:

    def __init__(self, ai_game, msg):
        
        pygame.init()
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # Set the dimensions and properties of the button.
        self.width , self.height = 200, 50
        self.play_color = (0, 0, 0)
        self.easy_color = (0, 255, 0)
        self.normal_color = (0, 255, 255)
        self.hard_color = (255, 0, 0)

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Calibri', 48, True)
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # The button message needs to be prepped only once.
        self._prep_msg(msg)
    
    def _prep_msg(self,msg):
        """Turn msg into a rendered image and center text on the button."""
        if msg == 'Play':
            self.msg_image = self.font.render(msg, True, self.text_color, 
                    self.play_color)      # Boolean value to turn antialiasing on or off (antialiasing
                                        # makes the edges of the text smoother).
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center
        elif msg == 'Easy':
            self.msg_image = self.font.render(msg, True, self.text_color, 
                    self.easy_color)     
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.centerx = self.rect.centerx - self.msg_image_rect.width
            self.msg_image_rect.centery = self.rect.centery + self.msg_image_rect.height
        elif msg == 'Normal':
            self.msg_image = self.font.render(msg, True, self.text_color, 
                    self.normal_color)      
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.centerx = self.rect.centerx 
            self.msg_image_rect.centery = self.rect.centery + self.msg_image_rect.height

        elif msg == 'Hard':
            self.msg_image = self.font.render(msg, True, self.text_color, 
                    self.hard_color)     
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.centerx = self.rect.centerx + self.msg_image_rect.width
            self.msg_image_rect.centery = self.rect.centery + self.msg_image_rect.height
       
    def _draw_button(self, msg ='Play'):
        # Draw blank button and then draw message.
        if msg == 'Play':
            self.screen.fill(self.play_color, self.rect)
        elif msg == 'Easy':
            self.screen.fill(self.easy_color, self.rect)
        elif msg == 'Normal':
            self.screen.fill(self.normal_color, self.rect)
        elif msg == 'Hard':
            self.screen.fill(self.hard_color, self.rect)
    
        self.screen.blit(self.msg_image, self.msg_image_rect)