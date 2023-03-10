import sys
import pygame
from bullet import Bullet
from alien import Alien
from star import Star
from raindrop import Raindrop

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
            
            
def update_screen(ai_settings, screen, ship, aliens, bullets, stars, raindrops):
    screen.fill(ai_settings.bg_color)
    raindrops.draw(screen)

    for star in stars:
        star.blitme()
    # bullets.sprites return a list containing all bullets.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)


    pygame.display.flip()
    
    
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()
        
        
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
        
    
def get_number_aliens(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2* alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 3*alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    

def generate_star(ai_settings, screen, stars):
    for i in range(10):
        new_star = Star(ai_settings, screen)
        stars.add(new_star)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def get_number_raindrops(ai_settings, raindrop_width):
    available_raindrop_x = ai_settings.screen_width - 2 * raindrop_width
    raindrops_number = int(available_raindrop_x / raindrop_width)
    return raindrops_number

def get_number_raindrops_row(ai_settings, raindrop_height):
    available_y = ai_settings.screen_height
    raindrops_number_rows = int(available_y / raindrop_height)
    return raindrops_number_rows

def create_raindrop(ai_settings, screen, raindrops, raindrop_number, raindrop_row):
    raindrop = Raindrop(ai_settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height
    raindrop.x = raindrop_width + 2 * raindrop_number * raindrop_width
    raindrop.y = raindrop_height + 2 * raindrop_row * raindrop_height
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = raindrop.y
    raindrops.add(raindrop)

def create_raindrops(ai_settings, screen, raindrops):
    raindrop = Raindrop(ai_settings, screen)
    r_w = raindrop.rect.width
    r_h = raindrop.rect.height
    number_x = get_number_raindrops(ai_settings, r_w)
    number_y = get_number_raindrops_row(ai_settings, r_h)
    for row_number in range(number_y):
        for number_column in range(number_x):
            create_raindrop(ai_settings, screen, raindrops, number_column, row_number)
