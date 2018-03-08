import pygame

from src.const import *


class HUD():
    
    def __init__(self, game):
        self.game = game
        
        self.fonts = {"fps": pygame.font.SysFont("monospace", 20)}
    
    def render(self):
        fps_display = self.fonts["fps"].render(f"{round(self.game.fps_clock.get_fps())}",
                                               True,
                                               BLACK)
        self.game.surface.blit(fps_display, (DISPLAY_WIDTH-fps_display.get_width(),0))