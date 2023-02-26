import sys
import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

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
    ship = Ship(ai_settings,screen)
    
    # Group for bullets generated
    bullets = Group()

    # Loop to start game
    while True:
        # Check keyboard event, defined in game_functions
        gf.check_events(ai_settings, screen, ship, bullets)
        
        # Update the position of the ship
        ship.update()
        
        gf.update_bullets(bullets)
            
        # A function defined in game_functions.py to draw a new screen and show it
        gf.update_screen(ai_settings, screen, ship, bullets)
        


run_game()
