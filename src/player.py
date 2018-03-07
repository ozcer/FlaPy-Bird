import pygame
from pygame.locals import *

from src.const import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos,):
        pygame.sprite.Sprite.__init__(self)

        # sprite
        self.sprites = {"jump": pygame.image.load("sprites/jump.png"),
                        "fall": pygame.image.load("sprites/fall.png")}
        self.image = self.sprites["fall"]

        self.x, self.y = pos
        
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.width = self.rect.width
        self.height = self.rect.height
        
        
        # kinematics
        self.dx = 0
        self.dy = 0
        
        self.hit = False
    
    # def draw(self, surface):
    #     surface.blit(self.image, (self.x, self.y), (self.sprite_index*self.width, 0, self.width, self.height))
    
    def update(self):
        if not self.hit:
            # jumping
            keys = pygame.key.get_pressed()
            if keys[K_SPACE] and self.dy >= 0:
                self.dy -= 10

        self.image = self.sprites["jump"] if self.dy < 0 else self.sprites["fall"]
        
        # gravity
        self.dy += GRAV if self.dy < TERM_VEL else 0
        
        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y
