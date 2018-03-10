import sys
import random
import pygame
from pygame.locals import *

from src.const import *
from src.floor import Floor
from src.game_object.player import Player
from src.game_object.wall import Wall
from src.HUD import HUD

class Game:
    
    def __init__(self):
        # surfaces
        self.surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
        pygame.display.set_caption(CAPTION)
        pygame.init()
        
        self.pan_speed = PAN_SPEED
        
        self.entities = {}

        self.fps_clock = pygame.time.Clock()
        self.hud = HUD(self)
        
        self.set_up()
        self.run()
    
    def set_up(self):
        # init player spawn
        player = Player(self, (200, 100))
        self.add_entity(player)
        #self.entities["players"].add(player)
    
        # init wall cd
        self.wallCd = 0 #WALL_RATE
        
        # floor
        floor = Floor(self)
        self.add_entity(floor)
        
    def run(self):
        while True:
            self.surface.fill(LIGHTGREY)

            self.pan_speed = PAN_SPEED
            
            for cls in sorted(self.entities,
                              key=lambda cls: self.entities[cls].sprites()[0].depth,
                              reverse=True):
                print(cls, self.entities[cls].sprites()[0].depth)
                self.entities[cls].update()
                self.entities[cls].draw(self.surface)
                
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            # wall creation
            if self.wallCd <= 0:
                self.wallCd = WALL_RATE
                self.make_walls()
            self.wallCd -= 1

            # # collision
            # collision = pygame.sprite.groupcollide(self.entities["walls"], self.entities["players"], False, False)
            # if collision:
            #     for wall in collision:
            #         collision[wall][0].alive = False
            #         wall.hit = True
            
            self.hud.render()

            pygame.display.update()
            self.fps_clock.tick(FPS)
    
    def add_entity(self, object):
        class_name = object.__class__.__name__
        if class_name not in self.entities:
            self.entities[class_name] = pygame.sprite.Group()
        self.entities[class_name].add(object)
    
    def make_walls(self):
        gap_height = random.randint(GAP_SIZE/2, DISPLAY_HEIGHT-GAP_SIZE/2)
        gap_top = gap_height - GAP_SIZE / 2
        gap_bottom = gap_height + GAP_SIZE / 2
        
        # top wall
        top_height = gap_top
        top_wall = Wall(self, (DISPLAY_WIDTH+WALL_WIDTH, top_height / 2), (WALL_WIDTH, top_height))
        self.add_entity(top_wall)
    
        # bottom wall
        bottom_height = DISPLAY_HEIGHT - gap_bottom
        bottom_wall = Wall(self, (DISPLAY_WIDTH+WALL_WIDTH, gap_bottom + bottom_height / 2), (WALL_WIDTH, bottom_height))
        self.add_entity(bottom_wall)
        
        
if __name__ == "__main__":
    Game()