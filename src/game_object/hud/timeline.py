import random

import pygame

from src.const import *
from src.game_object.game_object import GameObject
from src.game_object.hud.period import Period


class Timeline(GameObject):
    
    def __init__(self, game, *, frontlog=None, backlog=None, depth=TIMELINE_DEPTH):
        image = pygame.Surface((TL_WIDTH, TL_HEIGHT))
        x = DISPLAY_WIDTH / 2
        y = DISPLAY_HEIGHT - TL_HEIGHT / 2
        super().__init__(game, pos=(x, y), depth=depth, image=image)

        self.debug_font = pygame.font.SysFont("monospace", 20, bold=True)
        
        self.frontlog = [] if frontlog is None else frontlog
        self.backlog = [] if frontlog is None else backlog
        
        # placeholders
        self.colors = [RED, GREEN, YELLOW]
        
        self.period_count = 1
        
        self.frontlog.append(self.random_period(left=0))
        self.add_period(self.random_period())
        self.add_period(self.random_period())
        
        
    def add_period(self, period):
        self.backlog.append(period)
    
    def random_period(self, left=DISPLAY_WIDTH):
        new_period = Period(self.game,
                            length=DISPLAY_WIDTH,
                            name=f"period {self.period_count}",
                            color=random.choice(self.colors),
                            left=left)
        self.period_count += 1
        
        return new_period

    def expose_period(self):
        """
        move the first in backlog to end of frontlog
        :return: None
        """
        newcomer = self.backlog.pop(0)
        # attach to last period in frontlog
        if len(self.frontlog) > 0:
            newcomer.set_left(self.frontlog[-1].rect.right)
        else:
            newcomer.set_left(DISPLAY_WIDTH)
        self.frontlog.append(newcomer)
    
    def display_current_period(self):
        name = "NO PERIOD" if len(self.frontlog) == 0 else self.frontlog[0].name
        text_surf = self.debug_font.render(f"{name}",
                                                True,
                                                BLACK)
        text_rect = text_surf.get_rect()
        text_rect.center = (self.rect.left + text_rect.w/2 + 10, self.y)
        self.game.surface.blit(text_surf, text_rect)
        
    def draw(self):
        super().draw()
        
        for period in self.frontlog:
            period.draw()
        
        self.display_current_period()
        
    
    def update(self):
        super().update()
        for period in self.frontlog:
            period.update()
        
        # remove from frontlog once moves off screen
        if (len(self.frontlog) > 0) and (self.frontlog[0].rect.right < 0):
            self.frontlog.pop(0)
            
        # if last period in front log is almost done exposing
        # the whole image, start exposing the next
        if ((len(self.frontlog)==0 or
             self.frontlog[-1].rect.right <= DISPLAY_WIDTH) and
           len(self.backlog) > 0):
            self.expose_period()
            self.add_period(self.random_period())

