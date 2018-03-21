import pygame

from src.game_object.dynamic import Dynamic


class Projectile(Dynamic):
    
    def __init__(self, game, *, pos, depth, image):
        super().__init__(game, pos=pos, depth=depth, image=image)
        
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