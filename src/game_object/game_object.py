import logging
import pygame

from src.const import *


class GameObject(pygame.sprite.Sprite):
    
    def __init__(self,
                 game, *,
                 pos,
                 depth,
                 image,
                 ):
        """
        General game object
        :param game: Game
        :param pos: (x,y)
        :param depth: int
        :param image: pygame.Surface
        """
        super().__init__()
        self.game=game
        
        # hit box and positioning
        self.x, self.y = pos
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
        # draw depth, larger=more behind
        self.depth = depth
        
        # zone which sprites doesn't delete itself
        self.nondecay_zone = self.game.surface.get_rect()
        
        # font for debug attributes
        self.debug_font = pygame.font.SysFont("monospace", 12)
    
    def update(self):
        if self.decayable():
            logging.info(f"{self} decayed")
            self.kill()
    
    def draw(self):
        self.game.surface.blit(self.image, self.rect)
        if self.game.hud.dev_mode:
            self.show_attributes()
        
    def show_attributes(self):
        members = [attr for attr in dir(self)
                   if not callable(getattr(self, attr))
                   and not attr.startswith("__")]
    
        attribute_surfaces = []
        for member in members:
            attribute_surfaces.append(self.debug_font.render(f"{member}={getattr(self, member)}",
                                                   True,
                                                   GREEN)
                            )
        for index, display in enumerate(attribute_surfaces):
            self.game.surface.blit(display, (self.x, self.y + display.get_rect().h * index))

    def decayable(self):
        """
        defauls to not decay
        :return: bool
        """
        return False
    
    def __str__(self):
        return f"{self.__class__.__name__} at {self.x, self.y}"