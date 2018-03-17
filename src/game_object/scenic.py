import pygame

from src.const import *
from src.game_object.game_object import GameObject


class Scenic(GameObject):
    
    def __init__(self):
        super().__init__()
    
    
    def decayable(self):
        """
        check if is too far out from main surface
        :return: bool
        """
        # active zone = main surface x 2
        active_zone = self.game.surface.get_rect().inflate(self.rect.width*2, DISPLAY_HEIGHT/2)
        return not active_zone.colliderect(self.rect)
    
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        self.x += -self.game.pan_speed
        
        if self.decayable():
            #print(f"{self} decaying")
            self.kill()
    