import pygame

from src.const import *
from src.game_object.scenic import Scenic
from src.game_object.dynamic import Dynamic


class Backdrop(Scenic):
    depth = 10
    
    def __init__(self, game, left=None, dim=(BACKDROP_WIDTH, BACKDROP_HEIGHT), color=L_GREY):
        super().__init__()
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
        
        print(f"{self} created at {self.rect.left}")
    
    def extend(self):
        self.extended = True
        color = D_GREY if self.color == L_GREY else L_GREY
        
        extension = Backdrop(self.game, left=self.rect.right, color=color)
        print(f"{extension} extended at {extension.rect.left}")
        self.game.add_entity(extension)
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        if self.rect.left <= 0 and not self.extended:
            self.extend()

