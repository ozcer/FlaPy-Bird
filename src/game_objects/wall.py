import pygame

from src.const import *
from src.game_objects.scenic import Scenic


class Wall(Scenic):
    def __init__(self, *args, dim, depth=WALL_DEPTH, **kwargs):
        self.images = {"init": pygame.Surface(dim)}
        super().__init__(*args, depth=depth, init_image_key="init", **kwargs)
        
        self.image.fill(BLACK)
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
