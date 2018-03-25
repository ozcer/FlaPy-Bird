import logging
import os
import random
import sys

import pygame
from pygame.locals import *

from src.game_objects.foes.scripts.fly_sinusoidal import FlySinusoidal
from src.game_objects.foes.scripts.fly_straight import FlyStraight
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

        # backdrop
        # backdrop = Backdrop(self, left=0)
        # self.add_entity(backdrop)

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
            

            # wall creation
            if self.wall_cd <= 0:
                self.wall_cd = WALL_RATE
                self.make_walls()
            self.wall_cd -= 1

            # monster creation
            random_height = random.randint(DISPLAY_HEIGHT - TIMELINE_HEIGHT -250,
                                           DISPLAY_HEIGHT - TIMELINE_HEIGHT -100)
            pos = (DISPLAY_WIDTH, random_height)
            new_enemy = BasicFoe(self,
                                 pos=pos,
                                 script=FlySinusoidal(4, 100, 500, *pos))
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

    def make_walls(self):
        gap_height = random.randint(GAP_SIZE / 2, DISPLAY_HEIGHT - TIMELINE_HEIGHT - GAP_SIZE / 2)
        gap_top = gap_height - GAP_SIZE / 2
        gap_bottom = gap_height + GAP_SIZE / 2

        # # top wall
        # top_height = gap_top
        # top_wall = Wall(self, (DISPLAY_WIDTH+WALL_WIDTH, top_height / 2), (WALL_WIDTH, top_height))
        # self.add_entity(top_wall)

        # bottom wall
        bottom_height = DISPLAY_HEIGHT - TIMELINE_HEIGHT - gap_bottom
        bottom_wall = Wall(self,
                           pos=(DISPLAY_WIDTH + WALL_WIDTH, gap_bottom + bottom_height / 2),
                           dim=(WALL_WIDTH, bottom_height))
        self.add_entity(bottom_wall)


if __name__ == "__main__":
    Game()
