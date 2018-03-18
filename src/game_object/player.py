import pygame
from pygame.locals import *

from src.const import *
from src.game_object.dynamic import Dynamic
from src.game_object.projectile.bullet import Bullet


class Player(Dynamic):
    sprites = {"jump": pygame.image.load("sprites/jump.png"),
               "fall": pygame.image.load("sprites/fall.png")}

    def __init__(self, game, pos, depth=-5):
        super().__init__()
        self.game = game
        
        # sprites
        self.image = Player.sprites["fall"]
        self.depth = depth
        
        # hitbox
        self.rect = self.image.get_rect()
        self.x, self.y = pos
        self.rect.center = self.x, self.y
        self.width = self.rect.width
        self.height = self.rect.height
        
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
        self.image = self.sprites["jump"]
    
    def shoot(self):
        bullet = Bullet(self.game, (self.x, self.y))
        self.game.add_entity(bullet)
    
    def draw(self):
        super().draw()
    
    def update(self):
        self.handle_input()
        
        if self.dy > 0:
            self.image = self.sprites["fall"]
        
        # gravity
        self.dy += GRAV if self.dy < MAX_DOWN_SPEED else 0
        
        # off screen death
        if not (0 < self.x < DISPLAY_WIDTH and 0 < self.y < DISPLAY_HEIGHT):
            self.alive = True # False

        # apply kinematics
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y
