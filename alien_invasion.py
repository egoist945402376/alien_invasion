import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Initialize the background and run the pygame
    pygame.init()
    
    # Setting class instance
    # which includes arguments about game settings.
    ai_settings = Settings()
    
    
    # Create a window
    #(1200, 800) is a tuple indicates the size of the window
    
    # screen is a surface
    # surface is a part of the screen, used to represent the game element
    # Create a surface by pygame.display.set_mode() 
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.title)
    
    # set the background color
    # bg_color = (230,230,230)

    # Create a ship
    ship = Ship(screen)

    # Loop to start game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # Show the screen
        pygame.display.flip()
        


run_game()
