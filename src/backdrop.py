import pygame

from src.const import *
from src.scenic_object import ScenicObject
from src.kinematic import Kinematic


class Backdrop(ScenicObject, Kinematic):
    depth = 10
    
    def __init__(self, game, left=None, dim=(BACKDROP_WIDTH, BACKDROP_HEIGHT), color=L_GREY):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        
        self.image = pygame.Surface(dim)
        self.color = color
        self.image.fill(self.color)
        self.depth = Backdrop.depth
        
        if left is not None:
            self.x = left + dim[0] / 2
            self.y = BACKDROP_HEIGHT - dim[1] / 2
        # default spawn at right of screen
        else:
            self.x = DISPLAY_WIDTH + dim[0] / 2
            self.y = BACKDROP_HEIGHT - dim[1] / 2
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
        # kinematics
        self.dx = 0
        self.dy = 0
        
        self.extended = False
    
    def extend(self):
        print("extending")
        self.extended = True
        color = D_GREY if self.color == L_GREY else L_GREY
        
        extension = Backdrop(self.game, left=self.rect.right - 10, color=color)
        self.game.add_entity(extension)
    
    def update(self):
        if self.rect.left <= 0 and not self.extended:
            self.extend()
        self.pan()
        self.apply_kinematic()

