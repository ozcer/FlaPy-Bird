import pygame
from pygame.locals import *

from src.const import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, pos,):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        
        
        # sprite
        self.sprites = {"jump": pygame.image.load("sprites/jump.png"),
                        "fall": pygame.image.load("sprites/fall.png")}
        self.image = self.sprites["fall"]

        self.x, self.y = pos
        
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.width = self.rect.width
        self.height = self.rect.height
        
        # kinematics
        self.dx = 0
        self.dy = 0
        
        self.alive = True
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if self.alive:
            # up
            if keys[K_w] and self.dy > -MAX_UP_SPEED:
                self.dy -= UP_ACCEL
                self.image = self.sprites["jump"]
            
            # horizontal
            # if keys[K_d]:
            #     self.game.pan_speed += 3
            # elif keys[K_a]:
            #     self.game.pan_speed = -3
            # else:
            #     self.dx = 0

        
    def update(self):
        self.handle_input()
        
        if self.dy > 0:
            self.image = self.sprites["fall"]
        
        # gravity
        self.dy += GRAV if self.dy < MAX_DOWN_SPEED else 0
        
        # off screen death
        if not (0 < self.x < DISPLAY_WIDTH and 0 < self.y < DISPLAY_HEIGHT):
            self.alive = True # False

        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y
