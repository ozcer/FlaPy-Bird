import sys

import pygame
from pygame.locals import *

from src.const import *
from src.player import Player

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


if __name__ == "__main__":
    Game()