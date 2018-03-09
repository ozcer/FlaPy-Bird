import pygame

from src.const import *

class Floor(pygame.sprite.Sprite):
    def __init__(self, game, pos, dim=(2000, 50)):
        self.game = game
        
        
        self.image = pygame.Surface(dim)
        self.rect = self.image.get_rect()
        self.color = D_OLIVE
        self.image.fill(self.color)
        
        self.x, self.y = pos