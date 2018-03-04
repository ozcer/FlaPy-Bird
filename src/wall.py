import pygame
from pygame.locals import *

from src.const import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, dim):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = pos
        self.width, self.height = dim
        
        self.image = pygame.Surface(dim)
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
        # kinematics
        self.dx = -2
        self.dy = 0

    def update(self):
        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y
