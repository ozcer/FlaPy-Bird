import random

from src.game_object.Foe.foe import *


class BasicFoe(Foe):
    def __init__(self,
                 game,
                 pos=(DISPLAY_WIDTH + 50, DISPLAY_HEIGHT/2),
                 depth=-4):
        #Sprite
        self.sprites = {"ooze": pygame.image.load("sprites/foesprites/foe1.png"),
                        "tedders": pygame.image.load("sprites/foesprites/foe2.png")}
        self.image = random.choice(list(self.sprites.items()))[1]

        #Movement
        self.dx = -5
        self.dy = 0

        #Monster Hp
        self.hp = 50

        super().__init__(game, pos, depth, self.image)

    def draw(self):
        Foe.draw(self)

    def update(self):
        Foe.update(self)
