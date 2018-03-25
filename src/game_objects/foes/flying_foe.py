import pygame

from src.const import *
from src.game_objects.foes.foe import Foe
from src.game_objects.foes.scripts.fly_sinusoidal import FlySinusoidal


class FlyingFoe(Foe):
    
    def __init__(self,
                 game, *,
                 pos,
                 script=None,
                 depth=BASIC_FOE_DEPTH):
        script = FlySinusoidal(4, 100, 500, *pos) if script is None else script
        self.images = {"tedders": pygame.image.load("sprites/foesprites/foe2.png")}

        init_image = self.images["tedders"]
        super().__init__(game, pos=pos, script=script, depth=depth, image=init_image)

        # Monster Hp
        self.hp = 50
    
    def draw(self):
        super().draw()

    def update(self):
        super().update()