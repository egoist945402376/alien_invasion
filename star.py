import pygame
from random import randint
from pygame.sprite import Sprite
from ship import Ship
class Star(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/star.bmp')

        ship = Ship(ai_settings, screen)

        self.ai_settings = ai_settings

        self.rect = self.image.get_rect()
        self.rect.width = ship.rect.width
        self.rect.height = ship.rect.height

        self.screen_rect = screen.get_rect()

        self.random_row = randint(1, 9)
        self.random_column = randint(1, 9)

        self.rect.top = int((ai_settings.screen_height - 200) / self.random_column)
        self.rect.left = int((ai_settings.screen_width - 200) / self.random_row)


    def blitme(self):
        print(self.rect.height)
        self.screen.blit(self.image, self.rect)