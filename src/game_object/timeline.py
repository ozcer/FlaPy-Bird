import pygame

from src.const import *
from src.game_object.scenic import Scenic
from src.game_object.dynamic import Dynamic


class Timeline(Scenic):
    
    def __init__(self, game,
                 left=None,
                 dim=(TL_WIDTH, TL_HEIGHT),
                 color=OLIVE,
                 depth=0):
        super().__init__()
        self.game = game
        
        # graphics
        self.image = pygame.Surface(dim)
        self.color = color
        self.image.fill(self.color)
        self.depth = depth
        
        # position and hitbox
        if left is not None:
            self.x = left+ dim[0]/2
            self.y = DISPLAY_HEIGHT - dim[1]/2
        # default spawn at right of screen
        else:
            self.x = DISPLAY_WIDTH + dim[0] / 2
            self.y = DISPLAY_HEIGHT - dim[1] / 2
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
        # dynamics
        self.dx = 0
        self.dy = 0
        
        self.extended = False
        
    def extend(self):
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

