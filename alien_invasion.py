import sys
import pygame

def run_game():
    # Initialize the background and run the pygame
    pygame.init()
    
    # Create a window
    #(1200, 800) is a tuple indicates the size of the window
    
    # screen is a surface
    # surface is a part of the screen, used to represent the game element
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    
    # set the background color
    bg_color = (230,230,230)

    # Loop to start game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)
        
        # Show the screen
        pygame.display.flip()
