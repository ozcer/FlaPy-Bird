import pygame
from src.game_objects.game_object import GameObject

class Dynamic(GameObject):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
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