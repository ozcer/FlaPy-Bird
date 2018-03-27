import pygame

from src.game_objects.dynamic import Dynamic
from src.game_objects.foes.foe import Foe


class Projectile(Dynamic):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def decayable(self):
        """
        Overriding decayable in GameObject
        :return: bool
        """
        active_zone = self.game.surface.get_rect()
        return not active_zone.colliderect(self.rect)

    def draw(self):
        super().draw()

    def update(self):
        super().update()
