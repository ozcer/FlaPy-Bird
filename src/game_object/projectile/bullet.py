import pygame

from src.const import *
from src.game_object.dynamic import Dynamic


class Bullet(Dynamic):
    
    def __init__(self,
                 game,
                 pos,
                 dim=(10,10),
                 depth=-2):
        super().__init__()
        self.game = game
        
        self.x, self.y = pos
        self.width, self.height = dim
        
        self.image = pygame.Surface(dim)
        self.image.fill(YELLOW)
        
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
        self.depth = depth

        # kinematics
        self.dx = 8
        self.dy = 0

    def draw(self):
        super().draw()
    
    def update(self):
        super().update()

