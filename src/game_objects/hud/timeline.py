import random

import pygame

from src.const import *
from src.game_objects.game_object import GameObject
from src.game_objects.hud.period import Period


class Timeline(GameObject):
    
    def __init__(self, game, *args, queue=None, depth=TIMELINE_DEPTH):
        self.images = {"init": pygame.Surface((TL_WIDTH, TIMELINE_HEIGHT))}
        self.images["init"].set_alpha(0)
        x = DISPLAY_WIDTH / 2
        y = DISPLAY_HEIGHT - TIMELINE_HEIGHT / 2
        super().__init__(game, pos=(x, y), depth=depth, init_image_key="init")

        self.debug_font = pygame.font.SysFont("monospace", 20, bold=True)
        
        self.queue = [] if queue is None else list(queue)
        
        # testing purposes only
        self.colors = [RED, GREEN, YELLOW, OLIVE, L_OLIVE, D_OLIVE]
        self.period_count = 1
        self.add_random_period()
        self.add_random_period()
        self.add_random_period()
        self.add_random_period()
        self.add_random_period()
        
    def enqueue(self, period):
        # attach period to last period
        # if doesn't exist, push to left
        last = self.get_last_period()
        new_left = 0 if last is None else last.rect.right
        period.set_left(new_left)
        
        self.queue.append(period)
        self.game.add_entity(period)
    
    def add_random_period(self):
        """
        for testing only, add random period to queue
        :return:
        """
        rand_color = random.choice(self.colors)
        new_period = Period(self.game,
                            length=DISPLAY_WIDTH,
                            name=f"period {self.period_count}",
                            color=rand_color
                            )
        self.enqueue(new_period)
        self.period_count += 1

    def get_current_period(self):
        current = None
        for period in self.queue:
            if period.rect.left >= CURRENT_PERIOD_MARKER:
                break
            current = period
        return current
    
    def get_last_period(self):
        if len(self.queue) == 0:
            last = None
        else:
            last = self.queue[-1]
        return last
    
    def display_current_period(self):
        current = self.get_current_period()
        text = "NO PERIOD" if current is None else current.name
        text_surf = self.debug_font.render(f"{text}",
                                           True,
                                           BLACK)
        text_rect = text_surf.get_rect()
        text_rect.center = (self.rect.left + text_rect.w/2 + 10, self.y)
        self.game.surface.blit(text_surf, text_rect)
    
    def draw(self):
        super().draw()
        self.display_current_period()
    
    def update(self):
        super().update()

