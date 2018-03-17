import pygame

from src.const import *
from src.game_object.scenic import Scenic
from src.game_object.dynamic import Dynamic


class Wall(Scenic):
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
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()

        if self.hit:
            self.image.fill(RED)
        
        
