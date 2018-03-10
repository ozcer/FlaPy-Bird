import pygame

class Kinematic(pygame.sprite.Sprite):
    
    def apply_kinematic(self):
        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y