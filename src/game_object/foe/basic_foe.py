import random

import pygame

from src.const import *
from src.game_object.foe.foe import Foe


class BasicFoe(Foe):
    sprites = {"ooze": pygame.image.load("sprites/foesprites/foe1.png"),
               "tedders": pygame.image.load("sprites/foesprites/foe2.png")}

    def __init__(self,
                 game, *,
                 pos,
                 depth=BASIC_FOE_DEPTH):
        image = random.choice(list(BasicFoe.sprites.items()))[1]
        super().__init__(game, pos=pos, depth=depth, image=image)
        
        # Movement
        self.dx = -5

        # Monster Hp
        self.hp = 100

    def draw(self):
        super().draw()

    def update(self):
        super().update()

