import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        #screen : initial position of the ship in the screen
        # Initialize the position in the screen
        self.screen = screen
        
        # game settings
        self.ai_settings = ai_settings
        
        # Members defined:
        # Ships' image:
        self.image = pygame.image.load('images/ship.bmp')
        
        # Ship's initial rectangle
        self.rect = self.image.get_rect()
        
        # Rectangle of the screen
        self.screen_rect = screen.get_rect()
            
        # Put the ship on the center of the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Float number of ship's position in x axis
        self.centerinx = float(self.rect.centerx)
        
        # Flag to indicate movement
        self.moving_right = False
        
        self.moving_left = False
        
        self.moving_forward = False
        
        self.moving_back = False
    
    # method to move the ship:
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerinx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerinx -= self.ai_settings.ship_speed_factor
            
        self.rect.centerx = self.centerinx
        
        '''if self.moving_forward:
            self.rect.centery += 1
        if self.moving_forward:
            self.rect.centery -= 1'''
            
        
        
        
    
        
    def blitme(self):
        #Draw the ship
        self.screen.blit(self.image, self.rect)
        
        