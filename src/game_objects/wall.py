import pygame

from src.const import *
from src.game_objects.scenic import Scenic


class Wall(Scenic):
    def __init__(self, game, *,
                 pos,
                 dim,
                 depth=WALL_DEPTH):
        self.images = {"init": pygame.Surface(dim)}
        super().__init__(game, pos=pos, depth=depth, init_image_key="init")
        
        self.image.fill(BLACK)
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
