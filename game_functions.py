import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        # Movements
        # Every button pressed will be registered as a KEYDOWN event in pygame
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
             
        # Release the button
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

            
def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    
    # bullets.sprites return a list containing all bullets.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    pygame.display.flip()
    
    
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
        
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def update_bullets(bullets):
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)