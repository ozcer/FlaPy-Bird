import pygame

from src.const import *
from src.game_object.dynamic import Dynamic


class Bullet(Dynamic):
    
    def __init__(self,
                 game,
                 pos,
                 dim=(10,10),
                 depth=-2):
        image = pygame.Surface(dim)
        super().__init__(game, pos=pos, depth=depth,image=image)
        self.game = game
        
        self.image.fill(YELLOW)
        
        # kinematics
        self.dx = 8
        self.dy = 0

    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()

