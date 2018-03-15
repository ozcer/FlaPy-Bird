import pygame
from src.const import *

class GameObject(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.debug_font = pygame.font.SysFont("monospace", 20)
    
    def update(self):
        pass
    
    def show_attribute(self):
        # members = [attr for attr in dir(self)
        #            if not callable(getattr(self, attr))
        #            and not attr.startswith("__")]
        #
        # displays = []
        # for member in members:
        #     displays.append(self.debug_font.render(f"{member}={getattr(self, member)}",
        #                                            True,
        #                                            GREEN)
        #                     )
        # print(displays)
        #
        # for index, display in enumerate(displays):
        #     self.game.surface.blit(display, (self.x, self.y + display.get_rect().h * index))
        show = self.debug_font.render(f"{self.dx}={getattr(self, 'dx')}",
                                               True,
                                               GREEN)
        self.game.surface.blit(show, (self.x, self.y))
        