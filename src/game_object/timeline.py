import pygame

from src.const import *
from src.game_object.scenic_object import ScenicObject
from src.game_object.kinematic import Kinematic


class Timeline(ScenicObject, Kinematic):
    depth = 0
    
    def __init__(self, game, left=None, dim=(TL_WIDTH, TL_HEIGHT), color=OLIVE):
        super().__init__()
        self.game = game
        
        self.image = pygame.Surface(dim)
        self.color = color
        self.image.fill(self.color)
        self.depth = Timeline.depth
        
        if left is not None:
            self.x = left+ dim[0]/2
            self.y = DISPLAY_HEIGHT - dim[1]/2
        # default spawn at right of screen
        else:
            self.x = DISPLAY_WIDTH + dim[0] / 2
            self.y = DISPLAY_HEIGHT - dim[1] / 2
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
        # kinematics
        self.dx = 0
        self.dy = 0
        
        self.extended = False

        print(f"{self} created at {self.rect.left}")
        
    def extend(self):
        print(f"{self} extended at {self.rect.left}")
        self.extended = True
        color = D_OLIVE if self.color == OLIVE else OLIVE
        
        extension = Timeline(self.game, left=self.rect.right, color=color)
        self.game.add_entity(extension)
    
    def draw(self):
        super().draw()
        
    
    def update(self):
        super().update()
        
        if self.rect.left <= 0 and not self.extended:
            self.extend()

