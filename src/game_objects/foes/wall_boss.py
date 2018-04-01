import random

import pygame

from src.const import *
from src.game_objects.foes.foe import Foe
from src.game_objects.foes.scripts.fly_straight import FlyStraight
from src.game_objects.foes.scripts.wall_boss_script import WallBossScript


class WallBoss(Foe):
    
    def __init__(self, *args,
                 depth=BASIC_FOE_DEPTH+10,
                 image_scale=(2,2),
                 script=WallBossScript(1,1000),
                 **kwargs, ):
        image = pygame.image.load("sprites/foesprites/smash.png").convert_alpha()
        self.images = {"init": image}
        super().__init__(*args,
                         depth=depth,
                         script=script,
                         image_scale=image_scale,
                         init_image_key="init",
                         **kwargs, )
        
        # Monster Hp
        self.hp = 1000
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        self.m = pygame.mask.from_surface(self.image)
