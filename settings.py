import pygame

class Settings():
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"
        self.ship_speed_factor = 1.5
        
        # settings for bullet:
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Move symbols for aliens
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1: right -1: left
        self.fleet_direction = 1

        self.rain_drop_speed = 10
        