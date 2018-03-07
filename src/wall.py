

import pygame
from pygame.locals import *

from src.const import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, pos, dim):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        self.x, self.y = pos
        self.width, self.height = dim
        self.image = pygame.Surface(dim)
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        
        # kinematics
        self.dx = -WALL_SPEED
        self.dy = 0
        
        # collision
        self.hit = False
        
    def update(self):
        if self.hit:
            self.image.fill(RED)
        
        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y
        
        # leaves screen
        if self.rect.right < 0:
            del self
