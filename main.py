import sys
import random
import pygame
from pygame.locals import *

from src.const import *
from src.player import Player
from src.wall import Wall

class Game:
    surface = None
    sprite_groups = ["players", "walls"]
    entities = {sp: pygame.sprite.Group() for sp in sprite_groups}
    fps_clock = pygame.time.Clock()
    
    wallCd = WALL_RATE/2

    player = Player((200, 100))
    entities["players"].add(player)
    
    def __init__(self):
        Game.surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
        pygame.display.set_caption(CAPTION)
        pygame.init()

        Game.run()
    
        
    @staticmethod
    def run():
        while True:
            Game.surface.fill(LIGHTGREY)
            
            for group in Game.entities:
                Game.entities[group].update()
                Game.entities[group].draw(Game.surface)
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
            # wall creation
            if Game.wallCd <= 0:
                Game.wallCd = WALL_RATE
                Game.make_walls()
            Game.wallCd -= 1
            
            # collision
            collision = pygame.sprite.groupcollide(Game.entities["walls"], Game.entities["players"], False, False)
            if collision:
                for wall in collision:
                    collision[wall][0].hit = True
                    wall.hit = True
                    
            pygame.display.update()
            Game.fps_clock.tick(FPS)

    @staticmethod
    def make_walls():
        gap_height = random.randint(GAP_SIZE/2, DISPLAY_HEIGHT-GAP_SIZE/2)
        gap_top = gap_height - GAP_SIZE / 2
        gap_bottom = gap_height + GAP_SIZE / 2
    
        top_height = gap_top
        top_wall = Wall((DISPLAY_WIDTH+WALL_WIDTH, top_height / 2), (WALL_WIDTH, top_height))
        Game.entities["walls"].add(top_wall)
    
        bottom_height = DISPLAY_HEIGHT - gap_bottom
        bottom_wall = Wall((DISPLAY_WIDTH+WALL_WIDTH, gap_bottom + bottom_height / 2), (WALL_WIDTH, bottom_height))
        Game.entities["walls"].add(bottom_wall)
        
        
if __name__ == "__main__":
    Game()