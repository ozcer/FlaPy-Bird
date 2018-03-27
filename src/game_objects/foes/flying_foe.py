import pygame

from src.const import *
from src.game_objects.foes.foe import Foe
from src.game_objects.foes.scripts.fly_sinusoidal import FlySinusoidal


class FlyingFoe(Foe):
    
    def __init__(self, *args, pos, script=None, depth=BASIC_FOE_DEPTH, image_scale=(1.5,1.5), **kwargs):
        self.images = {"tedders": pygame.image.load("sprites/foesprites/foe2.png")}
        script = FlySinusoidal(4, 100, 500, *pos) if script is None else script
        super().__init__(*args,
                         pos=pos,
                         script=script,
                         depth=depth,
                         init_image_key="tedders",
                         image_scale=image_scale,
                         **kwargs)
        
        # Monster Hp
        self.hp = 50
    
    def draw(self):
        super().draw()

    def update(self):
        super().update()