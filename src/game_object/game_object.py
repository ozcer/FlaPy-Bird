import pygame

from src.const import *


class GameObject(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.debug_font = pygame.font.SysFont("monospace", 17)
    
    def update(self):
        if self.decayable():
            self.kill()
    
    def draw(self):
        self.game.surface.blit(self.image, self.rect)
        if self.game.hud.dev_mode:
            self.show_attributes()
        
    def show_attributes(self):
        members = [attr for attr in dir(self)
                   if not callable(getattr(self, attr))
                   and not attr.startswith("__")]
    
        displays = []
        for member in members:
            displays.append(self.debug_font.render(f"{member}={getattr(self, member)}",
                                                   True,
                                                   GREEN)
                            )
        for index, display in enumerate(displays):
            self.game.surface.blit(display, (self.x, self.y + display.get_rect().h * index))

    def decayable(self):
        """
        check if is too far out from main surface
        :return: bool
        """
        # active zone = main surface x 2
        active_zone = self.game.surface.get_rect().inflate(self.rect.width*2, DISPLAY_HEIGHT/2)
        return not active_zone.colliderect(self.rect)
