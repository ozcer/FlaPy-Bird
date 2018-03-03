import sys

import pygame as pg
from pygame.locals import *

from src.const import *


class Game():
    def __init__(self):
        self.surface = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
        pg.display.set_caption(CAPTION)
        pg.init()
        
        self.run()
    
    def run(self):
        while True:
            self.surface.fill(LIGHTGREY)
            
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.update()


if __name__ == "__main__":
    Game()