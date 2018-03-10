import pygame

class ScenicObject(pygame.sprite.Sprite):

    def pan(self):
        self.x += -self.game.pan_speed
    