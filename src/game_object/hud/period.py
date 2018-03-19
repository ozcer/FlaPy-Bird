import pygame

from src.const import *
from src.game_object.dynamic import Dynamic


class Period(Dynamic):
    def __init__(self, game, *,
                 length,
                 name,
                 left=DISPLAY_WIDTH,
                 depth=PERIOD_DEPTH,
                 color=OLIVE,
                 ):
        image = pygame.Surface((length, TL_HEIGHT))
        x = left + length / 2
        y = DISPLAY_HEIGHT - TL_HEIGHT / 2
        super().__init__(game, pos=(x, y), depth=depth, image=image)
        
        self.name = name
        
        self.color = color
        self.image.fill(self.color)
        
        self.dx = -self.game.pan_speed
        self.dy = 0
    
    def set_left(self, left):
        self.x = left + self.rect.w / 2
        self.y = DISPLAY_HEIGHT - TL_HEIGHT / 2
    
    def draw(self):
        super().draw()
        name_surf = self.debug_font.render(f"{self.name}",
                               True,
                               BLACK)
        self.game.surface.blit(name_surf, (self.x, self.y))
    
    def update(self):
        super().update()