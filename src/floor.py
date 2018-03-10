import pygame

from src.const import *
from src.scenic_object import ScenicObject
from src.kinematic import Kinematic

class Floor(ScenicObject, Kinematic):
    def __init__(self, game, pos=None, dim=(DISPLAY_WIDTH, 20)):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        
        self.image = pygame.Surface(dim)
        self.rect = self.image.get_rect()
        self.color = D_OLIVE
        self.image.fill(self.color)
        self.depth = 0
        
        if pos is None:
            x = DISPLAY_WIDTH + dim[0]/2
            y = DISPLAY_HEIGHT - dim[1]/2
            pos = (x, y)
        self.x, self.y = pos

        # kinematics
        self.dx = 0
        self.dy = 0
    
    def update(self):
        self.pan()
        self.apply_kinematic()