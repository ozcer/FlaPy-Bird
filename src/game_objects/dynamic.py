import pygame
from src.game_objects.game_object import GameObject

class Dynamic(GameObject):
    
    def __init__(self, game, *, pos, depth, init_image_key, image_scale=(1, 1)):
        super().__init__(game,
                         pos=pos,
                         depth=depth,
                         init_image_key=init_image_key,
                         image_scale=image_scale)
        
        self.dx = 0
        self.dy = 0
        
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y