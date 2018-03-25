import pygame
from pygame.locals import *

from src.const import *
from src.gfx_helpers import *
from src.game_object.dynamic import Dynamic
from src.game_object.hud.timeline import Timeline
from src.game_object.projectile.bullet import Bullet


class Player(Dynamic):
    
    def __init__(self, game, *,
                 pos,
                 depth=PLAYER_DEPTH,
                 image_scale=(2.5,2.5)):
        self.images = {"jump": pygame.image.load("sprites/jump.png"),
                       "fall": pygame.image.load("sprites/fall.png")}
        init_image = self.images["fall"]
        super().__init__(game, pos=pos, depth=depth, image=init_image, image_scale=image_scale)
        
        self.hp = 200
        
    def is_alive(self):
        return self.hp > 0
    
    def handle_input(self):
        # keyboard input
        keys = pygame.key.get_pressed()
        if keys[K_w] and self._on_ground():
            self.jump()
        
        # left click
        for event in self.game.events:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                pass
            if event.type == KEYDOWN and event.key == K_j:
                self.shoot()
    
    def _on_ground(self):
        # make a rect with height of 1 pixel
        # put it under the player and see if that collides with timeline
        detect_rect = pygame.Rect((0, 0), (self.rect.w, 1))
        detect_rect.top = self.rect.bottom
        for entity in self.game.entities[GLOBAL_SPRITE_GROUP]:
            if isinstance(entity, Timeline) and detect_rect.colliderect(entity.rect):
                return True
        return False
    
    def _gravity(self):
        """
        affect subject with gravitational forces
        :return: None
        """
        if self.dy < MAX_DOWN_SPEED:
            self.dy += GRAV
    
    def jump(self):
        self.dy -= PLAYER_JUMP_POWER
        self.set_image(self.images["jump"])
    
    def shoot(self):
        bullet = Bullet(self.game, pos=(self.x, self.y))
        self.game.add_entity(bullet)
    
    def draw(self):
        #self.draw_hitbox()
        super().draw()
    
    def update(self):
        super().update()
        if self.is_alive():
            self.handle_input()
        
        # limit player in screen
        # hitting ceiling
        if self.rect.top < 0:
            correction = self.rect.copy()
            correction.top = 0
            self.x, self.y = correction.center
        # hitting floor
        elif self.rect.bottom > DISPLAY_HEIGHT-TIMELINE_HEIGHT:
            correction = self.rect.copy()
            correction.bottom = DISPLAY_HEIGHT - TIMELINE_HEIGHT
            self.x, self.y = correction.center
            self.dy = 0
        
        if self.dy > 0:
            self.set_image(self.images["fall"])
        
        # gravity
        if not self._on_ground():
            self._gravity()
