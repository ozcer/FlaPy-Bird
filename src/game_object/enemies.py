import pygame
from pygame.locals import *

from src.const import *
from src.game_object.dynamic import *

class enemies(Dynamic):
    depth = -4
    def __init__(self, game):
        super().__init__()
        self.game = game

        # sprite
        self.sprites = {"ooze": pygame.image.load("sprites/monster1.png")}
        self.type = {"basic"}

        self.image = self.sprites["ooze"]

        self.x = DISPLAY_WIDTH + 50
        self.y = DISPLAY_HEIGHT/2

        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.width = self.rect.width
        self.height = self.rect.height

        self.dx = -1
        self.dy = 0

        self.alive = True

    def draw(self):
        super().draw()

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y
