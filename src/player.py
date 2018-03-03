import pygame
from pygame.locals import *

from src.const import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, dim):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = pos
        self.width, self.height = dim
        
        # red rect
        self.image = pygame.Surface(dim)
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # kinematics
        self.dx = 0
        self.dy = 0
        
    
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_SPACE] and self.dy > -1:
            self.dy -= 10
        
        # gravity
        if self.rect.bottom < DISPLAY_HEIGHT:
            self.dy += GRAV if self.dy < TERM_VEL else 0
        else:
            self.dy = 0
        
        
        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y

        print(self.dy)
        
        