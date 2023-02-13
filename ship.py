import pygame

class Ship():
    
    def __init__(self,screen):
        #screen : initial position of the ship in the screen
        # Initialize the position in the screen
        self.screen = screen
        
        # Members defined:
        # Ships' image:
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Put the ship on the center of the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        #Draw the ship
        self.screen.blit(self.image, self.rect)
        
        