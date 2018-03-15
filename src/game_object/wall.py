import pygame

from src.const import *
from src.game_object.scenic_object import ScenicObject
from src.game_object.kinematic import Kinematic


class Wall(ScenicObject, Kinematic):
    depth = 1
    def __init__(self, game, pos, dim):
        super().__init__()
        self.game = game

        self.x, self.y = pos
        self.width, self.height = dim
        
        self.image = pygame.Surface(dim)
        self.image.fill(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
        self.depth = Wall.depth

        # kinematics
        self.dx = 0
        self.dy = 0
        
        # collision
        self.hit = False
        
    def update(self):
        super().update()

        self.show_attribute()

        if self.hit:
            self.image.fill(RED)
        
        
