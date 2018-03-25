import random

import pygame

from src.const import *
from src.game_object.foe.foe import Foe


class BasicFoe(Foe):
    

    def __init__(self,
                 game, *,
                 pos,
                 depth=BASIC_FOE_DEPTH):
        self.images = {"ooze": pygame.image.load("sprites/foesprites/foe1.png"),
                       "tedders": pygame.image.load("sprites/foesprites/foe2.png")}
        init_image = random.choice(list(self.images.items()))[1]
        super().__init__(game, pos=pos, depth=depth, image=init_image)
        
        # Movement
        self.dx = -5

        # Monster Hp
        self.hp = 50

    def draw(self):
        super().draw()

    def update(self):
        super().update()

