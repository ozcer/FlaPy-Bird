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
                 depth=BASIC_FOE_DEPTH):
        self.images = {"ooze": pygame.image.load("sprites/foesprites/foe1.png")}
        init_image = self.images["ooze"]
        super().__init__(game, pos=pos, script=script, depth=depth, image=init_image)
        
        # Monster Hp
        self.hp = 50

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

