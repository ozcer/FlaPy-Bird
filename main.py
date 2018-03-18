import sys
import os
import random
import pygame
from pygame.locals import *

from src.const import *
from src.game_object.backdrop import Backdrop
from src.game_object.timeline import Timeline
from src.game_object.player import Player
from src.game_object.wall import Wall
from src.HUD import HUD

class Game:

    def __init__(self, **options):
        # pygame window setups
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # center window
        pygame.init()
        pygame.display.set_caption(CAPTION)
        self.surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
        
        self.pan_speed = PAN_SPEED
        
        self.entities = {GLOBAL_SPRITE_GROUP: pygame.sprite.Group()}

        self.fps_clock = pygame.time.Clock()
        self.hud = HUD(self)
        
        self.events = pygame.event.get()

        #game state
        self.game_state = [STARTING_SCREEN]
        self.done = False
        #Menu font
        self.font = pygame.font.Font(None, 24)

        self.set_up()
        self.run()
    
    def set_up(self):
        # init player spawn
        player = Player(self, pos=(200, 100))
        self.add_entity(player)
    
        # init wall cd
        self.wallCd = 0  # WALL_RATE

        #init monster cd
        self.monsterCd = 5

        # backdrop
        backdrop = Backdrop(self, left=0)
        self.add_entity(backdrop)
        
    def run(self):
        while self.game_state:
            if not self.game_state:
                pygame.quit()
                sys.exit()

            next_state = self.game_state.pop()
            print("Switching state")
            function_name = next_state.replace(" ", "_")
            print(self.game_state)
            if hasattr(self, function_name):
                function = getattr(self, function_name)
                function()
            else:
                pygame.quit()
                sys.exit()
                print("Game over")

    def title_screen(self):
        print("start screen called")
        self.done = False
        while not self.done:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.game_state.append(GAME_SCREEN)
                        self.done = True

            self.surface.fill(OLIVE)
            #Text
            text = "Title Screen"
            self.surface.blit(self.font.render(text, 1, BLACK), (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))

            pygame.display.update()
            self.fps_clock.tick(20)

    def game_screen(self):
        print("game screen called")
        self.done = False
        while not self.done:
            self.surface.fill(L_GREY)

            self.pan_speed = PAN_SPEED
            
            # update all objects
            for sprite in self.entities[GLOBAL_SPRITE_GROUP]:
                sprite.update()
            
            # draw abased on depth
            for sprite in sorted(self.entities[GLOBAL_SPRITE_GROUP],
                                 key=lambda sprite: sprite.depth,
                                 reverse=True):
                sprite.draw()
                
            # wall creation
            if self.wallCd <= 0:
                self.wallCd = WALL_RATE
                self.make_walls()
            self.wallCd -= 1

            # monster creation
            new_enemy = BasicFoe(self)
            if self.monsterCd <= 0:
                self.monsterCd = MONSTER_RATE
                self.add_entity(new_enemy)
            self.monsterCd -= 1

            # hud
            self.hud.draw()
            
            # fps and update display
            pygame.display.update()
            self.fps_clock.tick(FPS)
            
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_TAB:
                        self.hud.mode_toggle()
                    elif event.key == K_ESCAPE:
                        self.game_state.append(STARTING_SCREEN)
                        Game.run(self)

    def pause_menu(self):
        pass

    def add_entity(self, object):
        # add to its own sprite group
        class_name = object.__class__.__name__
        if class_name not in self.entities:
            self.entities[class_name] = pygame.sprite.Group()
        self.entities[class_name].add(object)
        
        # also add to global sprite group
        self.entities[GLOBAL_SPRITE_GROUP].add(object)
    
    def make_walls(self):
        gap_height = random.randint(GAP_SIZE/2, DISPLAY_HEIGHT-GAP_SIZE/2)
        gap_top = gap_height - GAP_SIZE / 2
        gap_bottom = gap_height + GAP_SIZE / 2
        
        # # top wall
        # top_height = gap_top
        # top_wall = Wall(self, (DISPLAY_WIDTH+WALL_WIDTH, top_height / 2), (WALL_WIDTH, top_height))
        # self.add_entity(top_wall)
    
        # bottom wall
        bottom_height = DISPLAY_HEIGHT - gap_bottom
        bottom_wall = Wall(self,
                           pos=(DISPLAY_WIDTH + WALL_WIDTH, gap_bottom + bottom_height / 2),
                           dim=(WALL_WIDTH, bottom_height))
        self.add_entity(bottom_wall)


if __name__ == "__main__":
    Game()
