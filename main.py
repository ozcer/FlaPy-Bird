import logging
import os
import random
import sys

import pygame
from pygame.locals import *

from src.game_objects.foes.flying_foe import FlyingFoe
from src.game_objects.foes.scripts.fly_sinusoidal import FlySinusoidal
from src.game_objects.foes.scripts.fly_straight import FlyStraight
from src.game_objects.foes.wall_boss import WallBoss
from src.game_objects.hud.HUD import HUD
from src.const import *
from src.game_objects.backdrop import Backdrop
from src.game_objects.foes.basic_foe import BasicFoe
from src.game_objects.hud.period import Period
from src.game_objects.hud.timeline import Timeline
from src.game_objects.player import Player
from src.game_objects.wall import Wall


class Game:

    def __init__(self):
        # pygame window setups
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # center window
        pygame.init()
        pygame.display.set_caption(CAPTION)
        self.surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
        logging.basicConfig(level=LOG_LEVEL,
                            datefmt='%m/%d/%Y %I:%M:%S%p',
                            format='%(asctime)s %(message)s')
        
        self.pan_speed = PAN_SPEED

        self.entities = {GLOBAL_SPRITE_GROUP: pygame.sprite.Group()}
    
        self.fps_clock = pygame.time.Clock()
        self.hud = HUD(self)
        
        self.timeline = Timeline(self)
        self.add_entity(self.timeline)
        
        self.events = pygame.event.get()

        self.set_up()
        self.run()

    def set_up(self):
        # init player spawn
        player = Player(self, pos=PLAYER_SPAWN)
        self.add_entity(player)

        # init wall cd
        self.wall_cd = 0  # WALL_RATE

        # init monster cd
        self.monster_cd = 5

        wall_boss = WallBoss(self, pos=(1500, 250))
        self.add_entity(wall_boss)

    def run(self):
        while True:
            self.surface.fill(L_GREY)

            self.pan_speed = PAN_SPEED

            # update all objects
            for sprite in self.entities[GLOBAL_SPRITE_GROUP]:
                sprite.update()

            # draw abased on depth
            for sprite in sorted(self.entities[GLOBAL_SPRITE_GROUP],
                                 key=lambda sprite: sprite.depth,
                                 reverse=True):
                sprite.draw()
            

            # monster creation
            random_height = random.randint(DISPLAY_HEIGHT - TIMELINE_HEIGHT -250,
                                           DISPLAY_HEIGHT - TIMELINE_HEIGHT -100)
            pos = (DISPLAY_WIDTH+50, random_height)
            
            foe_type = random.choice([BasicFoe, FlyingFoe])
            new_enemy = foe_type(self,
                                 pos=pos,)
            if self.monster_cd <= 0:
                self.monster_cd = MONSTER_RATE
                self.add_entity(new_enemy)
            self.monster_cd -= 1

            # hud
            self.hud.draw()

            # fps and update display
            pygame.display.update()
            self.fps_clock.tick(FPS)

            self.events = pygame.event.get()
            for event in self.events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_TAB:
                    self.hud.mode_toggle()

    def add_entity(self, object):
        # add to its own sprite group
        class_name = object.__class__.__name__
        if class_name not in self.entities:
            self.entities[class_name] = pygame.sprite.Group()
        self.entities[class_name].add(object)
        logging.info(f"{object} created")

        # also add to global sprite group
        self.entities[GLOBAL_SPRITE_GROUP].add(object)


if __name__ == "__main__":
    Game()
