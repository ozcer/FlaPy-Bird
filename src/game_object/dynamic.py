import pygame
from src.game_object.game_object import GameObject

class Kinematic(GameObject):
    
    def __init__(self):
        super().__init__()
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y