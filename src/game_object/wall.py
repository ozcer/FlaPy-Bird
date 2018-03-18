import pygame

from src.const import *
from src.game_object.scenic import Scenic


class Wall(Scenic):
    def __init__(self, game, *,
                 pos,
                 dim,
                 depth=1):
        image = pygame.Surface(dim)
        super().__init__(game, pos=pos, depth=depth, image=image)
        
        self.image.fill(BLACK)

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
