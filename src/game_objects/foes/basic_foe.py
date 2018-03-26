import random

import pygame

from src.const import *
from src.game_objects.foes.foe import Foe
from src.game_objects.foes.scripts.fly_straight import FlyStraight


class BasicFoe(Foe):
    

    def __init__(self,
                 game, *,
                 pos,
                 script=FlyStraight(5),
                 depth=BASIC_FOE_DEPTH,
                 image_scale=(2,2),):
        self.images = {"ooze": pygame.image.load("sprites/foesprites/foe1.png")}

        super().__init__(game,
                         pos=pos,
                         script=script,
                         depth=depth,
                         init_image_key="ooze",
                         image_scale=image_scale)
        
        # Monster Hp
        self.hp = 200

    def draw(self):
        super().draw()


    def update(self):
        super().update()

        if self.rect.bottom > DISPLAY_HEIGHT - TIMELINE_HEIGHT:
            correction = self.rect.copy()
            correction.bottom = DISPLAY_HEIGHT - TIMELINE_HEIGHT
            self.x, self.y = correction.center
            self.dy = 0
        
        # gravity
        if not self._on_ground():
            self._gravity()

