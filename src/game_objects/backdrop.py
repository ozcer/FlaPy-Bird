import pygame

from src.const import *
from src.game_objects.scenic import Scenic
from src.game_objects.dynamic import Dynamic


class Backdrop(Scenic):
    
    def __init__(self, game,
                 left=None,
                 dim=(BACKDROP_WIDTH, BACKDROP_HEIGHT),
                 color=L_GREY,
                 depth=BACKDROP_DEPTH):
        image = pygame.Surface(dim)
        if left is not None:
            x = left + dim[0] / 2
        # default spawn at right of screen
        else:
            x = DISPLAY_WIDTH + dim[0] / 2
        y = DISPLAY_HEIGHT/2
        
        super().__init__(game, pos=(x,y), depth=depth, image=image)
        
        self.color = color
        self.image.fill(self.color)
        
        self.extended = False

    
    def extend(self):
        self.extended = True
        color = D_GREY if self.color == L_GREY else L_GREY
        
        extension = Backdrop(self.game, left=self.rect.right, color=color)
        self.game.add_entity(extension)
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        if self.rect.left <= 0 and not self.extended:
            self.extend()

