import pygame

from src.const import *
from src.game_objects.foes.foe import Foe
from src.game_objects.projectiles.projectile import Projectile

class Bullet(Projectile):
    
    def __init__(self,
                 game, *,
                 pos,
                 dim=(10,10),
                 depth=BULLET_DEPTH):
        self.images = {0: pygame.Surface(dim)}
        super().__init__(game, pos=pos, depth=depth,image=self.images[0])
        self.game = game
        
        self.image.fill(YELLOW)
        
        # kinematics
        self.dx = 8
        
        self.damage = 35
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()

        collidee = self.collide_with_class(Foe)
        if collidee:
            collidee.hp -= self.damage
            self.kill()
