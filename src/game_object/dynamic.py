import pygame
from src.game_object.game_object import GameObject

class Dynamic(GameObject):
    
    def __init__(self, game, *, pos, depth, image):
        super().__init__(game, pos=pos, depth=depth, image=image)
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y