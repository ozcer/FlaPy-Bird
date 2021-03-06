import random

import pygame

from src.const import *
from src.game_objects.foes.foe import Foe
from src.game_objects.foes.scripts.fly_straight import FlyStraight


class BasicFoe(Foe):
    
    def __init__(self, *args,
                 script=FlyStraight(5),
                 depth=BASIC_FOE_DEPTH,
                 image_scale=(2,2),
                 **kwargs,):
        self.images = {"ooze": pygame.image.load("sprites/foesprites/foe1.png")}

        super().__init__(*args,
                         script=script,
                         depth=depth,
                         init_image_key="ooze",
                         image_scale=image_scale,
                         **kwargs, )
        
        # Monster Hp
        self.hp = 200

    def draw(self):
        super().draw()

    def update(self):
        super().update()
        self.gravitate()

