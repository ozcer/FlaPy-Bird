

import pygame
from pygame.locals import *

from src.const import *
from src.scenic_object import ScenicObject
from src.kinematic import Kinematic

class Wall(ScenicObject, Kinematic):
    def __init__(self, game, pos, dim):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        self.x, self.y = pos
        self.width, self.height = dim
        
        self.image = pygame.Surface(dim)
        self.rect = self.image.get_rect()
        self.image.fill(BLACK)
        self.depth = 1

        # kinematics
        self.dx = 0
        self.dy = 0
        
        # collision
        self.hit = False
        
    def update(self):
        self.pan()
        
        if self.hit:
            self.image.fill(RED)
        
        self.apply_kinematic()
        
        # leaves screen
        if self.rect.right < 0:
            del self
