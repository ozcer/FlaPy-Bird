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
    
    def __init__(self):
        Game.surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
        pygame.display.set_caption(CAPTION)
        pygame.init()
        
        player = Player((100, 100), (50, 50))
        Game.entities["players"].add(player)
        
        Game.make_walls()
        
        Game.run()
    
        
    @staticmethod
    def run():
        while True:
            Game.surface.fill(LIGHTGREY)
            
            for group in Game.entities:
                Game.entities[group].draw(Game.surface)
                Game.entities[group].update()
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
            Game.fps_clock.tick(FPS)
    
    @staticmethod
    def make_walls():
        gap_height = random.randint(0, DISPLAY_HEIGHT)
        gap_top = gap_height - GAP_SIZE / 2
        gap_bottom = gap_height + GAP_SIZE / 2
    
        top_height = gap_top
        top_wall = Wall((DISPLAY_WIDTH, top_height / 2), (20, top_height))
        Game.entities["walls"].add(top_wall)
    
        bottom_height = DISPLAY_HEIGHT - gap_bottom
        print(f"bottom_height={bottom_height}")
        bottom_wall = Wall((DISPLAY_WIDTH, gap_bottom + bottom_height / 2), (20, bottom_height))
        Game.entities["walls"].add(bottom_wall)
        
        
if __name__ == "__main__":
    Game()