import pygame
from pygame.locals import *

from src.const import *
from src.game_object.dynamic import Dynamic
from src.game_object.projectile.bullet import Bullet


class Player(Dynamic):
    sprites = {"jump": pygame.image.load("sprites/jump.png"),
               "fall": pygame.image.load("sprites/fall.png")}
    
    def __init__(self, game, *, pos, depth=-5):
        image = Player.sprites["fall"]
        super().__init__(game, pos=pos, depth=depth, image=image)
        
        # dynamics
        self.dx = 0
        self.dy = 0
        
        self.alive = True
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if self.alive:
            # up
            if keys[K_w] and self.dy > -MAX_UP_SPEED:
                self.jump()
        
        for event in self.game.events:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.shoot()
            
    def jump(self):
        self.dy -= UP_ACCEL
        self.image = Player.sprites["jump"]
    
    def shoot(self):
        bullet = Bullet(self.game, (self.x, self.y))
        self.game.add_entity(bullet)
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        self.handle_input()
        
        
        # limit player in screen
        # hitting ceiling
        if self.rect.top < 0:
            correction = self.rect.copy()
            correction.top = 0
            self.x, self.y = correction.center
        # hitting floor
        elif self.rect.bottom > DISPLAY_HEIGHT-TL_HEIGHT:
            correction = self.rect.copy()
            correction.bottom = DISPLAY_HEIGHT-TL_HEIGHT
            self.x, self.y = correction.center
            
            self.dy = 0
        
        if self.dy > 0:
            self.image = Player.sprites["fall"]
        
        # gravity
        self.dy += GRAV if self.dy < MAX_DOWN_SPEED else 0
        
        # off screen death
        if not (0 < self.x < DISPLAY_WIDTH and 0 < self.y < DISPLAY_HEIGHT):
            self.alive = True # False
        