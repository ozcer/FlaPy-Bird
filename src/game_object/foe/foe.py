import pygame

from src.game_object.dynamic import Dynamic
from src.const import *


class Foe(Dynamic):

    def __init__(self,
                 game, *,
                 pos,
                 depth,
                 image):
        super().__init__(game, pos=pos, depth=depth, image=image)
    
    def decayable(self):
        """
        Overriding decayable in GameObject
        :return: bool
        """
        return self.rect.right < 0
    
    def draw(self):
        super().draw()
    
    def is_alive(self):
        return self.hp > 0
    
    def update(self):
        super().update()
        
        if not self.is_alive():
            self.kill()



