import pygame
from pygame.sprite import Sprite
class Raindrop(Sprite):
    def __init__(self,screen,ai_settings):
        super().__init__()
        self.image = pygame.image.load('images/raindrop.bmp')

        self.rect = self.image.get_rect()
        self.screen = screen
        self.ai_settings = ai_settings
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def update_raindrops(self):
        self.rect.y += self.ai_settings.rain_drop_speed

    def check_edges(self):
        if self.rect.bottom >= self.screen.get_rect().height:
            return True
