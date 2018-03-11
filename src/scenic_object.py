import pygame

from src.const import *

class ScenicObject(pygame.sprite.Sprite):
    
    def decayable(self):
        """
        check if is too far out from main surface
        :return: bool
        """
        # active zone = main surface x 2
        active_zone = self.game.surface.get_rect().inflate(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)
        return not active_zone.colliderect(self.rect)
    
    
    def pan(self):
        self.x += -self.game.pan_speed
        
        if self.decayable():
            print(f"{self} decaying")
            self.kill()
    