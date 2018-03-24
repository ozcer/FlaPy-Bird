import pygame

from src.const import *
from src.game_object.scenic import Scenic


class Wall(Scenic):
    def __init__(self, game, *,
                 pos,
                 dim,
                 depth=WALL_DEPTH):
        self.images = {0: pygame.Surface(dim)}
        super().__init__(game, pos=pos, depth=depth, image=self.images[0])
        
        self.image.fill(BLACK)
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
