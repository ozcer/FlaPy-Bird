import pygame

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
        # gravity
        if self.rect.y < DISPLAY_HEIGHT:
            self.dy += GRAV

        self.x += self.dx
        self.y += self.dy
        
        self.rect.center = self.x, self.y